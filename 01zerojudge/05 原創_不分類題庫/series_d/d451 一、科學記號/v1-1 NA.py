# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge 451. 一、科學記號 v1-1


def convert_to_scientific_notation(num: str, precision: int) -> str:
    num_float = float(num)

    # handle special cases of zero
    if num_float == 0:
        return '0' + (('.' + '0' * (precision -  1)) if precision > 1 else '') + 'x10(0)'
    
    # Determine the exponent (power of 10)
    if num_float >= 1:
        exponent = len(num.split('.')[0]) - 1
    else:
        exponent = len(num.replace('.', '').strip('0')) - len(num.replace('.', '').rstrip('0'))
    
    # Determine the normalized value
    num_float /= 10 ** exponent
    num_float = round(num_float, precision - 1)
    num_float = str(num_float).rstrip('0')
    if len(num_float) < precision + 1:
        num_float = num_float.ljust(precision + 1, '0')
    
    return num_float.rstrip('.') + 'x10(' + str(exponent) + ')'


def main():
    for _ in range(int(input())):
        num, precision = input().split()
        print(convert_to_scientific_notation(''.join(num.split(',')), int(precision)))


if __name__ == '__main__':
    main()
