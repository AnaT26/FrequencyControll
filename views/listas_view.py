import tkinter as tk
from tkinter import ttk, messagebox
from control import gerar_lista_completa, gerar_lista_simplificada

class ListasView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Lista Completa
        tk.Label(self.frame, text="Lista Completa:").pack(pady=5)
        self.lista_completa = tk.Text(self.frame, width=50, height=10)
        self.lista_completa.pack(pady=5)

        # Botão para gerar a lista completa
        tk.Button(self.frame, text="Gerar Lista Completa", command=self.gerar_completa).pack(pady=10)

        # Lista Simplificada
        tk.Label(self.frame, text="Lista Simplificada:").pack(pady=5)
        self.lista_simplificada = tk.Text(self.frame, width=10, height=10)
        self.lista_simplificada.pack(pady=5)

        # Botão para gerar a lista simplificada
        tk.Button(self.frame, text="Gerar Lista Simplificada", command=self.gerar_simplificada).pack(pady=10)

    def gerar_completa(self):
        """Gera e exibe a lista completa."""
        lista = gerar_lista_completa()
        self.lista_completa.delete(1.0, tk.END)  # Limpa o conteúdo anterior
        self.lista_completa.insert(tk.END, "\n".join(lista))  # Insere a lista completa
        messagebox.showinfo("Sucesso", "Lista completa gerada com sucesso!")

    def gerar_simplificada(self):
        """Gera e exibe a lista simplificada."""
        lista = gerar_lista_simplificada()
        self.lista_simplificada.delete(1.0, tk.END)  # Limpa o conteúdo anterior
        self.lista_simplificada.insert(tk.END, "\n".join(lista))  # Insere a lista simplificada
        messagebox.showinfo("Sucesso", "Lista simplificada gerada com sucesso!")