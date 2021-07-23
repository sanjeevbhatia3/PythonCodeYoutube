# class car_package:
#     color = 'blue'
#
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#
#     def car_description(self, battery):
#         print(f'I love my {self.make} and its color is {car_package.color}')
#         print(f'Car has a battery of {battery}')
#
#
# my_car1 = car_package(make="Tesla", model="Model-X")
# # print(my_car1.make)
# my_car2 = car_package("Tesla", "Model 3")
# # print(my_car2.model)
# # print(my_car1.color)
# # print(my_car2.color)
# my_car1.car_description("75kWh")


# Inheritance
class Car:
    def __init__(self):
        print(f'Car class created')

    def music_system(self):
        print(f'Car has BOSS music system')

    def tire_brand(self):
        print(f'Car comes with Bridgestone tires')


class Tesla(Car):
    def __init__(self):
        Car.__init__(self)
        print(f'Tesla class created')

    def color(self):
        print(f'car color is blue')

    def music_system(self):
        print(f'Car has Harman-Kardon music system')


my_car = Tesla()
my_car.color()
my_car.music_system()
my_car1 = Car()
my_car1.music_system()

