import tkinter as tk
from tkinter import messagebox

# Exemplo de listas
nomes_completos = ["Anderson Leonardo Luiz", "Arlelto Carvalho do Nascimento", "Charles Pereira Bento", "Cleber Ferreira de Sousa", "Elier Corrêa Bernal", "Eudes Bentes Bulhosa", "Felipe Fernandes Machado", "Francisco Tiago Gomes Barbosa", "Helton Santana da Silva", "Henrique Ricardo Dantas de Souza", "Italo de Almeida Lobato", "Jho Anderson Monteiro Ferreira", "Jorge Ricardo dos Passos Massen", "José Adailton Neves de Oliveira Filho", "José Alyson Cordeiro da Silva", "Kaio Givisiez dos Reis", "Laudir Freire da Silva", "Luis Henrique Barbosa", "Marcelo Augusto Dutra Castro", "Marcos Jhones de Almeida Curico", "Mauricio Xavier Barreto", "Nilmar Oliveira da Silva", "Rafael de Jesus Ventura", "Roberto Faria Neto", "Wallace Silva da Costa"]
apelidos_presenca = ["adailton neves", "Anderson Luiz", "Arlelto carvalho", "Charles Bento", "Cleber Sousa", "Elioenai Santos", "Eudes Bentes", "Felipe Fernandes Machado", "Helton Santana", "Ítalo Lobato", "JHO ANDERSON", "Jorge Massen Passos", "jose alyson", "Kaio Givisiez", "Kaio Givisiez", "Luis Henrique", "Marcelo Castro", "Marcos Jhones", "MAURICIO BARRETO", "Nilmar Oliveira da Silva", "Nilmar Oliveira", "Rafael de Jesus Ventura", "Ricardo Dantas", "Roberto De Faria neto", "Tiago Gomes", "Wallace Silva"]

# Dicionário para mapear nome completo aos apelidos
mapa_apelidos = {
    "Anderson Leonardo Luiz": ["Anderson Luiz"],
    "Arlelto Carvalho do Nascimento": ["Arlelto carvalho"],
    "Charles Pereira Bento": ["Charles Bento"],
    "Cleber Ferreira de Sousa": ["Cleber Sousa"],
    "Elier Corrêa Bernal": [],
    "Eudes Bentes Bulhosa": ["Eudes Bentes"],
    "Felipe Fernandes Machado": ["Felipe Fernandes Machado"],
    "Francisco Tiago Gomes Barbosa": ["Tiago Gomes"],
    "Helton Santana da Silva": ["Helton Santana"],
    "Henrique Ricardo Dantas de Souza": ["Ricardo Dantas"],
    "Italo de Almeida Lobato": ["Ítalo Lobato"],
    "Jho Anderson Monteiro Ferreira": ["JHO ANDERSON"],
    "Jorge Ricardo dos Passos Massen": ["Jorge Massen Passos"],
    "José Adailton Neves de Oliveira Filho": ["adailton neves"],
    "José Alyson Cordeiro da Silva": ["jose alyson"],
    "Kaio Givisiez dos Reis": ["Kaio Givisiez"],
    "Laudir Freire da Silva": [],
    "Luis Henrique Barbosa": ["Luis Henrique"],
    "Marcelo Augusto Dutra Castro": ["Marcelo Castro"],
    "Marcos Jhones de Almeida Curico": ["Marcos Jhones"],
    "Mauricio Xavier Barreto": ["MAURICIO BARRETO"],
    "Nilmar Oliveira da Silva": ["Nilmar Oliveira da Silva", "Nilmar Oliveira"],
    "Rafael de Jesus Ventura": ["Rafael de Jesus Ventura"],
    "Roberto Faria Neto": ["Roberto De Faria neto"],
    "Wallace Silva da Costa": ["Wallace Silva"]
}

