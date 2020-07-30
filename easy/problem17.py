# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 

letters = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
}

count = 0
# i = 100
for i in range(1, 1000):
    # three-digit-number
    if i // 100 >= 1:
        # even hundred
        if i % 100 == 0:
            count += letters[i // 100]
        # even tens
        elif i % 10 == 0:
            count += letters[i // 100] + letters[i % 100] + 3  # and = 3
        # two-digit ending > 20
        elif i % 100 > 20:
            count += letters[i // 100] + letters[(i % 100) // 10 * 10] + letters[i % 10] + 3  # and = 3
        # teens and single digit
        else:
            count += letters[i // 100] + letters[i % 100] + 3  # and = 3
        count += 7  # hundred = 7
    # two-digit number >= 20
    elif i // 10 > 1 and i // 10 < 10:
        # even tens
        if i % 10 == 0:
            count += letters[i]
        else:
            count += letters[i // 10 * 10] + letters[i % 10]
    # teens or single digit
    else:
        count += letters[i]
count += 3 + 8  # one thousand

print(count)