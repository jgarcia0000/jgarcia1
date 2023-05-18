def calculate_lcm(a, b):
    # Find the greater number
    greater = max(a, b)
    # Initialize lcm as the greater number
    lcm = greater

    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
        lcm += greater

    return lcm

# Prompt the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the LCM
result = calculate_lcm(num1, num2)

# Display the result
print(f"The LCM of {num1} and {num2} is: {result}")
