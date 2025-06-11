def escrever(linha, ns):

    linha = str(linha)
    
    with open("D:/Trabalho/TESTE-"+ns+"-RESULTADO.txt", "w") as arquivo:
        arquivo.write(linha+"\n")
    
    return f"Arquivo TESTE-{ns}-RESULTADO criado"
    