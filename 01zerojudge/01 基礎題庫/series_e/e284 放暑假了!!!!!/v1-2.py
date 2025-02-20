# # -*- encoding: utf-8 -*-
# # python 3.12
# # ZeroJudge e284. 放暑假了!!!!!


from sys import stdin, stdout

nums = [0] * 33
nums[0] = 1
for i in range(1, 33):
    nums[i] = 2 * nums[i - 1]
nums = frozenset(nums)

for n in stdin.read().splitlines():
    stdout.write('Yes\n' if int(n) in nums else 'No\n')
