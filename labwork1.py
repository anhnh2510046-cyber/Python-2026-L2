#  Excercise 1: Write a program that calculates the area of a circle. The circle radius is entered by users.
radius = float(input("Enter circle radius? "))
area = 3.14 * radius ** 2
print(f"Circle area = {area}")

# Excercise 2: Write a program that converts Celsius (0C) into Fahrenheit (0F).
c = float(input("Enter the temperature in Celcius? "))
f = c * 9/5 + 32
print(f"{c} (C) = {f} (F)")

# Excercise 3: Write a program that checks whether a number is prime or not
n = int(input("Enter a number? "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime: 
    print(f"{n} is a prime number")
else:
    print(f"{n} is NOT a prime number")

# Excercise 4:
n = int(input("Enter a number? "))
sum_divisors = sum(i for i in range(1, n) if n % i == 0)

if sum_divisors == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a NOT perfect number")

# Excercise 5:
colors = ["White", "Black", "Blue", "Red", "Brown", "Yellow", "Orange"]

fav_color = input("What is your favorite color? ")

if fav_color in colors:
    idx = colors.index(fav_color)
    print(f"Your color is at index {idx} in my list")
else:
    print("Sorry, I could not find your color")

# Excercise 6: 
range1 = list(range(0, 7))        # 0,1,2,3,4,5,6
range2 = list(range(1, 11, 3))    # 1,4,7,10
range3 = list(range(5, 0, -1))    # 5,4,3,2,1
range4 = list(range(6, -3, -2))   # 6,4,2,0,-2

print("range1:", range1)
print("range2:", range2)
print("range3:", range3)
print("range4:", range4)

# Excercise 7:
def remove_dollar_sign(s):
    return s.replace("$", "")
s = input("Enter a string containing '$': ")
print("Results: ", remove_dollar_sign(s))

# Excercise 8:
def extract_even(l):
    return [x for x in l if x % 2 == 0]
raw = input("Enter integers seperated by space: ")
numbers = [int(x) for x in raw.split()]
print ("Even items: ", extract_even(numbers))

# Excercise 9:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a non-negative integer: "))
print(factorial(n))

# Excercise 10:
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

n = int(input("Enter a number: "))
print(f"Divisors of {n}: ", get_divisors(n))

# Excercise 11:
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance between the two points = {distance}")

# Excercise 12:
def print_pattern(m, n):
    for i in range(m):          
        for j in range(n):      
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()   

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
print_pattern(m, n)


