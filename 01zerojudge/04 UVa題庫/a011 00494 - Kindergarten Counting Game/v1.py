import re, sys

for line in sys.stdin:
    line = line.strip()
    result = re.findall(r'[A-Za-z]+', line)
    print(len(result))