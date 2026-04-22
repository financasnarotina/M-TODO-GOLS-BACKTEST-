from typing import List
from app.engine.models import Etapa0, MethodEvaluation
from app.engine.etapa0 import (
    odd_media_necessaria_inicial,
    odd_media_necessaria_restante,
    classificar_trajetoria,
)


def build_pre_game_response(
    etapa0: Etapa0,
    banca_atual: float,
    entrada_atual: int,
    avaliacoes: List[MethodEvaluation],
) -> str:
    entradas_restantes = max(etapa0.n_entradas_max - entrada_atual + 1, 0)
    odd_ini = odd_media_necessaria_inicial(etapa0)
    odd_rest = odd_media_necessaria_restante(
        etapa0.meta_final,
        banca_atual,
        max(entradas_restantes, 1),
    )
    status = classificar_trajetoria(odd_rest)

    linhas: list[str] = []
    linhas.append("1. Etapa 0 resumida")
    linhas.append(
        f"Projeto: {etapa0.nome_do_projeto} | Casa: {etapa0.casa_de_aposta} | "
        f"Stake padrão: {etapa0.stake_real_padrao}"
    )
    linhas.append("2. Bloco financeiro")
    linhas.append(
        f"Banca inicial: {etapa0.banca_inicial} | Banca atual: {banca_atual} | "
        f"Odd média inicial: {odd_ini} | Odd média restante: {odd_rest} | Status: {status}"
    )
    linhas.append("7. Bloco explícito por método testado")
    for a in avaliacoes:
        linhas.append(
            f"- {a.method_code} | {a.status} | {a.evidence_type} | {a.market} | {a.objective}"
        )
        for i, c in enumerate(a.criteria_results, start=1):
            linhas.append(
                f"  C{i}: {c.label} | corte={c.cutoff} | dado={c.found} | "
                f"status={'PASSOU' if c.passed else 'FALHOU'}"
            )
        linhas.append(f"  Decisão final: {'APROVADO' if a.passed else 'BLOQUEADO'}")
        if a.blocks:
            linhas.append(f"  Bloqueios: {'; '.join(a.blocks)}")
    return "\n".join(linhas)
