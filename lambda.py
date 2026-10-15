
def add(a, b):
    return a + b


# Lambda Function
multiply = lambda a, b: a * b


# Taking input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


# Calling normal function
sum_result = add(num1, num2)

# Calling lambda function
multiply_result = multiply(num1, num2)


# Displaying results
print("Addition =", sum_result)
print("Multiplication =", multiply_result)