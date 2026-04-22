CREATE TABLE IF NOT EXISTS cofre_geral (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    projeto TEXT NOT NULL,
    banca_inicial REAL NOT NULL,
    banca_atual REAL NOT NULL,
    meta_final REAL NOT NULL,
    n_entradas_max INTEGER NOT NULL,
    entrada_atual INTEGER NOT NULL,
    entradas_restantes INTEGER NOT NULL,
    odd_media_inicial REAL NOT NULL,
    odd_media_restante REAL NOT NULL,
    status_trajetoria TEXT NOT NULL,
    stake_padrao REAL NOT NULL,
    caixa_realizado REAL NOT NULL,
    bilhetes_em_aberto INTEGER NOT NULL DEFAULT 0,
    jogos_em_aberto INTEGER NOT NULL DEFAULT 0,
    metodos_ativos_por_liga TEXT,
    metodos_sombra_por_liga TEXT,
    metodos_bloqueados_por_liga TEXT,
    ultima_atualizacao TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cofre_entradas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    liga TEXT NOT NULL,
    jogo TEXT NOT NULL,
    metodo TEXT NOT NULL,
    mercado TEXT NOT NULL,
    odd_publica REAL,
    odd_justa REAL,
    edge REAL,
    stake REAL,
    status_pre TEXT,
    contexto_jogo TEXT,
    tipo_bilhete TEXT,
    resultado_final TEXT,
    lucro_prejuizo REAL,
    observacao_curta TEXT
);

CREATE TABLE IF NOT EXISTS cofre_posjogo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    jogo TEXT NOT NULL,
    metodo TEXT NOT NULL,
    mercado TEXT NOT NULL,
    resultado_metodo TEXT,
    resultado_financeiro REAL,
    motivo_principal TEXT,
    motivo_secundario TEXT,
    leitura_estrutural TEXT,
    leitura_preco TEXT,
    falha_contexto TEXT,
    falha_escalacao TEXT,
    falha_rotacao TEXT,
    falha_importancia TEXT,
    variancia_pura TEXT,
    ajuste_futuro TEXT,
    status_metodo_apos_jogo TEXT
);

CREATE TABLE IF NOT EXISTS relatorio_metodos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liga TEXT NOT NULL,
    metodo TEXT NOT NULL,
    entradas INTEGER NOT NULL DEFAULT 0,
    greens INTEGER NOT NULL DEFAULT 0,
    reds INTEGER NOT NULL DEFAULT 0,
    winrate REAL,
    roi REAL,
    yield REAL,
    drawdown_maximo REAL,
    bad_run INTEGER,
    green_run INTEGER,
    lucro_acumulado REAL,
    ultimos_5_jogos TEXT,
    status_atual TEXT
);
