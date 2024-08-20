# 用title()方法可以一口氣將所有單字的開頭都改成大寫
print(
    *input().title().split(),
    sep='\n'
)