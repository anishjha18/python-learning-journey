# Leap year checker
x=int(input("Enter a year: "))
if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print(f"{x} is a leap year.")
else:
    print(f"{x} is not a leap year.")

# Example usage
year = int(input("Enter a year to check if it's a leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    