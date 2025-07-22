""" **Assignment 3: Using Lambda Functions in Python**Rewrite the functions from Assignment 4 using lambda functions.
**Instructions:**
1. Create a new Python file named `lambda_calculator.py`.
2. Define a lambda function for addition that takes two arguments and returns their sum.
3. Define a lambda function for subtraction that takes two arguments and returns their difference.
4. Define a lambda function for multiplication that takes two arguments and returns their product.
5. Define a lambda function for division that takes two arguments and returns their quotient.
6. Write a main block that calls each lambda function with sample inputs and prints the results. """

add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b


if __name__ == "__main__":
    x = 12
    y = 4

    print("Addition:", add(x, y))         
    print("Subtraction:", subtract(x, y)) 
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))     
