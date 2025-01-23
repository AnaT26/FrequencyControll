import sqlite3
from sqlite3 import Error
#Caminho do Banco de dados
DATABASE_PATH = 'controle_presencas.db'

def conectar():
    """Conecta ao banco de dados e retorna a conexão"""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        print("Conexão com o DB estabelecida")
        return conn
    except Error as e:
        print(f"Erro ao conectar ao DB: {e}")
    return conn

def criar_tabelas():
    """Cria as tabelas no DB caso não existam"""
    conn = conectar()
    if conn:
        try:
            c = conn.cursor()
            #Tabela de turmas
            c.execute('''
                CREATE TABLE IF NOT EXISTS turmas (
                      id INTEGER PRIMARY KEY AUTOINCREMENT
                      nome TEXT NOT NULL
                      )

''')
            #Tabela de alunos
            c.execute('''
                CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_completo TEXT NOT NULL,
                    turma_id INTEGER,
                    FOREIGN KEY (turma_id) REFERENCES turmas(id)
''')
            # Tabela de apelidos
            c.execute('''
                CREATE TABLE IF NOT EXISTS apelidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    apelido TEXT NOT NULL,
                    aluno_id INTEGER,
                    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
                )
            ''')
            # Tabela de presenças
            c.execute('''
                CREATE TABLE IF NOT EXISTS presencas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    aluno_id INTEGER,
                    data DATE,
                    presente BOOLEAN,
                    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
                )
            ''')
            conn.commit()
            print("Tabelas criadas com sucesso!")
        except Error as e:
            print(f"Erro ao crias as tabelas: {e}")
        finally:
            conn.close()

# Verifica se o banco de dados existe e cria as tabelas ao importar o módulo
criar_tabelas()


    
