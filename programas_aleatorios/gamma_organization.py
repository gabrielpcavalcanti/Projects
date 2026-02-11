import os
import csv
from tkinter import filedialog

def choose_directory():

    try:
        path_directory = filedialog.askdirectory()
        
        return path_directory
    
    except OSError:
        print("Select a file")

gamma_folder_path = choose_directory()

os.chdir(gamma_folder_path)

base_string = "spectrum_256_id_{}.spc"
lista_strings = []

for i in range(15, 1225):
    nova_string = base_string.format(i)
    lista_strings.append(nova_string)

for i in range(1293, 1450):
    nova_string = base_string.format(i)
    lista_strings.append(nova_string)

for i in range(1551, 2395):
    nova_string = base_string.format(i)
    lista_strings.append(nova_string)


for i in os.listdir():

    caminho_do_arquivo = f"{os.getcwd()}\\{i}"

    if i in lista_strings:
        try:
            os.remove(caminho_do_arquivo)
            #print(f"O arquivo '{caminho_do_arquivo}' foi deletado com sucesso.")
        except FileNotFoundError:
            print(f"O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar deletar o arquivo: {e}")
    else:
        continue

# Nome do arquivo de entrada e saída
arquivo_entrada = f"{gamma_folder_path}\\assay_modificado2.csv"
arquivo_saida = f"{gamma_folder_path}\\assay_modificado3.csv"

separador_personalizado = ';'  # Altere para o separador desejado
inicio = 1551
fim = 2395

numeros = list(range(inicio, fim))  # Exemplo: números de 1 a 10
strings = list(map(str, numeros))

indice_coluna_verificacao = 0  # Índice baseado em zero da coluna a ser verificada
valores_indesejados = set(strings)

linhas = []

with open(arquivo_entrada, "r", newline="") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=separador_personalizado)
    for linha in leitor_csv:
        if linha[indice_coluna_verificacao] not in valores_indesejados:
            linhas.append(linha)

with open(arquivo_saida, "w", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=separador_personalizado)
    escritor_csv.writerows(linhas)

    