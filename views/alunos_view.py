import tkinter as tk
from tkinter import ttk, messagebox
from control import adc_aluno, adc_apelido, listar_turmas  # Importações atualizadas

class AlunosView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Campo para nome completo
        tk.Label(self.frame, text="Nome Completo:").pack(pady=5)
        self.entrada_nome_completo = tk.Entry(self.frame, width=40)
        self.entrada_nome_completo.pack(pady=5)

        # Combobox para selecionar a turma
        tk.Label(self.frame, text="Turma:").pack(pady=5)
        self.combo_turmas = ttk.Combobox(self.frame, width=37)
        self.combo_turmas.pack(pady=5)

        # Carregar turmas ao inicializar a aba
        self.carregar_turmas()

        # Campo para apelido
        tk.Label(self.frame, text="Apelido:").pack(pady=5)
        self.entrada_apelido = tk.Entry(self.frame, width=40)
        self.entrada_apelido.pack(pady=5)

        # Botões
        tk.Button(self.frame, text="Adicionar Aluno", command=self.adc_aluno).pack(pady=10)
        tk.Button(self.frame, text="Adicionar Apelido", command=self.adc_apelido).pack(pady=10)

    def carregar_turmas(self):
        """Carrega todas as turmas no Combobox."""
        turmas = listar_turmas()
        if turmas:
            self.combo_turmas['values'] = [f"{turma[0]}: {turma[1]}" for turma in turmas]
            messagebox.showinfo("Sucesso", "Turmas carregadas com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nenhuma turma cadastrada.")
        print("Turmas encontradas (Alunos):", turmas)  # Debug: Mostra as turmas no terminal

    def adc_aluno(self):
        """Adiciona um novo aluno."""
        nome_completo = self.entrada_nome_completo.get()
        turma_id = self.combo_turmas.get().split(":")[0]  # Pega o ID da turma
        if nome_completo and turma_id:
            aluno_id = adc_aluno(nome_completo, int(turma_id))
            messagebox.showinfo("Sucesso", f"Aluno adicionado com ID: {aluno_id}")
            self.entrada_nome_completo.delete(0, "end")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")

    def adc_apelido(self):
        """Adiciona um apelido a um aluno existente."""
        aluno_id = self.entrada_nome_completo.get()  # Aqui você pode ajustar para selecionar o aluno
        apelido = self.entrada_apelido.get()
        if aluno_id and apelido:
            adc_apelido(int(aluno_id), apelido)
            messagebox.showinfo("Sucesso", "Apelido adicionado com sucesso!")
            self.entrada_apelido.delete(0, "end")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")