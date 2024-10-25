#simple exercise
#task01 if statements
num1 = int(input("enter the number to check if the number is divisable by 5 :"))
mod = num1 % 5
if mod == 0:
    print("Divisible by 5")
    
#task02 Else statements
age = int(input("enter the age :"))
if age >= 18:
    print("eligible for vote")
else:
    print("not eligible for vote")
    
#task03 elif statements
num = int(input("enter the number (positive,negative, or 0):"))
if num > 0:
    print("positive number")
elif num ==0:
    print('number is 0')
else:
    print("negative number")
    
#task04 nested if
num4 = int(input("enter the number (odd,even):"))
if num4 < 10:
    print("number is less that 10")
    oddoreven = num4 % 2
    if oddoreven == 0:
        print("number is even number")
    else:
        print("number is odd number")
else:
    print('number is not greater than 10')
    
#task05 leap year
year = int(input("enter the year to check if it's a leap year :"))
leapornot = year % 4
if leapornot == 0:
    print("it's a leap year")
else:
    print("it's not a leap year")
    
#task06 vowel or not
character = input("enter a character (vowel check):").lower()
vowels = ["a","e","i","o","u"]

if character in vowels:
    print("it's a vowel")
else:
    print("not a vowel")
    
#task07 categorizer
import string    

character = input("enter a character (upper,lower,digit,special):")

if character in string.ascii_uppercase:
    print("upper character")
elif character in tring.ascii_lowercase:
    print("lower character")
elif character in tring.digits:
    print("digit character")
elif character in string.punctuation:
    print("special character")
else:
    print("wrong input")

#task08
amount = int(input("enter the purchase amount :"))
if amount > 1000:
    print("eligible for 10% discount")
    discount = amount / 10
    final = amount - discount
    print("final amount is ", final)

    

    
