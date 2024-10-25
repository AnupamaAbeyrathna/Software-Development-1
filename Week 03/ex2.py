import random

for i in range(0,9):
    number = random.randint(0,10)
    if number == 7:
        print('lucky 7')
    else:
        print(number)