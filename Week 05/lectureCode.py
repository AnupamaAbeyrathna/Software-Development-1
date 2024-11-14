def question01():
    for i in range(1,11):
        print(i,'-',i**2)
        
def question02():
    import random
    number = random.randint(0,5)
    count = 1
    guess = None
    while guess != number:
        guess = int(input("guess the number between 0, 100: "))
        count+=1
        if guess < number:
            print("too low")
        elif guess > number:
            print('too high')
        elif guess == number:
            print("correct!")
            print(f"correct in {count} times")
        

def question03():
    import random
    number = random.randint(0,100)
    count = 1
    while True:
        guess = int(input('guess the number (0,100):'))
        if guess < number:
            print("too low")
        elif guess > number:
            print('too high')
        elif guess == number:
            print("correct!")
            print(f"correct in {count} times")
            break
        count+=1
        
def question04():
    correct_password = "python123"
    while True:
        password = input("enter the password : ")
        if password == correct_password:
            print('correct password!')
            break
        else:
            print("incorrect password!")
        
def question05():
    for i in range(1,11):
        if i % 3 == 0:
            continue
        else:
            print(i)
        
question05()
'''variable = None
print(type(variable))'''
