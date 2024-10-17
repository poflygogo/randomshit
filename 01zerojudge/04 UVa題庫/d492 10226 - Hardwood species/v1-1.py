from sys import stdin


def print_ans():
    total = sum(data.values())
    temp = sorted(data)
    for tree in temp:
        print(f'{tree} {data[tree] * 100 / total:.4f}')


stdin.readline()
stdin.readline()
data = {}
for tree in stdin:
    tree = tree.rstrip()
    if not tree:
        print_ans()
        print()
        data.clear()
        continue

    data[tree] = data.get(tree, 0) + 1
print_ans()

