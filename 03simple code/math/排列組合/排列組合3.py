def permute(s):
    if len(s) == 1:
        return [s]
    res = []
    for i in range(len(s)):
        for p in permute(s[:i] + s[i+1:]):
            res.append(s[i] + p)
    return res