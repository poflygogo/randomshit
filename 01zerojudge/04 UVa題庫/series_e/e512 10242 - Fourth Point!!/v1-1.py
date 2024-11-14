# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10242 Fourth Point!!
# ZeroJudge e512


while True:
    try:
        vertex = tuple(map(float, input().split()))
    except EOFError:
        exit()
    else:
        if (vertex[0], vertex[1]) == (vertex[4], vertex[5]):
            print(f'{vertex[2] + vertex[6] - vertex[0]:.3f} {vertex[3] + vertex[7] - vertex[1]:.3f}')

        elif (vertex[0], vertex[1]) == (vertex[6], vertex[7]):
            print(f'{vertex[2] + vertex[4] - vertex[0]:.3f} {vertex[3] + vertex[5] - vertex[1]:.3f}')

        elif (vertex[2], vertex[3]) == (vertex[4], vertex[5]):
            print(f'{vertex[0] + vertex[6] - vertex[2]:.3f} {vertex[1] + vertex[7] - vertex[3]:.3f}')

        else:
            print(f'{vertex[0] + vertex[4] - vertex[2]:.3f} {vertex[1] + vertex[5] - vertex[3]:.3f}')
