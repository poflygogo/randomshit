times = int(input())

chain_data = []
for _ in range(times):
    chain = list(map(int, input().split()))[1:]
    chain_data.append(min(chain))

print(max(chain_data))