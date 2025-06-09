# Dicionários. Estou me baseando nos slides da aula.

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

def decodificacao (instrucao):
  opcode = instrucao[0:6]

# Condicional para instruções do tipo R
  if opcode == '000000': #Opcode
    #Como as instruções vão ser lidas da esquerda para a direita, o sentido de contagem dos bits para alocamento nas variáveis é o inverso do que foi mostrado na tabela da aula. Ao invés de 31-0 temos 0-31
    rs = instrucao[6:11]
    rt = instrucao[11:16]
    rd = instrucao[16:21]
    shamt = instrucao[21:26]
    function = instrucao[26:32]

    mnemonico = R_TYPE_FUNCTION.get(function)
    if not mnemonico:
      return f"Erro: Mnemônico do Tipo R é desconhecido para o campo function: {function}"
    
    #As instruções srl e sll são instruções de salto e não contém o rs. o int(shamt, 2) é para transformar o valor binário do shamt em decimal
    if mnemonico in ('srl', 'sll'):
      return f"{mnemonico}, {REGISTRADORES[rd]}, {REGISTRADORES[rt]}, {int(shamt, 2)})"
    
    elif mnemonico in ('jr'):
      return f"{mnemonico}, {REGISTRADORES[rs]}"
    
    else:
      return f"{mnemonico}, {REGISTRADORES[rd]}, {REGISTRADORES[rs]}, {REGISTRADORES[rt]}"
  
  #Condicional do tipo J, o imediato vai ser convertido para binário
  elif opcode in J_TYPE_OPCODE:
    imediato = instrucao[6:32]
    mnemonico = J_TYPE_OPCODE.get(opcode)
    if not mnemonico:
      return f"Erro: Mnemônico do Tipo J é desconhecido para o opcode: {opcode}"
      
    return f"{mnemonico} {int(imediato, 2)}"