# Função para comparar listas e gerar as listas de presença
def comparar_listas():
    presentes_manha = presencia_manha_text.get("1.0", "end-1c").strip().split("\n")  # Entrada de presença da manhã
    presentes_manha = [p.strip() for p in presentes_manha if p.strip()]  # Limpar espaços e remover linhas vazias

    presentes_tarde = presencia_tarde_text.get("1.0", "end-1c").strip().split("\n")  # Entrada de presença da tarde
    presentes_tarde = [p.strip() for p in presentes_tarde if p.strip()]  # Limpar espaços e remover linhas vazias

    # Inicializando as listas
    lista_completa = []
    lista_planilha = []

    # Verifica se todos os presentes estão na lista de alunos
    for nome_completo in nomes_completos:
        # Obter a lista de apelidos do nome completo (ou uma lista vazia se não encontrado)
        apelidos = mapa_apelidos.get(nome_completo, [])
        
        # Verificar se algum dos apelidos está na lista de presentes da manhã ou da tarde
        if any(apelido in presentes_manha or apelido in presentes_tarde for apelido in apelidos):
            lista_completa.append(f"{nome_completo}: P")  # Presente
            lista_planilha.append("P")
        else:
            lista_completa.append(f"{nome_completo}: F")  # Falta
            lista_planilha.append("F")

    # Exibe o resultado completo na caixa de texto
    resultados_text.delete(1.0, "end")  # Limpa a caixa de texto antes de adicionar os novos resultados
    resultados_text.insert("end", "\n".join(lista_completa))  # Insere a lista completa com nomes

    # Exibe a lista apenas com P e F na caixa de texto
    resultados_planilha.delete(1.0, "end")  # Limpa a caixa de texto
    resultados_planilha.insert("end", "\n".join(lista_planilha))  # Insere a lista de P's e F's na caixa de texto

    # Retorna a lista para ser copiada na planilha
    return lista_planilha

# Interface Tkinter
root = tk.Tk()
root.title("Comparar Lista de Alunos")

# Entrada para lista de presença da manhã
tk.Label(root, text="Digite os apelidos presentes pela manhã (separados por linha):").pack(pady=5)
presencia_manha_text = tk.Text(root, height=10, width=60)
presencia_manha_text.pack(pady=5)

# Entrada para lista de presença da tarde
tk.Label(root, text="Digite os apelidos presentes pela tarde (separados por linha):").pack(pady=5)
presencia_tarde_text = tk.Text(root, height=10, width=60)
presencia_tarde_text.pack(pady=5)

# Caixa de texto para mostrar os resultados com os nomes completos
tk.Label(root, text="Resultados (com nomes e P/F):").pack(pady=5)
resultados_text = tk.Text(root, height=10, width=60)
resultados_text.pack(pady=5)

# Caixa de texto para mostrar a lista apenas com P e F
tk.Label(root, text="Resultados (somente P/F):").pack(pady=5)
resultados_planilha = tk.Text(root, height=10, width=60)
resultados_planilha.pack(pady=5)

# Função para copiar para a área de transferência
def copiar_para_planilha():
    lista_planilha = comparar_listas()
    lista_planilha_str = "\n".join(lista_planilha)  # Converter lista para string com uma linha por "P" ou "F"
    root.clipboard_clear()  # Limpar área de transferência
    root.clipboard_append(lista_planilha_str)  # Adicionar nova lista
    messagebox.showinfo("Resultado", "Lista copiada para a área de transferência!")

# Função para limpar os campos de texto
def limpar_campos():
    presencia_manha_text.delete(1.0, "end")
    presencia_tarde_text.delete(1.0, "end")
    resultados_text.delete(1.0, "end")
    resultados_planilha.delete(1.0, "end")

# Frame para os botões
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Botão para comparar as listas
compare_button = tk.Button(button_frame, text="Comparar e Copiar para Planilha", command=copiar_para_planilha)
compare_button.pack(side="left", padx=5)

# Botão para limpar os campos
clear_button = tk.Button(button_frame, text="Limpar Tudo", command=limpar_campos)
clear_button.pack(side="left", padx=5)

root.mainloop()