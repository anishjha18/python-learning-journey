#smallest number among three numbers
numbers=[10,5,3]
smallest=numbers[0]
for num in numbers:
    if num < smallest:
        smallest=num
print("The smallest number is:",smallest)

# Example usage
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
smallest = min(num1, num2, num3)
print(f"The smallest number among {num1}, {num2}, and {num3} is {smallest}.")