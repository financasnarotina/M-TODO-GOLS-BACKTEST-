import re
from typing import Optional
from app.engine.models import Etapa0


def parse_etapa0_from_text(text: str) -> Optional[Etapa0]:
    patterns = {
        'banca_inicial': r'banca\s*inicial\s*[:=]\s*([\d\.,]+)',
        'meta_final': r'meta\s*final\s*[:=]\s*([\d\.,]+)',
        'n_entradas_max': r'n\s*entradas\s*max\s*[:=]\s*(\d+)',
        'nome_do_projeto': r'nome\s*do\s*projeto\s*[:=]\s*(.+)',
        'casa_de_aposta': r'casa\s*de\s*aposta\s*[:=]\s*(.+)',
        'stake_real_padrao': r'stake\s*real\s*padrao\s*[:=]\s*([\d\.,]+)',
    }
    found = {}
    for key, pattern in patterns.items():
        m = re.search(pattern, text, flags=re.IGNORECASE)
        if m:
            found[key] = m.group(1).strip()
    if len(found) < 6:
        return None
    def br_num(v: str) -> float:
        return float(v.replace('.', '').replace(',', '.')) if ',' in v else float(v)
    return Etapa0(
        banca_inicial=br_num(found['banca_inicial']),
        meta_final=br_num(found['meta_final']),
        n_entradas_max=int(found['n_entradas_max']),
        nome_do_projeto=found['nome_do_projeto'],
        casa_de_aposta=found['casa_de_aposta'],
        stake_real_padrao=br_num(found['stake_real_padrao']),
    )
