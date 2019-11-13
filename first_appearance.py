
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

digits = dict()
with open('pi.txt', 'r') as infile:
    pi = infile.readline()
    for idx in range(len(pi)):
        if pi[idx] in numbers:
            digits[pi[idx]] = idx
            numbers.remove(pi[idx])
            if not numbers:
                break

print(digits)
counts = 0
for digit, count in digits.items():
    counts += count

print(counts/len(digits))

# {'3': 0, '1': 1, '4': 2, '5': 4, '9': 5, '2': 6, '6': 7, '8': 11, '7': 13}