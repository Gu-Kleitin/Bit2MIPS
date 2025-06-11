#código para entrar no pendrive e ler um arquivo txt

import os
from resolucao import escrever
from decoder import decodificacao

def lendoArquivoPendrive(drive_letter, filename):
    """
    Lê o conteúdo de um arquivo de texto de um pendrive.
    Args:
        drive_letter (str): A letra da unidade do pendrive (ex: 'D:', 'E:').
        filename (str): O nome do arquivo .txt a ser lido.

    Return
        str: O conteúdo do arquivo, ou uma mensagem de erro se o arquivo não for encontrado.
    """
    file_path = os.path.join(drive_letter, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            decodificacao(content, ns)
        return f"Conteúdo do arquivo {file_path}:\n\n{content}"
    
    except FileNotFoundError:
        return f"Erro: O arquivo {file_path} não foi encontrado. Verifique se o pendrive está conectado e o caminho está correto."
    
    except Exception as e:
        return f"Ocorreu um erro ao ler o arquivo: {e}"

if __name__ == "__main__":
    
    n = 0
    ns = ""

    while (n != 10):
        ns=""
        n = n+1
        if(n!=10):
            ns ="0"
            ns = ns + str(n)
        else:
            ns=str(n)
            #O caminho tem que ser alterado caso o caminho não seja o mesmo.
        result = lendoArquivoPendrive('D:\Trabalho', 'TESTE-'+ns+'.txt')
    

