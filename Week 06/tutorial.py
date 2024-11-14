#part 1 - exercises on lists
#ex1 - managing a shopping list
def ex1():
    shopping_list = ['noodles', 'biscuts', 'rice', 'floor', 'yogurt']
    print('original list :',shopping_list)
    shopping_list.append('milk')
    shopping_list.append('orange')
    print('after adding 2 elements :',shopping_list)
    shopping_list.remove('milk')
    print('after removing elements :',shopping_list)
    
#ex2 - list statistics
def ex2():
    numbers = [23, 45, 12, 67, 34, 89, 10]
    print(numbers)
    sum_of_numbers = sum(numbers)
    print('sum of the list: ',sum_of_numbers)
    avg_of_numbers = sum_of_numbers / len(numbers)
    print('average of the numbers', avg_of_numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    print(f'minimum number is {minimum} and the maximum number is {maximum}')
    numbers.sort()
    print('ascending: ',numbers)
    numbers.sort(reverse=True)
    print("descending: ",numbers)
    
#Exercise 3: List Comprehensions
def ex3():
    squares = [x**2 for x in range(1, 21) if x % 3 == 0]
    print(squares)
    
#part 2
#Ex 1 - creating and using tuples
def ex3():
    student = (1, 'john', 21, CS)
    print(for i in student)
ex3()