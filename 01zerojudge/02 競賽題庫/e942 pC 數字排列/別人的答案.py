def main():
    from sys import stdin, stdout
    from itertools import permutations

    #d = [0,1,2,3,4,5,6,7,8]
    n = int(stdin.readline())
    f = sorted(stdin.readline().strip().split(), key = int)
    #p = d[:n]
    U = permutations(f)
    for u in U:
        stdout.write(f"{' '.join(u)}"+'\n')
main()
