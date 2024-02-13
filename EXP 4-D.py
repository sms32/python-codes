def is_happy_number(num):
    seen_numbers = set()

    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))

    return num == 1

# Get input from the user
number = int(input("Enter a number: "))

# Check and display the result
if is_happy_number(number):
    print(f"{number} is a Happy Number.")
else:
    print(f"{number} is not a Happy Number.")
