# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e571. 詞語接龍


from typing import List, Dict


def find_longest_chain(graph: Dict[int, List[int]], start: int):
    def _dfs(curr):
        if curr not in graph or all(i in seen for i in graph[curr]):
            nonlocal result
            result = max(result, len(seen))
            return
        for i in graph[curr]:
            if i not in seen:
                seen.add(i)
                _dfs(i)
                seen.remove(i)

    seen = {start}
    result = 0
    _dfs(start)
    return result
    

def word_chain(n: int, arr: List[str], fail_msg: str = "1\n什麼爛表"):
    # 建立鄰接表
    graph = {}
    for i in range(n):
        for j in range(n):
            if i != j and arr[i][-1] == arr[j][0]:
                if i in graph:
                    graph[i].append(j)
                else:
                    graph[i] = [j]
    if not graph:
        return fail_msg
    
    counter = {i: find_longest_chain(graph, i) for i in graph}
    max_val = max(counter.values())
    return f'{max_val}\n' + ' '.join(arr[i] for i in counter if counter[i] == max_val)


def main():
    while True:
        try:
            n = int(input())
            arr = [input() for _ in range(n)]
            print(word_chain(n, arr))
        except EOFError:
            break


main()
