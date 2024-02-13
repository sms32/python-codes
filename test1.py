def facto(n):
    if(n==1):
        return n
    else:
        return n*facto(n-1)

    print(f" FACTORIAL OF {i} is {fact}")
i=int(input("ENTER THE NUMBER : "))
if(i<0):
    print("FACTORIAL DOES NOT EXIST WITH NEGATIVE VALUE")
elif(i==0):
    print(f"FACTORIAL OF {i} is 1")
else:
    print(f" FACTORIAL OF {i} is {facto(i)}")
