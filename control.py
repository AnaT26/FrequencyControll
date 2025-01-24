from database import conectar
from models import Turma, Aluno, Apelido, Presenca

def adc_turma(nome):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO  turmas (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()

def adc_aluno(nome_completo, turma_id):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO alunos (nome_completo, turma_id) VALUES (?, ?)",
              (nome_completo, turma_id))
    conn.commit()
    conn.close()

def buscar_apelidos(aluno_id):
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT apelido FROM apelidos WHERE aluno_id = ?", (aluno_id,))
    apelidos = [row[0] for row in c.fetchall()]  # Lista de apelidos
    conn.close()
    return apelidos

def registrar_presenca(aluno_id, data, presente):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO presencas (aluno_id, data, presente) VALUES (?, ?, ?)",
              (aluno_id, data, presente))
    conn.commit()
    conn.close() 

