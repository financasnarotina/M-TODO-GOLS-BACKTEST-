# Arquitetura resumida

## Camadas
- Telegram = canal
- FastAPI = backend
- SQLite = Cofre Mestre
- methods/*.json = fonte da verdade dos métodos
- engine/ = regras do projeto
- collectors/ = coleta web de fallback
- data_raw/ = CSVs e planilhas

## Regra de ouro
O prompt explica. O código decide.
