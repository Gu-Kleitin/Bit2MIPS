import os

def lendoArquivoPendrive(drive_letter, filename):
    """
    Lê o conteúdo de um arquivo de texto de um pendrive.
    Args:
        drive_letter (str): A letra da unidade do pendrive (ex: 'D:', 'E:').
        filename (str): O nome do arquivo .txt a ser lido.

    Returns:
        str: O conteúdo do arquivo, ou uma mensagem de erro se o arquivo não for encontrado.
    """
    file_path = os.path.join(drive_letter, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"Conteúdo do arquivo {file_path}:\n\n{content}"
    except FileNotFoundError:
        return f"Erro: O arquivo {file_path} não foi encontrado. Verifique se o pendrive está conectado e o caminho está correto."
    except Exception as e:
        return f"Ocorreu um erro ao ler o arquivo: {e}"

if __name__ == "__main__":
    # Exemplo de uso:
    # No seu computador Windows, substitua 'D:' pela letra da unidade do seu pendrive.
    # E 'meu_arquivo.txt' pelo nome do arquivo que você quer ler. 
    # O que está dentro do parêntese tem que ser alterado caso mude o nome do arquivo
    # result = lendoArquivoPendrive('D:', 'TESTE-01.txt')
    
    result = lendoArquivoPendrive('D:', 'TESTE-01.txt')
    print(result)