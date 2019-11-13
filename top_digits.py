
digits = dict()

with open('pi.txt', 'r') as infile:
    pi = infile.readline()
    for digit in pi:
        digits[digit] = digits.setdefault(digit, 0) + 1

print(sorted([(number, count) for number, count in digits.items()], key=lambda x: x[1], reverse=True))
