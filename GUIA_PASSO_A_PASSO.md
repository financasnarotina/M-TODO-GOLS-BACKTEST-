# GUIA PASSO A PASSO - versão traduzida e sem enrolação

## 1) O que você vai fazer
Você vai criar um bot no Telegram, rodar este projeto no seu computador e deixar o bot conversar com o backend local.

## 2) O que instalar
Instale:
- Python 3.11 ou 3.12
- VS Code
- Git (opcional, mas recomendado)

## 3) Como criar o bot no Telegram
1. Abra o Telegram.
2. Procure por **BotFather**.
3. Digite `/newbot`.
4. Escolha um nome.
5. Escolha um username terminado em `bot`.
6. Copie o token que ele te entregar.
7. Abra o arquivo `.env` e cole o token em `TELEGRAM_BOT_TOKEN`.

## 4) Como rodar localmente
### Windows
- Dê duplo clique em `start_local.bat`
ou rode no terminal:
- `python -m venv .venv`
- `.venv\Scripts\activate`
- `pip install -r requirements.txt`
- `copy .env.example .env`
- editar `.env`
- `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

### Linux/macOS
- `bash start_local.sh`

## 5) Onde colocar seus CSVs
Coloque seus arquivos em `data_raw/`.

## 6) O que o sistema deve receber
### Etapa 0
- banca inicial
- meta final
- n entradas max
- nome do projeto
- casa de aposta
- stake real padrão

### Grade
Pode vir em texto. O ideal é um formato simples com uma linha por jogo:
- `Ligue 1 | PSG x Marseille`
- `Premier League | Arsenal x Chelsea`

## 7) O que o sistema faz
1. Lê a Etapa 0.
2. Calcula o bloco financeiro.
3. Consulta o Cofre Mestre.
4. Identifica a liga.
5. Carrega só os métodos oficiais daquela liga.
6. Busca dados no CSV.
7. Se faltar dado atual, tenta coleta web.
8. Se o dado importante continuar faltando, bloqueia.
9. Testa critério por critério.
10. Calcula odd justa.
11. Compara com odd pública.
12. Verifica contexto.
13. Verifica trajetória financeira.
14. Atualiza o Cofre Mestre.
15. Entrega a resposta no formato fixo.

## 8) O que você NÃO deve fazer no começo
- não usar WhatsApp logo de cara;
- não tentar subir tudo em nuvem antes de funcionar localmente;
- não tentar ligar todos os coletores web ao mesmo tempo;
- não usar métodos sombra para autoaprovação.

## 9) O que ainda precisa de ajuste manual
### Coletores web
Você vai precisar decidir quais sites usar para:
- odds;
- escalações e ausências;
- métricas adicionais.

O pacote já deixa isso separado em `app/collectors/`, mas você precisa escolher as fontes finais.

## 10) Regra mais importante
O bot não pode "achar" nada.
Se faltar dado importante, ele bloqueia. Não inventa.
