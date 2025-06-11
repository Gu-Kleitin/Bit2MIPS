
from resolucao import escrever
REGISTRADORES = {
  '01000': '$t0', '01110': '$t6', '10100': '$s4',
  '01001': '$t1', '01111': '$t7', '10101': '$s5',
  '01010': '$t2', '10000': '$s0', '10110': '$s6',
  '01011': '$t3', '10001': '$s1', '10111': '$s7',
  '01100': '$t4', '10010': '$s2', '00000': '$zero',
  '01101': '$t5', '10011': '$s3'
}

# Principais instruções do tipo R
R_TYPE_FUNCTION = {
  '100000': 'add', '100010': 'sub', '100100': 'and', '100101': 'or',
  '100111': 'nor', '000000': 'sll', '000010': 'srl',  '001000': 'jr'
}

# Principais instruções do Tipo I
I_TYPE_OPCODE = {
  '001000': 'addi', '001100': 'andi', 
  '100011': 'lw',   '101011': 'sw',   
  '000101': 'bne',  '001101': 'ori',
  '000100': 'beq'
}

#Principal instrução do tipo J
J_TYPE_OPCODE = {
  '000010': 'j'
}

def decodificacao(linha, ns):
    code = linha.replace("\n","")
    index = 0
    while (index != len(code)):

        instrucao = code[index:index+32]

        opcode = instrucao[0:6]

        if(opcode == "000000"):
            #Como as instruções vão ser lidas da esquerda para a direita, o sentido de contagem dos bits para alocamento nas variáveis é o inverso do que foi mostrado na tabela da aula. Ao invés de 31-0 temos 0-31
            rs = instrucao[6:11]
            rt = instrucao[11:16]
            rd = instrucao[16:21]
            shamt = instrucao[21:26]
            function = instrucao[26:32]

            mnemonico = R_TYPE_FUNCTION.get(function)
            if not mnemonico:
                return f"Erro: mnemônico do tipo R desconhecido para o funct: {function}"
            
            if mnemonico in ('srl', 'sll'):
                result = mnemonico, REGISTRADORES[rd], REGISTRADORES[rt], int(shamt, 2)
                escrever(result, ns)
            
            elif mnemonico in ('jr'):
                result = mnemonico, REGISTRADORES[rs]
                escrever(result, ns)
    
            else:
                result = mnemonico, REGISTRADORES[rd], REGISTRADORES[rs], REGISTRADORES[rt]
                escrever(result, ns)
                
        elif opcode in J_TYPE_OPCODE:
            imediato = instrucao[6:32]
            mnemonico = J_TYPE_OPCODE.get(opcode)
            result = mnemonico, int(imediato, 2)
            escrever(result, ns)

        elif opcode in I_TYPE_OPCODE:
            rs = instrucao[6:11]
            rt = instrucao[11:16]
            imediato = instrucao[16:32]
            mnemonico = I_TYPE_OPCODE.get(opcode)

            # Conversão do imediato para número com sinal (signed)
            valor_imediato = int(imediato, 2)
            if imediato[0] == '1':  # Se for negativo (bit mais significativo é 1)
                valor_imediato -= (1 << 16)

            if mnemonico in ('lw', 'sw'):
                # Formato: lw/sw rt, offset(rs)
                result = mnemonico, REGISTRADORES[rt], valor_imediato, REGISTRADORES[rs]
                escrever(result, ns)

            elif mnemonico in ('beq', 'bne'):
                # Formato: beq rs, rt, label (offset)
                result = mnemonico, REGISTRADORES[rs], REGISTRADORES[rt], valor_imediato
                escrever(result, ns)

            else:
                # Formato: addi/andi/ori rt, rs, imediato
                result = mnemonico, REGISTRADORES[rt], REGISTRADORES[rs], valor_imediato
                escrever(result, ns)

        index=index+32
    
