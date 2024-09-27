from sys import stdin


def generate_binary_numbers(n: int):
    if n == 1:
        return ['0', '1']
    else:
        sub_results = generate_binary_numbers(n - 1)
        results = []
        for sub_result in sub_results:
            results.append('0' + sub_result)
            results.append('1' + sub_result)
        return results


for num in stdin:
    print(*generate_binary_numbers(int(num)), sep='\n')

# made by Genimi Ai
