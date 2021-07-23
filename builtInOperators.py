# range
# start, stop, step
# for num in range(3,11,3):
#     print(num)
#
# num_list = list(range(1,51))
# print(num_list)

# enumerate
# name = 'mickey'
# for index, value in enumerate(name):
#     print(f'{value} is at index {index}')

# zip
# num = [1,2,3,4,5,6]
# character = ['a','b','c','d']
# name = ['john', 'jake', 'mike']
#
# for item in zip(num, character, name):
#     print(item)

# in
# num = [1,2,3,4,5]
# print(12 in num)

# name = {'first_name': 'john', 'last_name': 'oliver'}
# print('mike' in name.values())

# min, max
# num = [1,3,6,2,8,5,6]
# print(max(num))

# from random import randint
# i = 1
# while i <= 5:
#     random_num = randint(1,10)
#     print(random_num)
#     i += 1

# from random import choice
# names = ['john', 'mike', 'jake', 'sanj']
# for num in range(5):
#     print(choice(names))

# input
# name = input("Enter your name:")
# print("hello " + name)
#
# age = int(input("Enter your age:"))
# print(f'you are {age} years old.')

# sorted
my_list = [12,3,4,6,2,9,3,6]
print(sorted(my_list))