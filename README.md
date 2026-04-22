# Coletores web

## Como usar este diretório
Aqui ficam os coletores de fallback.

## Regra do projeto
1. CSV primeiro.
2. Web depois.
3. Se o dado importante continuar faltando, bloquear.

## Sugestão prática
Crie um coletor por tipo de dado, e não um coletor para "tudo":
- odds_collector.py
- lineups_collector.py
- injuries_collector.py
- stats_collector.py

## Atenção
Não use scraping livre sem normalização. Sempre devolva os campos no padrão do projeto.
