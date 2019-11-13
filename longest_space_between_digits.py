

digits = dict()
last_digit = dict()
with open('pi.txt', 'r') as infile:
    pi = infile.readline()
    for idx in range(len(pi)):
        digit = pi[idx]
        if int(digits.setdefault(digit, 0)) < idx - int(last_digit.setdefault(digit, 0)):
            digits[digit] = int(idx) - int(last_digit.setdefault(digit, 0))
        last_digit[digit] = idx


print(digits)
counts = 0
for digit, count in digits.items():
    counts += count

print(counts/len(digits))

