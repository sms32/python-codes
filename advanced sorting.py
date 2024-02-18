#SORTING AN ALPHANUMERIC CHARACTER AS LOWERCASE LETTERS FIRST THEN UPPERCASE THEN ODD NUMBERS AND IN THE END EVEN NUMBERS WILL BE PRINTED .


s = input()
upper, lower,odd, even  = [], [], [], []

for char in s:
    if char.isnumeric():
        if int(char)%2 == 0:
            even.append(char)
        else:
            odd.append(char)
    else:
        if char.isupper():
            upper.append(char)
        else:
            lower.append(char)

print(''.join(sorted(lower))+''.join(sorted(upper))+''.join(sorted(odd))+''.join(sorted(even)))
