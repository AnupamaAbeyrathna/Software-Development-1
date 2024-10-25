#get a random number between 0 - 100 until number is 0
#if number is 7 print 'lucky 7!'
#can't use continuous loop or break
import random

loop = True
times = 0

while loop:
    number = random.randint(0, 10)
    times += 1
    print(times,"-",number)
    if number == 0:
        loop = False
    elif number == 7:
        print('---lucky 7!---')
        