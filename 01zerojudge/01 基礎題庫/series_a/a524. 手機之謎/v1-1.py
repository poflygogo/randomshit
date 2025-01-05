# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a524. 手機之謎


def main():
    while True:
        try:
            n = input().rstrip()
        except EOFError:
            break

        if not n:
            continue
        print(phone_secret(int(n)))


def phone_secret(n: int):
    def backtrack(visit: set, path: list):
        if visit and path and len(visit) == n:
            result.append(path.copy())
            return
        for i in range(n, 0, -1):
            if i not in visit:
                visit.add(i)
                path.append(i)
                backtrack(visit, path)
                visit.remove(i)
                path.pop()

    result = []
    backtrack(set(), [])
    return '\n'.join(''.join(str(i) for i in line) for line in result)


if __name__ == '__main__':
    main()
