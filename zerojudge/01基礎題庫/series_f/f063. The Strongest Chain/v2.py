times = int(input())

chain_data = [min(list(map(int, input().split()))[1:]) for _ in range(times)]

print(max(chain_data))