from math import pow
from app.engine.models import Etapa0


def odd_media_necessaria_inicial(etapa0: Etapa0) -> float:
    return round(pow(etapa0.meta_final / etapa0.banca_inicial, 1 / etapa0.n_entradas_max), 4)


def odd_media_necessaria_restante(meta_final: float, banca_atual: float, entradas_restantes: int) -> float:
    if entradas_restantes <= 0:
        return 0.0
    return round(pow(meta_final / banca_atual, 1 / entradas_restantes), 4)


def classificar_trajetoria(odd_restante: float) -> str:
    if odd_restante <= 2.0:
        return "Coerente"
    if odd_restante <= 2.5:
        return "Pressionada"
    return "Critica"
