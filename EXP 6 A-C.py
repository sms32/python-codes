#Write a Python program to find the second most repeated word in a
#given string.



string = input("Enter a string :-")
l = string.split()
max = 0
sec = 0
for i in l:
    if l.count(i) >= max :
        max = l.count(i)
    elif l.count(i) >= sec :
        sec = l.count(i)
        a = i

print("Second most repeated word is : ", a )
