from tkinter import filedialog
import os
import csv


def choose_directory():

    try:

        path_directory = filedialog.askdirectory()
        
        return path_directory
    
    except OSError:

        print("Select a file")


def create_list_del_values(start, stop):
    
    numeros = list(range(start, stop))  
    del_values = set(map(str, numeros))

    return del_values


def create_list_string(start, stop, name_file):
    
    base_string = name_file
    list_strings = []

    for i in range(start, stop):

        nova_string = base_string.format(i)
        list_strings.append(nova_string)
    
    return list_strings


def remove_file(start, stop, name_file):

    for i in os.listdir():

        caminho_do_arquivo = f"{os.getcwd()}\\{i}"
        list_string = create_list_string(start, stop, name_file)

        if i in list_string:

            try:

                os.remove(caminho_do_arquivo)
                #print(f"O arquivo '{caminho_do_arquivo}' foi deletado com sucesso.")

            except FileNotFoundError:

                print(f"O arquivo '{caminho_do_arquivo}' não foi encontrado.")

            except Exception as e:

                print(f"Ocorreu um erro ao tentar deletar o arquivo: {e}")

        else:

            continue


def remove_lines(start, stop, assay_gamma_path, assay_modify_gamma_path):

    lines = []

    del_values = create_list_del_values(start, stop)

    with open(assay_gamma_path, "r", newline="") as arquivo_csv:

        leitor_csv = csv.reader(arquivo_csv, delimiter=';')

        for linha in leitor_csv:

            if linha[0] not in del_values:

                lines.append(linha)

    with open(assay_modify_gamma_path, "w", newline="") as arquivo_csv:
        
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')
        escritor_csv.writerows(lines)


def main():

    while True:

        gamma_folder_path = choose_directory()

        os.chdir(gamma_folder_path)

        assay_gamma_path = f"{gamma_folder_path}\\assay.csv"
        assay_modify_gamma_path = f"{gamma_folder_path}\\assay.csv"

        start = 1382
        stop = 2395

        ans_file = input("Would you like to remove the files: ")

        if ans_file.lower() == 'y':

            ans_type = input("type 256 or 1024: ")
            name_file = f"spectrum_{ans_type}_id_{{}}.spc"

            remove_file(start, stop, name_file)
        
        ans_lines = input("Would you like to remove the lines: ")

        if ans_lines.lower() == 'y':

            remove_lines(start, stop, assay_gamma_path, assay_modify_gamma_path)
            break

        else:

            break
            
main()
