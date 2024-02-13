#Write a Python program to get a single string from two given strings,
#separated by a space, and swap the first characters of each string.


A = input("ENTER A STRING : ")
B = input("ENTER ANOTHER STRING : ")
print(f"STRING 1 : {A} and STRING 2 : {B}")
d = A[0:1]
e = B[0:1]


C = A
A = B
B = C
print(d + A[1:] +" "+ e + B[1:])
