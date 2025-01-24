from database import conectar
from sqlite3 import Error

def adc_turma(nome):
    """Adiciona uma nova turma."""
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO turmas (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()

def adc_aluno(nome_completo, turma_id):
    """Adiciona um novo aluno."""
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO alunos (nome_completo, turma_id) VALUES (?, ?)",
              (nome_completo, turma_id))
    aluno_id = c.lastrowid  # Pega o ID do aluno recém-inserido
    conn.commit()
    conn.close()
    return aluno_id

def adc_apelido(aluno_id, apelido):
    """Adiciona um apelido a um aluno."""
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO apelidos (apelido, aluno_id) VALUES (?, ?)",
              (apelido, aluno_id))
    conn.commit()
    conn.close()

def listar_turmas():
    """Retorna uma lista de todas as turmas."""
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT id, nome FROM turmas")
    turmas = c.fetchall()  # Retorna uma lista de tuplas (id, nome)
    conn.close()
    return turmas

def listar_alunos_por_turma(turma_id):
    """Retorna uma lista de alunos de uma turma específica."""
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        SELECT id, nome_completo, apelido 
        FROM alunos 
        WHERE turma_id = ?
    ''', (turma_id,))
    alunos = c.fetchall()  # Retorna uma lista de tuplas (id, nome_completo, apelido)
    conn.close()
    return alunos

def listar_apelidos_por_aluno(aluno_id):
    """Retorna uma lista de apelidos de um aluno específico."""
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        SELECT id, apelido 
        FROM apelidos 
        WHERE aluno_id = ?
    ''', (aluno_id,))
    apelidos = c.fetchall()  # Retorna uma lista de tuplas (id, apelido)
    conn.close()
    return apelidos

def registrar_presenca(aluno_id, data, presente):
    """Registra a presença de um aluno."""
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO presencas (aluno_id, data, presente) VALUES (?, ?, ?)",
              (aluno_id, data, presente))
    conn.commit()
    conn.close()

def listar_presencas():
    """Retorna uma lista de alunos com suas presenças."""
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        SELECT a.nome_completo, p.presente
        FROM alunos a
        LEFT JOIN presencas p ON a.id = p.aluno_id
        ORDER BY a.nome_completo
    ''')
    presencas = c.fetchall()  # Retorna uma lista de tuplas (nome_completo, presente)
    conn.close()
    return presencas

def gerar_lista_completa():
    """Gera a lista completa no formato 'Nome Completo: P/F'."""
    presencas = listar_presencas()
    lista_completa = []
    for nome, presente in presencas:
        status = "P" if presente else "F"
        lista_completa.append(f"{nome}: {status}")
    return lista_completa

def gerar_lista_simplificada():
    """Gera a lista simplificada com apenas 'P' ou 'F'."""
    presencas = listar_presencas()
    lista_simplificada = []
    for _, presente in presencas:
        status = "P" if presente else "F"
        lista_simplificada.append(status)
    return lista_simplificada