class Turma:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Aluno:
    def __init__(self, id, nome_completo, turma_id):
        self.id = id 
        self.nome_completo = nome_completo
        self.turma_id = turma_id

class Apelido:
    def __init__(self, id, apelido, aluno_id):
        self.id = id 
        self.apelido = apelido
        self.aluno_id =aluno_id

class Presenca:
    def __init__(self, id, aluno_id, data, presente):
        self.id = id 
        self.aluno_id = aluno_id
        self.data = data
        self.presente = presente
        
        
        