#Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to ‘#’ except the first char
#itself.

L = input("ENTER A STRING : ")
A = L
B = A[0]
A = A.replace(B, '#')
A = B + A[1:]
print(A)

