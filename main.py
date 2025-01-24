import tkinter as tk
from tkinter import ttk
from database import criar_tabelas
from views.turmas_view import TurmasView
from views.alunos_view import AlunosView
from views.visualizar_view import VisualizarView
from views.deletar_view import DeletarView
from views.listas_view import ListasView  # Nova aba

def main():
    # Criar banco de dados e tabelas
    criar_tabelas()

    # Interface gráfica
    root = tk.Tk()
    root.title("Frequency Control")

    # Abas
    abas = ttk.Notebook(root)
    abas.pack(expand=True, fill="both")

    # Adicionar abas
    turmas_view = TurmasView(abas)
    alunos_view = AlunosView(abas)
    visualizar_view = VisualizarView(abas)
    deletar_view = DeletarView(abas)
    listas_view = ListasView(abas)  # Nova aba

    abas.add(turmas_view.frame, text="Turmas")
    abas.add(alunos_view.frame, text="Alunos")
    abas.add(visualizar_view.frame, text="Visualizar")
    abas.add(deletar_view.frame, text="Deletar")
    abas.add(listas_view.frame, text="Listas")  # Nova aba

    root.mainloop()

if __name__ == "__main__":
    main()