from itertools import permutations


def create_ans_file(id: int, n: int, nums: list[int]):
    with open(f'./case{id}_ans.txt', 'a') as f:
        nums.sort()
        f.write('\n'.join(' '.join(map(str, i)) for i in permutations(nums)) + '\n')


def read_test_file(id: int) -> tuple[int, list[int]]:
    with open(f'./case{id}_test.txt') as f:
        n = int(f.readline().rstrip())
        nums = list(map(int, f.readline().rstrip().split()))
    return n, nums


def main():
    for i in range(20):
        n, nums = read_test_file(i)
        create_ans_file(i, n, nums)


if __name__ == '__main__':
    main()
