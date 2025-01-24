import tkinter as tk
from tkinter import ttk, messagebox
from control import adc_aluno, adc_apelido, buscar_apelidos

class AlunosView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Nome Completo:").pack(pady=5)
        self.entrada_nome_completo = tk.Entry(self.frame, width=40)
        self.entrada_nome_completo.pack(pady=5)

        tk.Label(self.frame, text="Turma:").pack(pady=5)
        self.combo_turmas = ttk.Combobox(self.frame, width=37)
        self.combo_turmas.pack(pady=5)

        tk.Label(self.frame, text="Apelido:").pack(pady=5)
        self.entrada_apelido = tk.Entry(self.frame, width=40)
        self.entrada_apelido.pack(pady=5)

        tk.Button(self.frame, text="Adicionar Aluno", command=self.adicionar_aluno).pack(pady=10)
        tk.Button(self.frame, text="Adicionar Apelido", command=self.adicionar_apelido).pack(pady=10)

    def adicionar_aluno(self):
        nome_completo = self.entrada_nome_completo.get()
        turma_id = self.combo_turmas.get().split(":")[0]  # Pega o ID da turma selecionada
        if nome_completo and turma_id:
            aluno_id = adc_aluno(nome_completo, int(turma_id))
            messagebox.showinfo("Sucesso", f"Aluno adicionado com ID: {aluno_id}")
            self.entrada_nome_completo.delete(0, "end")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")

    def adicionar_apelido(self):
        aluno_id = self.entrada_nome_completo.get()  # Aqui você pode ajustar para selecionar o aluno
        apelido = self.entrada_apelido.get()
        if aluno_id and apelido:
            adc_apelido(int(aluno_id), apelido)
            messagebox.showinfo("Sucesso", "Apelido adicionado com sucesso!")
            self.entrada_apelido.delete(0, "end")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")