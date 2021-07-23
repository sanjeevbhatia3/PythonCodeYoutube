def divide_num(a, b):
    try:
        output = a / b
    except (ZeroDivisionError, TypeError) as err:
        print(f"Some error occurs!")
        print(err)
    else:
        print(f'Division output of {a} divide by {b} is {output}')
    finally:
        print(f'divide_num function is executed!')


divide_num(3,0)