import math

#task 01 Grade calculator
mark1 = float(input("Enter the first mark: "))
mark2 = float(input("Enter the second mark: "))
mark3 = float(input("Enter the third mark: "))
mark4 = float(input("Enter the fourth mark: "))
mark5 = float(input("Enter the fifth mark: "))
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

if 0 > average > 100:
    print("Invalid input")
elif average >= 75:
    print("A")
elif average >= 65:
    print("B")
elif average >= 55:
    print("C")
elif average >= 35:
    print("S")
else:
    print("F")

#task 02 Savings Goal tracker
target = float(input("Enter the target amount: "))
current = float(input("Enter the current amount: "))
mothly_amount = float(input("Enter the monthly saving amount: "))

months = math.ceil((target - current) / mothly_amount)
print("You will reach your goal in", months, "months")

#task 03 Distance between two points
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))

x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")