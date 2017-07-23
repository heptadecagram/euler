#!/usr/local/bin/python

lookup = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
        }

def in_words(n):
    val = ''
    if n > 999:
        val += '{}thousand'.format(lookup[n//1000])
        if n % 1000 == 0:
            return val

        n %= 1000

    if n > 99:
        val += '{}hundred'.format(lookup[n//100])
        if n % 100 == 0:
            return val

        val += 'and'
        n %= 100

    if n in lookup:
        val += lookup[n]
        return val

    val += lookup[n//10 * 10]
    val += lookup[n%10]

    return val

total = 0
for i in range(1, 1001):
    total += len(in_words(i))
    print(in_words(i))
print(total)




