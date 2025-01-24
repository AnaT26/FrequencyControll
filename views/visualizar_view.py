import tkinter as tk
from tkinter import ttk, messagebox
from control import listar_turmas, listar_alunos_por_turma

class VisualizarView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Lista de turmas
        tk.Label(self.frame, text="Turmas:").pack(pady=5)
        self.lista_turmas = ttk.Combobox(self.frame, width=40)
        self.lista_turmas.pack(pady=5)
        self.lista_turmas.bind("<<ComboboxSelected>>", self.carregar_alunos)  # Atualiza alunos ao selecionar turma

        # Lista de alunos
        tk.Label(self.frame, text="Alunos:").pack(pady=5)
        self.lista_alunos = tk.Listbox(self.frame, width=50, height=10)
        self.lista_alunos.pack(pady=10)

        # Botão para carregar turmas
        tk.Button(self.frame, text="Carregar Turmas", command=self.carregar_turmas).pack(pady=10)

    def carregar_turmas(self):
        """Carrega todas as turmas no Combobox."""
        turmas = listar_turmas()
        if turmas:
            self.lista_turmas['values'] = [f"{turma[0]}: {turma[1]}" for turma in turmas]
            messagebox.showinfo("Sucesso", "Turmas carregadas com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nenhuma turma cadastrada.")
        print("Turmas encontradas (Visualizar):", turmas)  # Debug: Mostra as turmas no terminal

    def carregar_alunos(self, event=None):
        """Carrega os alunos da turma selecionada."""
        turma_selecionada = self.lista_turmas.get()
        if turma_selecionada:
            turma_id = turma_selecionada.split(":")[0]  # Pega o ID da turma
            alunos = listar_alunos_por_turma(int(turma_id))
            self.lista_alunos.delete(0, tk.END)  # Limpa a lista atual
            if alunos:
                for aluno in alunos:
                    self.lista_alunos.insert(tk.END, f"{aluno[1]} ({aluno[2]})")  # Nome e apelido
            else:
                messagebox.showwarning("Aviso", "Nenhum aluno cadastrado nesta turma.")