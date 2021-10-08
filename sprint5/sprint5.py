import os
import glob
import csv

def todos_arquivos_txt():
    pass

def todos_arquivos_csv():
    looking_for = '**/*.csv'
    matched = glob.glob(looking_for, recursive=True)
    return matched

def carregar_arquivo_txt_para_lista(nome_arquivo):
    lista = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.replace('\n','')
            linha = linha.split('\t')
            linha = linha[0:-1]
            lista.append(tuple(linha))
    return lista

def carregar_arquivo_csv_para_lista(nome_arquivo):
    pass

def buscar_trecho_nome(lista, trecho_nome):
    pass

def buscar_nome(lista, trecho_nome):
    pass

def buscar_email(lista, email):
    pass

def buscar_cpf(lista, cpf):
    pass

def buscar_trecho_cpf(lista, trecho_cpf):
    pass

def buscar_dominio_email(lista, dominio):
    pass

def buscar_trecho_nome_email(lista, trecho_nome, email):
    pass

def gravar_lista_para_arquivo_csv(lista, nome_arquivo):
    with open(nome_arquivo,'w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerow(['Nome', 'CPF', 'E-mail'])
        wr.writerows(lista)

'''
if __name__ == '__main__':
    root_dir = os.getcwd()
    new_dir = os.getcwd() + '/arquivos/'
    os.chdir(new_dir)
    ocorrencias = []
    for arquivo in todos_arquivos_txt():
        ocorrencias += carregar_arquivo_txt_para_lista(arquivo) 
    for arquivo in todos_arquivos_csv():
        ocorrencias += carregar_arquivo_csv_para_lista(arquivo)
    dominio_ig_1 = buscar_dominio_email(ocorrencias, 'ig.com.br')

    os.chdir(root_dir)    
    new_dir = os.getcwd() + '/arquivos/diretorio6'
    os.chdir(new_dir)
    ocorrencias = []
    for arquivo in todos_arquivos_txt():
        ocorrencias += carregar_arquivo_txt_para_lista(arquivo) 
    for arquivo in todos_arquivos_csv():
        ocorrencias += carregar_arquivo_csv_para_lista(arquivo)
    dominio_ig_2 = buscar_dominio_email(ocorrencias, 'ig.com.br')
    
    # NESTE TRECHO, ALTERAR O DIRETÓRIO DE TRABALHO
    # Os arquivos gerados com as funções abaixo devem gerar arquivos
    # dentro do diretório relatorio. Este diretório deve ser criado via script também
    
    gravar_lista_para_arquivo_csv(dominio_ig_1, 'dominio_ig_all.csv')
    gravar_lista_para_arquivo_csv(dominio_ig_2, 'dominio_ig_dir6.csv')
'''