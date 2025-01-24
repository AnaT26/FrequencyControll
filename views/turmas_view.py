import tkinter as tk
from tkinter import messagebox
from control import adicionar_turma

class TurmasView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Nome da Turma:").pack(pady=5)
        self.entrada_turma = tk.Entry(self.frame, width=40)
        self.entrada_turma.pack(pady=5)

        tk.Button(self.frame, text="Adicionar Turma", command=self.adicionar_turma).pack(pady=10)

    def adicionar_turma(self):
        nome_turma = self.entrada_turma.get()
        if nome_turma:
            adicionar_turma(nome_turma)
            messagebox.showinfo("Sucesso", "Turma adicionada com sucesso!")
            self.entrada_turma.delete(0, "end")
        else:
            messagebox.showwarning("Erro", "Digite o nome da turma!")