#Tutorial 02
#Guided Practice Tasks

#Task 1 : Arithmetic Operations
def task1():
    print("2+4")
    print(2+4)
    print("2-4")
    print(2-4)
    print("2*4")
    print(2*4)
    print("2/4")
    print(2/4)

#Task 2 : Variable assignmnets
def task2():
    x = 5
    name = "Alice"
    print(x)
    print(name)

#Task 3 : Simple input and output
def task3():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello {name}, you are {age} years old.")

#Task 4 : String Concatenation
def task4():
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    print(full_name)

#Task 5 : Basic error handling
def task5():
    #print("hello"
    print("hello")

#Programmming excercises

#task 6 Basic arithmetic calculator
def task6():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    else:
        print("Invalid operation")

#task 7 :  Personal Information Script
def task7():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    color  = input("Enter your favorite color: ")
    print(f"Hello {name}, you are {age} years old and your favorite color is {color}.")

#task 8 :  Unit conversion program
def task8():
    num_of_days = int(input("Enter number of days: "))
    num_of_hours = num_of_days * 24
    num_of_minutes = num_of_hours * 60
    num_of_seconds = num_of_minutes * 60
    print(f"Number of hours: {num_of_hours}")
    print(f"Number of minutes: {num_of_minutes}")
    print(f"Number of seconds: {num_of_seconds}")

#task 9 :  Simple interest calculator
def task9():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time period: "))
    simple_interest = (principal * rate * time) / 100
    print(f"Simple Interest: {simple_interest}")


#Unguided Practice Tasks [To be done at home and submitted to BB]
#Task 10 :  temperature conversion program
def task10():
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def main():
        choice = input("Enter choice (1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius): ")
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(celsius)}")
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"Temperature in Celsius: {fahrenheit_to_celsius(fahrenheit)}")
        else:
            print("Invalid choice")

    main()

#Task 11 :  grocery bill estimator
def task11():
    def main():
        num_of_items = int(input("Enter number of items: "))
        total = 0
        for i in range(num_of_items):
            price = float(input(f"Enter price of item {i+1}: "))
            total += price
        print(f"Total bill: {total}")

    main()

#Task 12 :  distance conversion program
def task12():

    def meters_to_kilometers(meters):
        return meters / 1000

    def meters_to_miles(meters):
        return meters * 0.000621371

    def main():
        choice = input("Enter choice (1 for meters to kilometers, 2 for meters to miles): ")
        if choice == "1":
            meters = float(input("Enter distance in meters: "))
            print(f"Distance in kilometers: {meters_to_kilometers(meters)}")
        elif choice == "2":
            meters = float(input("Enter distance in meters: "))
            print(f"Distance in miles: {meters_to_miles(meters)}")
        else:
            print("Invalid choice")

    main()

#Task 13 :  BMI calculator
def task13():
    def calculate_bmi(weight, height):
        return weight / (height * height)

    def main():
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        bmi = calculate_bmi(weight, height)
        print(f"BMI: {bmi}")

    main()