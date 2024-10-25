import math

#task 01 Calculate Expressions
print('-----------------------------------------------')
print(8+2*5)
x = (8+2)
print(x*5)
print(20//3)
print(20%3)
print(2**3)
print('-----------------------------------------------')

#task 02 Variable Assignments
print('-----------------------------------------------')
a = 10+5
b = 30
b += 5
print(b)
print('-----------------------------------------------')

#task 03 Using Arithmetic Assignment Operators
print('-----------------------------------------------')
x = 10
x += 5
x *= 3
x -= 2
x /= 4
print(x)
print('-----------------------------------------------')

#task 04 Identify Data Types
print('-----------------------------------------------')
print(type(42))
print(type(3.14))
print(type(True))
print(type("hello,world!"))
print('-----------------------------------------------')

#task 05 Converting Data Types
print('-----------------------------------------------')
x = "123"
x = int(x)
print(x+10)

apples = 50
apples = str(apples)
print(apples+" apples")

num = 3.9
num = int(num)
print(type(num))
print('-----------------------------------------------')


#guided practice
#task 01 area of a circle
print('-----------------------------------------------')
radius = int(input("enter the radius : "))
circle_area = math.pi*radius**2
print(f"the area of the circle is {circle_area}")
print('-----------------------------------------------')

#task 02 Salary Increase Calculator
print('-----------------------------------------------')
current_salary = int(input("what is the current salary : "))
precentage = int(input("what is the increase precentage (%) : "))
increase = current_salary*precentage/100
new_salary = current_salary + increase
print("increased salary is :" , new_salary)
print('-----------------------------------------------')

#task 03 Volume of a Cylinde
print('-----------------------------------------------')
print("Volume of a Cylinde")
radius = int(input('enter the radius :'))
height = int(input('enter the height :'))

volume = math.pi * height * radius ** 2
print("the volume of the cylinder is " , volume)
print('-----------------------------------------------')

#task 04 Cuboid Area, Perimeter, and Volume Calculator
print('-----------------------------------------------')
print("Cuboid Area, Perimeter, and Volume Calculator")

length = int(input('enter the length :'))
width = int(input('enter the width :'))
height = int(input('enter the height :'))

surface_area = 2*(length*width + width*height + height*length)
perimeter = (width + length)*2
volume = width*length*height

print(f"surface area is {surface_area}")
print(f"perimeter is {perimeter}")
print(f"volume is {volume}")
print('-----------------------------------------------')




