'''
my_list = [1, 2, 3, 4]
my_list.insert(2, 'new')  # Insert 'new' at index 2
print(my_list)  # Output: [1, 2, 'new', 3, 4]

my_list = [1, 2, 3, 4]
my_list.remove(3)  # Remove the item with value 3
print(my_list)  # Output: [1, 2, 4]

my_list = [1, 2, 3, 4]
del my_list[1]  # Delete the item at index 1
print(my_list)  # Output: [1, 3, 4]

my_list = [1, 2, 3, 4]
removed_item = my_list.pop(1)  # Remove item at index 1
print(my_list)  # Output: [1, 3, 4]
print(removed_item)  # Output: 2

my_list = [1, 2, 3, 4]
my_list[2] = 'changed'  # Change the item at index 2
print(my_list)  # Output: [1, 2, 'changed', 4]

def average(num1, num2):
    avg = num1/num2
    print(avg)
    return avg

average(20,5)'''

numbers = (32, 56, 92, 35, 46, 76)
print(sum(numbers))