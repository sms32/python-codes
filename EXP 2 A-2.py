l = [1, 2, 3, 1, 2, 5, 9, 10, 12, 15]
frequency = {}
for i in l:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] = 1


print(frequency)
