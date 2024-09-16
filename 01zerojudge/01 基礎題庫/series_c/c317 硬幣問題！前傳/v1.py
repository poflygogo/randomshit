from sys import stdin, stdout

_ = stdin.readline()
for line in stdin:
    cost, curr_a, curr_b = map(int, line.strip().split())

    count_a = cost // curr_a
    while count_a >= 0:
        remain = cost - (curr_a * count_a)
        if remain % curr_b == 0:
            stdout.write(f'{count_a + remain // curr_b}\n')
            break

        count_a -= 1
    else:
        stdout.write('-1\n')