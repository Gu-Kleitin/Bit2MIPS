
from resolucao import escrever
REGISTRADORES = {
    '00000': '$zero', '00001': '$at', '00010': '$v0', '00011': '$v1',
    '00100': '$a0', '00101': '$a1', '00110': '$a2', '00111': '$a3',
    '01000': '$t0', '01001': '$t1', '01010': '$t2', '01011': '$t3',
    '01100': '$t4', '01101': '$t5', '01110': '$t6', '01111': '$t7',
    '10000': '$s0', '10001': '$s1', '10010': '$s2', '10011': '$s3',
    '10100': '$s4', '10101': '$s5', '10110': '$s6', '10111': '$s7',
    '11000': '$t8', '11001': '$t9', '11010': '$k0', '11011': '$k1',
    '11100': '$gp', '11101': '$sp', '11110': '$fp', '11111': '$ra'
}

# Principais instruções do tipo R
R_TYPE_FUNCTION = {
    '100000': 'add',   '100001': 'addu', '100100': 'and',  '100111': 'nor',
    '100110': 'xor',   '100101': 'or',   '101010': 'slt',  '101011': 'sltu',
    '000000': 'sll',   '000010': 'srl',  '000011': 'sra',  '011000': 'mult',
    '011001': 'multu', '011010': 'div',  '011011': 'divu', '010000': 'mfhi',
    '010010': 'mflo',  '001000': 'jr',   '001001': 'jalr', '100010': 'sub'
}

# Principais instruções do Tipo I
I_TYPE_OPCODE = {
    '001000': 'addi', '001001': 'addiu', '001100': 'andi', '001101': 'ori',
    '001110': 'xori', '001010': 'slti', '001011': 'sltiu', '100011': 'lw',
    '101011': 'sw', '100000': 'lb', '100100': 'lbu', '100001': 'lh',
    '100101': 'lhu', '100010': 'lwl', '100110': 'lwr', '101000': 'sb',
    '101001': 'sh', '101010': 'swl', '101110': 'swr', '000100': 'beq',
    '000101': 'bne', '000110': 'blez', '000111': 'bgtz', '001111': 'lui'
}

#Principal instrução do tipo J
J_TYPE_OPCODE = {
    '000010': 'j', '000011': 'jal'
}

def decodificacao(instrucao):

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
            if mnemonico in ('srl', 'sll', 'sra'):
               return f"{mnemonico}, {REGISTRADORES[rd]}, {REGISTRADORES[rt]}, {int(shamt, 2)})"
            elif mnemonico in ('jr', 'jalr'):
                return f"{mnemonico}, {REGISTRADORES[rs]}"
            elif mnemonico in ['mfhi', 'mflo']:
                return f"{mnemonico} {REGISTRADORES[rd]}"
            elif mnemonico in ['mult', 'multu', 'div', 'divu']:
                return f"{mnemonico} {REGISTRADORES[rs]}, {REGISTRADORES[rt]}"
    
            else:
                return f"{mnemonico}, {REGISTRADORES[rd]}, {REGISTRADORES[rs]}, {REGISTRADORES[rt]}"
                
        elif opcode in I_TYPE_OPCODE:
            rs = instrucao[6:11]
            rt = instrucao[11:16]
            imediato = instrucao[16:32]

            mnemonico = I_TYPE_OPCODE.get(opcode)

            # Conversão do imediato para número com sinal (signed)
            valor_imediato = int(imediato, 2)
            if imediato[0] == '1':  # Se for negativo (bit mais significativo é 1)
                #valor_imediato -= (1 << 16)
                valor_imediato -= (1 << len(imediato)) #para ser mais genérico

            if mnemonico in ('lw', 'sw', 'lb', 'lbu', 'lh', 'lhu', 'lwl', 'lwr', 'sb', 'sh', 'swl', 'swr'):
                # Formato: lw/sw rt, offset(rs)
                return f"{mnemonico} {REGISTRADORES[rt]}, {valor_imediato} ({REGISTRADORES[rs]})"

            elif mnemonico in ('beq', 'bne', 'blez', 'bgtz'):
                # Formato: beq rs, rt, label (offset)
                if mnemonico in ('beq', 'bne'):
                    return f"{mnemonico} {REGISTRADORES[rs]}, {REGISTRADORES[rt]}, {valor_imediato}"
                else:
                    return f"{mnemonico} {REGISTRADORES[rs]}, {valor_imediato}"
            elif mnemonico == 'lui':
                return f"{mnemonico} {REGISTRADORES[rt]}, {valor_imediato}"
            else:
                # Formato: addi/andi/ori rt, rs, imediato
                return f"{mnemonico} {REGISTRADORES[rt]}, {REGISTRADORES[rs]}, {valor_imediato}"

        elif opcode in J_TYPE_OPCODE:
            imediato = instrucao[6:32]
            mnemonico = J_TYPE_OPCODE.get(opcode)
            if not mnemonico:
                return f"Erro: Mnemônico do Tipo J é desconhecido para o opcode: {opcode}"
            
            return f"{mnemonico} {int(imediato, 2)}"
        else:
            return f"Erro: Opcode desconhecido: {opcode}"
        
        index=index+32
    
