import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Função para salvar dados inseridos pelo usuário em um arquivo CSV
def salvar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    genero = entry_genero.get()

    # Verificar se todos os campos foram preenchidos
    if nome == '' or idade == '' or genero == '':
        messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')
        return
    
    # Adicionar dados do visitante ao DataFrame
    novo_registro = pd.DataFrame({
        'Nome': [nome],
        'Idade': [idade],
        'Gênero': [genero]
    })

    # Verificar se o arquivo já existe ou criar um novo
    try:
        dados = pd.read_csv('Dados_Visitantes.csv')
        dados = pd.concat([dados, novo_registro], ignore_index=True)
    except FileNotFoundError:
        dados = novo_registro
    
    # Salvar dados no arquivo CSV
    dados.to_csv('Dados_Visitantes.csv', index=False)
    messagebox.showinfo('Sucesso', 'Dados salvos com sucesso.')

# Função para gerar visualização dos dados
def visualizar_dados():
    try:
        # Carregar dados do arquivo CSV
        dados = pd.read_csv('Dados_Visitantes.csv')

        # Gráfico de pizza para proporção de gênero
        plt.figure(figsize=(6, 6))
        dados['Gênero'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
        plt.title('Proporção de Gênero dos Visitantes')
        plt.ylabel('')
        plt.show()
    except FileNotFoundError:
        messagebox.showerror('Erro', 'Nenhum dado de visitantes encontrado.')

# Função principal da aplicação
def main():
    # Configuração da janela principal
    root = tk.Tk()
    root.title('Cadastro de Visitantes')

    # Criar campos de entrada
    tk.Label(root, text='Nome:').grid(row=0, column=0, padx=10, pady=5)
    tk.Label(root, text='Idade:').grid(row=1, column=0, padx=10, pady=5)
    tk.Label(root, text='Gênero:').grid(row=2, column=0, padx=10, pady=5)

    global entry_nome, entry_idade, entry_genero
    entry_nome = tk.Entry(root, width=30)
    entry_idade = tk.Entry(root, width=30)
    entry_genero = tk.Entry(root, width=30)

    entry_nome.grid(row=0, column=1, padx=10, pady=5)
    entry_idade.grid(row=1, column=1, padx=10, pady=5)
    entry_genero.grid(row=2, column=1, padx=10, pady=5)

    # Botões para salvar e visualizar dados
    tk.Button(root, text='Salvar', command=salvar_dados).grid(row=3, column=0, padx=10, pady=10)
    tk.Button(root, text='Visualizar Dados', command=visualizar_dados).grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
