import sqlite3

conn = sqlite3.connect('time_futebol.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS jogadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    posicao TEXT,
    gols INTEGER DEFAULT 0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS partidas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    adversario TEXT NOT NULL,
    placar TEXT NOT NULL
)
''')

def adicionar_jogador(nome, idade, posicao):
    cursor.execute('''
    INSERT INTO jogadores (nome, idade, posicao) VALUES (?, ?, ?)
    ''', (nome, idade, posicao))
    conn.commit()

def adicionar_partida(data, adversario, placar):
    cursor.execute('''
    INSERT INTO partidas (data, adversario, placar) VALUES (?, ?, ?)
    ''', (data, adversario, placar))
    conn.commit()

def registrar_gols(jogador_id, gols):
    cursor.execute('''
    UPDATE jogadores SET gols = gols + ? WHERE id = ?
    ''', (gols, jogador_id))
    conn.commit()

def listar_jogadores():
    cursor.execute('SELECT * FROM jogadores')
    return cursor.fetchall()

def listar_partidas():
    cursor.execute('SELECT * FROM partidas')
    return cursor.fetchall()

conn.close()
