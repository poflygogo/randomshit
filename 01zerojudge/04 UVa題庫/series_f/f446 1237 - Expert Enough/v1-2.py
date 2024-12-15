# -*- encoding: utf-8 -*-
# python 3.12
# UVa 1237 Expert Enough
# ZeroJudge f446



def mainloop():
    T = int(input())
    for times in range(T):
        factories = []
        for _ in range(int(input())):
            fac, a, b = input().split()
            factories.append((fac, int(a), int(b)))
        print(
            *[get_factory(factories, int(input())) for _ in range(int(input()))],
            sep='\n',
            end='\n\n' if times < T - 1 else '\n'
        )


def get_factory(factories: list, query: int) -> str:
    result = []
    for fac, a, b in factories:
        if a <= query <= b:
            result.append(fac)
        if len(result) > 1:
            return 'UNDETERMINED'
    if result:
        return result[0]
    return 'UNDETERMINED'


mainloop()


# def mainloop_but_for_test():
#     with open(r'01zerojudge\04 UVa題庫\series_f\f446 1237 - Expert Enough\test.txt', 'r', encoding='utf-8') as stdin:
#         stdout = open(r'01zerojudge\04 UVa題庫\series_f\f446 1237 - Expert Enough\test_ans.txt', 'a', encoding='utf-8')
#         for _ in range(int(next(stdin).rstrip())):
#             factories = []
#             for _ in range(int(next(stdin).rstrip())):
#                 fac, a, b = next(stdin).rstrip().split()
#                 factories.append((fac, int(a), int(b)))
#             for _ in range(int(next(stdin).rstrip())):
#                 ans = get_factory(factories, int(next(stdin).rstrip()))
#                 stdout.write(ans + '\n')
#             stdout.write('\n')


# mainloop_but_for_test()
