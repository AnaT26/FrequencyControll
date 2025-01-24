import tkinter as tk
from tkinter import ttk, messagebox
from control import deletar_turma, deletar_aluno, deletar_apelido, listar_turmas, listar_alunos_por_turma, listar_apelidos_por_aluno

class DeletarView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Combobox para selecionar a turma
        tk.Label(self.frame, text="Selecione a turma:").pack(pady=5)
        self.combo_turmas = ttk.Combobox(self.frame, width=40)
        self.combo_turmas.pack(pady=5)
        self.combo_turmas.bind("<<ComboboxSelected>>", self.carregar_alunos)

        # Combobox para selecionar o aluno
        tk.Label(self.frame, text="Selecione o aluno:").pack(pady=5)
        self.combo_alunos = ttk.Combobox(self.frame, width=40)
        self.combo_alunos.pack(pady=5)
        self.combo_alunos.bind("<<ComboboxSelected>>", self.carregar_apelidos)

        # Combobox para selecionar o apelido
        tk.Label(self.frame, text="Selecione o apelido:").pack(pady=5)
        self.combo_apelidos = ttk.Combobox(self.frame, width=40)
        self.combo_apelidos.pack(pady=5)

        # Botões
        tk.Button(self.frame, text="Deletar Turma", command=self.deletar_turma).pack(pady=10)
        tk.Button(self.frame, text="Deletar Aluno", command=self.deletar_aluno).pack(pady=10)
        tk.Button(self.frame, text="Deletar Apelido", command=self.deletar_apelido).pack(pady=10)

        # Carregar turmas ao inicializar a aba
        self.carregar_turmas()

    def carregar_turmas(self):
        """Carrega as turmas no Combobox."""
        turmas = listar_turmas()
        if turmas:
            self.combo_turmas['values'] = [f"{turma[0]}: {turma[1]}" for turma in turmas]
        else:
            messagebox.showwarning("Aviso", "Nenhuma turma cadastrada.")

    def carregar_alunos(self, event=None):
        """Carrega os alunos da turma selecionada."""
        turma_selecionada = self.combo_turmas.get()
        if turma_selecionada:
            turma_id = turma_selecionada.split(":")[0]  # Pega o ID da turma
            alunos = listar_alunos_por_turma(int(turma_id))
            if alunos:
                self.combo_alunos['values'] = [f"{aluno[0]}: {aluno[1]}" for aluno in alunos]
            else:
                messagebox.showwarning("Aviso", "Nenhum aluno cadastrado nesta turma.")
        else:
            messagebox.showwarning("Aviso", "Selecione uma turma primeiro.")

    def carregar_apelidos(self, event=None):
        """Carrega os apelidos do aluno selecionado."""
        aluno_selecionado = self.combo_alunos.get()
        if aluno_selecionado:
            aluno_id = aluno_selecionado.split(":")[0]  # Pega o ID do aluno
            apelidos = listar_apelidos_por_aluno(int(aluno_id))
            if apelidos:
                self.combo_apelidos['values'] = [f"{apelido[0]}: {apelido[1]}" for apelido in apelidos]
            else:
                messagebox.showwarning("Aviso", "Nenhum apelido cadastrado para este aluno.")
        else:
            messagebox.showwarning("Aviso", "Selecione um aluno primeiro.")

    def deletar_turma(self):
        """Deleta a turma selecionada."""
        turma_selecionada = self.combo_turmas.get()
        if turma_selecionada:
            turma_id = turma_selecionada.split(":")[0]  # Pega o ID da turma
            deletar_turma(int(turma_id))
            messagebox.showinfo("Sucesso", "Turma deletada com sucesso!")
            self.carregar_turmas()  # Atualiza a lista de turmas
        else:
            messagebox.showwarning("Erro", "Selecione uma turma primeiro.")

    def deletar_aluno(self):
        """Deleta o aluno selecionado."""
        aluno_selecionado = self.combo_alunos.get()
        if aluno_selecionado:
            aluno_id = aluno_selecionado.split(":")[0]  # Pega o ID do aluno
            deletar_aluno(int(aluno_id))
            messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
            self.carregar_alunos()  # Atualiza a lista de alunos
        else:
            messagebox.showwarning("Erro", "Selecione um aluno primeiro.")

    def deletar_apelido(self):
        """Deleta o apelido selecionado."""
        apelido_selecionado = self.combo_apelidos.get()
        if apelido_selecionado:
            apelido_id = apelido_selecionado.split(":")[0]  # Pega o ID do apelido
            deletar_apelido(int(apelido_id))
            messagebox.showinfo("Sucesso", "Apelido deletado com sucesso!")
            self.carregar_apelidos()  # Atualiza a lista de apelidos
        else:
            messagebox.showwarning("Erro", "Selecione um apelido primeiro.")