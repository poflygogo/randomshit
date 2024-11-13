from sys import stdin
import re


for line in stdin:
    line = line.rstrip().split('/')
    if line == ['e', 'o', 'i']:
        exit()

    # 使用 enumerate() 順便把字串的 index 提取出來
    for idx, word in enumerate(line):
        # 用正則表達式分析資料: r'[aeiouy]+' 意思是匹配連續的母音字符，並將結果以 list[str] 的形式回傳
        syllable = len(re.findall(r'[aeiouy]+', word))
        if not syllable == (5, 7)[idx % 2]:
            print(idx + 1)
            break
    else:
        print('Y')
