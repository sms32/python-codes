# AIM: PYTHON CODE TO CHECK A NUMBER IS PALINDROME OR NOT

"""
STEP 1: START
STEP 2: ENTER A NUMBER 
STEP 3:set equal to num and reverse equal to 0
STEP 4:while temp greater than 0 , remainder is equal to temp %10 
STEP 5:multiply reverse with 10 and add remainder which is equal to reverse and temp is equal to temp //10
STEP 6:if num is equal to reverse then given number is palindrome
STEP 7: DISPLAY OUTPUT
STEP 8: STOP
"""

num = int(input("Enter a number :"))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")


# RESULT: Understood the aim and executed the program.
