operation = str(input("enter the operation(+,-,*,/) :"))
first_num = int(input("enter the first number :"))
second_num = int(input("enter the second number :"))

answe=0

if operation == "+":
    answer = first_num + second_num
elif operation == "-":
    answer = firsy_num - second_num
elif operation == "/":
    answer = first_num / second_num
elif operation == "*":
    answer = first_num * second_num
else:
    print("please check your inputs")

print('your answer is ',answer)
