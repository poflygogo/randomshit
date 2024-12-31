# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d643. 勞動的符咒


def main():
    text = input().rstrip()
    factors = get_factors(len(text))
    result = {text}
    for i in factors:
        charm = get_charm(text, i)
        if charm not in result:
            print(charm)
            result.add(charm)
    if len(result) == 1:
        print('bomb!')


def grouper(iterable, n: int):
    # 參考 python 官方文檔, itertools的說明頁面最下方的附件: more_itertools 的 grouper
    # https://docs.python.org/3/library/itertools.html#itertools-recipes
    # 具體作用是將一個可迭代元素根據 n 的值拆分成多個部分
    iterators = [iter(iterable)] * n
    return zip(*iterators)


def get_charm(text: str, split_size: int) -> str:
    """根據 split_size 的值獲取符咒"""
    text_split = grouper(text, split_size)
    text_split = map(lambda x: ''.join(x), text_split)
    return ''.join(sorted(text_split))


def get_factors(n: int) -> list:
    """因數分解"""
    result = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            result.update({i, n // i})
    result.remove(n)
    return sorted(result)


if __name__ == '__main__':
    main()
