birthday = sum(int(i) * j for i, j in zip(input().split(), (100, 1)))
print(
    'Capricorn' if birthday <= 120
    else 'Aquarius' if birthday <= 219
    else 'Pisces' if birthday <= 320
    else 'Aries' if birthday <= 420
    else 'Taurus' if birthday <= 521
    else 'Gemini' if birthday <= 621
    else 'Cancer' if birthday <= 722
    else 'Leo' if birthday <= 821
    else 'Virgo' if birthday <= 923
    else 'Libra' if birthday <= 1023
    else 'Scorpio' if birthday <= 1122
    else 'Sagittarius' if birthday <= 1222
    else 'Capricorn'
)
