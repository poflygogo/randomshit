# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge f426. 高雄市109年資訊競賽國中組第四題
# 高雄市109年資訊競賽國中組第四題


a, b = int(input()), int(input())

# 歐拉篩
is_prime = [True] * (b + 1)
is_prime[0], is_prime[1] = False, False
prime_list = []
for i in range(2, b + 1):
    if is_prime[i] is True:
        prime_list.append(i)
    
    for j in prime_list:
        if i * j > b:
            break
        is_prime[i * j] = 0
        if i % j == 0:
            break

result_prime = [i for i in prime_list if i >= a]
print(len(result_prime), sum(result_prime), sep='\n')
