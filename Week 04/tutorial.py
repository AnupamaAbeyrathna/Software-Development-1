#simple Questions
#task 1
#printing numbers with for loop
def task1():
    for i in range(6):
        print(i)
#task 2
#Counting Down with a While Loop
def task2():
    i = 5
    while i > 0:
        print(i)
        i -= 1

#task 3
#Simple Sum with a while loop
def task3():
    i = 0
    total = 0
    while i < 5:
        total += i
        i += 1
    print(total)

#moderate questions
#task 4
#sum of even numbers
def task4():
    total = 0
    for i in range(0, 10, 2):
        total += i
        print(total)

#task 5
#user inout loop
def task5():
    total = 0
    while True:
        userInput = int(input("Enter a number: "))
        if userInput >= 0:
            total += userInput
        else:
            break
    print(total)

#task 06
#Multiplication Table
def task6():
    number = int(input("Enter a number to get the multiplication table : "))
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)
  
#task 07
#factorial calculation
def task7():
    number = int(input('enter number to find factorial :'))
    result = 1
    if number <= 0:
        print("invalid input")
    else:
        while number > 1:
            result *= number
            number -= 1
    print(result)

#task 08
#Prime numbers
def task8():
    for j in range(2,21):
        for i in range(2, int(j ** 0.5) + 1):
            if j % i == 0:
                break
        else:
            print(j)
        
        
def task9():
    for i in range(1):
        count = 0
        while count < 5:
            count +=1
            count_str = str(count)
            print(count_str*count)
    
task7()