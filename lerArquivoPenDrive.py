#código para entrar no pendrive e ler um arquivo txt

import os
from decoder import decodificacao
from resolucao import escrever

def lendoArquivoPendrive(drive_path, filename, ns_value):
    """
    Lê o conteúdo de um arquivo de texto de um pendrive.
    Args:
        drive_path (str): O caminho base para a pasta de trabalho (ex: 'D:/Trabalho').
        filename (str): O nome do arquivo .txt a ser lido (ex: 'TESTE-01.txt').
        ns_value (str): O número formatado do arquivo de teste (ex: '01', '02').

    Return
        str: O conteúdo do arquivo, ou uma mensagem de erro se o arquivo não for encontrado.
    """
    file_path = os.path.join(drive_path, filename)
    instrucoesDecodificadas = [] # Lista para armazenar todas as linhas decodificadas
    
    try:
        if not os.path.exists(file_path):
            return f"Aviso: Arquivo de entrada não encontrado: {file_path}. Pulando para o próximo.\n"
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for linhaNum, linha in enumerate(f, 1):
                instrucao = linha.strip()
                if not instrucao: #ignora linhas vazias
                    continue
                
                mnemonico_decodificado = decodificacao(instrucao)
                instrucoesDecodificadas.append(mnemonico_decodificado)

        #após ler e decodificar as linhas, chamamos a função de escrever
        escrever(instrucoesDecodificadas, ns_value)  
        return f"Decodificação de {filename} concluido"  
    
    except FileNotFoundError:
        return f"Erro: O arquivo {filename} não foi encontrado. Verifique se o pendrive está conectado e o caminho está correto."
    
    except Exception as e:
        return f"Ocorreu um erro ao ler o arquivo {filename}: {e}"

if __name__ == "__main__":
    
    Caminho_pendrive = 'D:/Trabalho'

    for i in range(1,11):
        ns = str(i).zfill(2)
        input_filename = f"TESTE-{ns}.txt"

        result_message = lendoArquivoPendrive(Caminho_pendrive, input_filename, ns)
        print(result_message)
