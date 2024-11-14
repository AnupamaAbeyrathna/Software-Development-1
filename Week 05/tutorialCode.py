
#exercise 2 - simple looping program
def ex1():
    import random
    count = 1
    while True:
        count += 1
        num = random.randint(1, 100)
        print(f"number {count} is {num}")
        if num == 0:
            break
        elif num == 7:
            print("Lucky 7!")

#exercise 3 - number guessing game
def ex2():
    import random
    num = random.randint(1, 100)
    guess = 0
    count = 0
    while guess != num:
        count += 1
        guess = int(input("Enter a number: "))
        if guess < num:
            print("Too low")
        elif guess > num:
            print("Too high")
        else:
            print(f"Correct! It took you {count} tries.")

ex2()

#exercise 4 - lap time recorder
def ex3():
    lap_times = int(input("How many lap times would you like to enter? "))
    total_time = 0

    
    fastest = None
    slowest = None

    for i in range(1, lap_times + 1):
        time = float(input(f"Enter time for lap {i} of {lap_times}: "))

        
        if fastest is None or slowest is None:
            fastest = time
            slowest = time
        else:
            
            if time < fastest:
                fastest = time
            if time > slowest:
                slowest = time

        total_time += time


    print(f"Fastest time: {fastest}")
    print(f"Slowest time: {slowest}")
    print(f"Average time: {round(total_time / lap_times, 2)}")