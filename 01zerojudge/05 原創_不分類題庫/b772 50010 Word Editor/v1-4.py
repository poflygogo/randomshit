# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b772. 50010. Word Editor


# ---------------------------------------------------

import sys
import io
Q = """pangfeng
replace g d
remove n
addhead a
addtail s
end
pangfeng
replace g d
remove n
addhead a
addtail s
addpangfeng b
addhead a
end"""
sys.stdin = io.StringIO(Q.strip())

# --------------------------------------------------

from sys import stdin

for word in stdin:
    word = word.rstrip()
    for comm in stdin:
        comm = comm.rstrip().split()
        if comm[0] == 'end':
            print(word)
            break

        elif comm[0] == 'replace':
            word = word.replace(comm[1], comm[2])
        
        elif comm[0] == 'remove':
            word = word.replace(comm[1], '')
        
        elif comm[0] == 'addhead':
            word = comm[1] + word
        
        elif comm[0] == 'addtail':
            word += comm[1]
        
        else:
            # 笑死，餵自己吃 RE
            raise SyntaxError(f'invalid command {comm[0]}')
