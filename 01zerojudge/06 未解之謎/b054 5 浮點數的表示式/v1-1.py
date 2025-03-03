# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b054. 5. 浮點數的表示式
# 96學年度高雄市資訊學科能力競賽

# ---------------------------------

import sys
import io
Q = """10
0.05
-10
-20.125"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------

def float_detail(n: str):
    binary = decimal_to_binary(n)
    if binary[1] != '0':
        exponent = len(binary[1])
        exponent_bin = exponent + 128   # 128 = 0b10000000
    else:
        exponent = len(binary[2]) - len(binary[2].lstrip('0'))
        exponent_bin = exponent ^ 127   # 127 = 0b1111111
        exponent_bin += 1
        exponent *= -1

    # bytes 裡面存的具體到底是什麼呢.......似乎不是二進制表達的數值
    n_bin = f'{int((binary[1] + binary[2]).lstrip('0'), 2):<024b}'

    print(
        f'Input a value: {n}',
        '                 Exponent lst byte 2nd byte 3rd byte',
        f'Memory Contents= {exponent_bin:8b} {binary[0] + n_bin[:7]} {n_bin[7:15]} {n_bin[15:23]}',
        f'                 <&H{exponent_bin:02X}>   <&H{int(binary[0] + n_bin[:7], 2):02X}>   <&H{int(n_bin[7:15], 2):02X}>   <&H{int(n_bin[15:23], 2):02X}>',
        f'FLOATING POINT FORMAT => {"-" if binary[0] == '1' else ""}0.{n_bin[:23]} * 2 ^ {exponent}',
        f'Floating Point Value = {n}',
        '=================================================================',
        sep='\n'
    )


def decimal_to_binary(n: str) -> str:
    binary = n.split('.')
    binary.insert(0, '01'[n.startswith('-')])       # 0 代表正, 1 代表負
    binary[1] = bin(int(binary[1].lstrip('-')))[2:]
    if len(binary) == 2:
        binary.append('0')
        return binary
    decimal, binary[2] = float('0.' + binary[2]), ''
    while decimal:
        decimal *= 2
        a, decimal = divmod(decimal, 1)
        binary[2] += str(int(a))
    return binary


def main():
    while True:
        try:
            n = input()
        except EOFError:
            break
        print(float_detail(n))


if __name__ == '__main__':
    main()
