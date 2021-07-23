# def say_hello(name="John"):
#     print("Hello " + name)
#
# say_hello("Jake")

# def add_num(a=2, b=5):
#     return a + b
#
# num_sum = add_num()
# print(num_sum)

# def even_odd(num):
#     if num % 2 == 0:
#         print("Given number is even")
#     else:
#         print("Given number is odd")
#
# even_odd(8)


# inventory = [('macbook', 5), ('tablet', 20), ('chromebook', 7), ('iPad', 4), ('iPhone', 10)]
# def inventory_check(inventory):
#     max_inventory_item = ""
#     current_inventory = 0
#     for item, num in inventory:
#         if num > current_inventory:
#             current_inventory = num
#             max_inventory_item = item
#     return max_inventory_item, current_inventory
#
# result = inventory_check((inventory))
# print(result)

# def full_name(first_name, last_name):
#     return first_name + " " + last_name
#
# name = full_name("John", "Oliver")
#
# def person_info(given_name=name):
#     age = 53
#     print(f'{given_name} is {age} years old.')
#
# person_info('Mike')

# *args and **kwargs
# def num_sum(*args):
#     print(sum(args))
#
# num_sum(1,2,3,4,5,3,4,5,5,6,6,6)

def fav_color(**kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}.'.format(kwargs['color']))
    else:
        print('I did not find any color')

fav_color(rose='red', juice='orange', color='brown')


total = 0
def number():
    global total
    total = 2
    total += 1
    print(total)

number()
print(total)