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
  '100111': 'nor', '000000': 'sll', '000010': 'srl'
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

