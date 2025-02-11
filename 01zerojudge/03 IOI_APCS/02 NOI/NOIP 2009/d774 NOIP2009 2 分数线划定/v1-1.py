# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d774. NOIP2009 2.分数线划定
# NOIP 2009


n, target = map(int, input().split())
data = [input().split() for _ in range(n)]

target = target * 3 // 2
data.sort(key=lambda x: (-int(x[1]), int(x[0])))
score_line = int(data[target - 1][1])
result = [i for i in data if int(i[1]) >= score_line]

print(f'{score_line} {len(result)}',
      '\n'.join(' '.join(i) for i in result),
      sep='\n')
