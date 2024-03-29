def is_perfect_number(num):
    # Validate that the number is positive
    if num <= 0:
        return False
    
    # Find the sum of proper divisors
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    # Check if the sum of divisors equals the original number
    return divisors_sum == num

# Get input from the user
number = int(input("Enter a number: "))

# Check and display the result
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
