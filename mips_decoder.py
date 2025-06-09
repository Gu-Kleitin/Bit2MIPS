#este código foi gerado por IA e serve só para tirar dúvidas durante o projeto

# Dicionário para mapeamento de registradores
REGISTERS = {
    '00000': '$zero', '00001': '$at', '00010': '$v0', '00011': '$v1',
    '00100': '$a0', '00101': '$a1', '00110': '$a2', '00111': '$a3',
    '01000': '$t0', '01001': '$t1', '01010': '$t2', '01011': '$t3',
    '01100': '$t4', '01101': '$t5', '01110': '$t6', '01111': '$t7',
    '10000': '$s0', '10001': '$s1', '10010': '$s2', '10011': '$s3',
    '10100': '$s4', '10101': '$s5', '10110': '$s6', '10111': '$s7',
    '11000': '$t8', '11001': '$t9', '11010': '$k0', '11011': '$k1',
    '11100': '$gp', '11101': '$sp', '11110': '$fp', '11111': '$ra'
}

# Opcodes e funct codes para instruções R-Type
R_TYPE_FUNCT = {
    '100000': 'add',   '100001': 'addu', '100100': 'and',  '100111': 'nor',
    '100110': 'xor',   '100101': 'or',   '101010': 'slt',  '101011': 'sltu',
    '000000': 'sll',   '000010': 'srl',  '000011': 'sra',  '011000': 'mult',
    '011001': 'multu', '011010': 'div',  '011011': 'divu', '010000': 'mfhi',
    '010010': 'mflo',  '001000': 'jr',   '001001': 'jalr'
}

# Opcodes para instruções I-Type
I_TYPE_OPCODE = {
    '001000': 'addi', '001001': 'addiu', '001100': 'andi', '001101': 'ori',
    '001110': 'xori', '001010': 'slti', '001011': 'sltiu', '100011': 'lw',
    '101011': 'sw', '100000': 'lb', '100100': 'lbu', '100001': 'lh',
    '100101': 'lhu', '100010': 'lwl', '100110': 'lwr', '101000': 'sb',
    '101001': 'sh', '101010': 'swl', '101110': 'swr', '000100': 'beq',
    '000101': 'bne', '000110': 'blez', '000111': 'bgtz', '001111': 'lui'
}

# Opcodes para instruções J-Type
J_TYPE_OPCODE = {
    '000010': 'j', '000011': 'jal'
}

def decode_mips_instruction(binary_instruction):
    opcode = binary_instruction[0:6]

    if opcode == '000000':  # R-Type
        rs = binary_instruction[6:11]
        rt = binary_instruction[11:16]
        rd = binary_instruction[16:21]
        shamt = binary_instruction[21:26]
        funct = binary_instruction[26:32]

        mnemonic = R_TYPE_FUNCT.get(funct)
        if not mnemonic:
            return f"Instrução R-Type desconhecida (funct: {funct})"

        if mnemonic in ['sll', 'srl', 'sra']:
            return f"{mnemonic} {REGISTERS[rd]}, {REGISTERS[rt]}, {int(shamt, 2)}"
        elif mnemonic in ['jr', 'jalr']:
            return f"{mnemonic} {REGISTERS[rs]}"
        elif mnemonic in ['mfhi', 'mflo']:
            return f"{mnemonic} {REGISTERS[rd]}"
        elif mnemonic in ['mult', 'multu', 'div', 'divu']:
            return f"{mnemonic} {REGISTERS[rs]}, {REGISTERS[rt]}"
        else:
            return f"{mnemonic} {REGISTERS[rd]}, {REGISTERS[rs]}, {REGISTERS[rt]}"

    elif opcode in I_TYPE_OPCODE:  # I-Type
        rs = binary_instruction[6:11]
        rt = binary_instruction[11:16]
        immediate = binary_instruction[16:32]
        
        mnemonic = I_TYPE_OPCODE.get(opcode)
        if not mnemonic:
            return f"Instrução I-Type desconhecida (opcode: {opcode})"

        if mnemonic in ['lw', 'sw', 'lb', 'lbu', 'lh', 'lhu', 'lwl', 'lwr', 'sb', 'sh', 'swl', 'swr']:
            # Load/Store instructions: mnemonic rt, offset(rs)
            signed_immediate = int(immediate, 2)
            if immediate[0] == '1': # Check for negative immediate
                signed_immediate = signed_immediate - (1 << len(immediate))
            return f"{mnemonic} {REGISTERS[rt]}, {signed_immediate}({REGISTERS[rs]})"
        elif mnemonic in ['beq', 'bne', 'blez', 'bgtz']:
            # Branch instructions: mnemonic rs, rt, offset (or mnemonic rs, offset for blez/bgtz)
            # For simplicity, we'll just show the immediate value as offset for now
            signed_immediate = int(immediate, 2)
            if immediate[0] == '1': # Check for negative immediate
                signed_immediate = signed_immediate - (1 << len(immediate))
            if mnemonic in ['beq', 'bne']:
                return f"{mnemonic} {REGISTERS[rs]}, {REGISTERS[rt]}, {signed_immediate}"
            else:
                return f"{mnemonic} {REGISTERS[rs]}, {signed_immediate}"
        elif mnemonic == 'lui':
            return f"{mnemonic} {REGISTERS[rt]}, {int(immediate, 2)}"
        else:
            # Other I-Type instructions: mnemonic rt, rs, immediate
            signed_immediate = int(immediate, 2)
            if immediate[0] == '1': # Check for negative immediate
                signed_immediate = signed_immediate - (1 << len(immediate))
            return f"{mnemonic} {REGISTERS[rt]}, {REGISTERS[rs]}, {signed_immediate}"

    elif opcode in J_TYPE_OPCODE:  # J-Type
        address = binary_instruction[6:32]
        mnemonic = J_TYPE_OPCODE.get(opcode)
        if not mnemonic:
            return f"Instrução J-Type desconhecida (opcode: {opcode})"
        # For J-type, the address is 26 bits, but the actual jump address is PC-relative and shifted.
        # For this exercise, we'll just show the raw address for simplicity.
        return f"{mnemonic} 0x{int(address, 2):X}"

    else:
        return f"Opcode desconhecido: {opcode}"

import os

def process_test_files(input_dir='.', num_files=10):
    for i in range(1, num_files + 1):
        file_number = str(i).zfill(2)
        input_filename = f"TESTE-{file_number}.txt"
        output_filename = f"TESTE-{file_number}-RESULTADO.txt"
        
        input_filepath = os.path.join(input_dir, input_filename)
        output_filepath = os.path.join(input_dir, output_filename)

        if not os.path.exists(input_filepath):
            print(f"Arquivo de entrada não encontrado: {input_filepath}. Pulando...")
            continue

        print(f"Processando {input_filepath}...")
        with open(input_filepath, 'r') as infile, open(output_filepath, 'w') as outfile:
            for line in infile:
                binary_instruction = line.strip()
                if len(binary_instruction) == 32 and all(c in '01' for c in binary_instruction):
                    mnemonic = decode_mips_instruction(binary_instruction)
                    outfile.write(mnemonic + '\n')
                else:
                    outfile.write(f"Erro: Linha inválida - {binary_instruction}\n")
        print(f"Resultado salvo em {output_filepath}")

if __name__ == "__main__":
    process_test_files()