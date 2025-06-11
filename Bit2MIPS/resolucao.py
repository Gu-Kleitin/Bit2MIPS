import os

def escrever(linhas_decod, ns):
    """
    Escreve uma lista de linhas decodificadas em um arquivo de resultado.

    Args:
        linhas_decod(list): Uma lista de strings, onde cada string é um mnemônico decodificado.
        ns (str): O número formatado do arquivo de teste (ex: '01', '02').
    """

    #o caminho tem que ser alterado caso seja diferente
    output_dir = 'D:/Trabalho'
    output_filepath = os.path.join(output_dir, f"TESTE-{ns}-RESULTADO.txt")
    
    try:
        with open(output_filepath, 'w', encoding='utf-8') as arquivo:
            for linha in linhas_decod:
                arquivo.write(linha + "\n")
        
        print(f"Arquivo {output_filepath} criado!")

    except Exception as e:
        print(f"Erro ao escrever no arquivo {output_filepath}: {e}")

    #with open("D:/Trabalho/TESTE-"+ns+"-RESULTADO.txt", "w") as arquivo:
    #    arquivo.write(linha+"\n")
    
    #return f"Arquivo TESTE-{ns}-RESULTADO criado"
    