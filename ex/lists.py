# # magicians = ['alice', 'david', "carolina"]
# # for magician in magicians:
# #     print(f"One of the name: {magician.title()}")
#
# cars = ["bmw", "audi", "porche"]
# for car in cars:
#     print(car)
#     print(f"I've favorite list of cars: cars[{cars}]")
#     print(f"My favorite car is {car}\n")
#
# pets = ['cat', 'dog', 'rabbit']
# for pet in pets:
#     print(f'A {pet} would make a great pet')
#     print('Any of these animals would make a great pet!\n')
#
# for value in range(0, 6):
#     print(value)
#
# numbers = list(range(1, 6))
# print(numbers)
#
# other_numbers = list(range(2, 12, 4))
# print(other_numbers)
#
# squares_of_numbers = []
# for value in range(1, 21):
#     square = value ** 2
#     squares_of_numbers.append(square)
#
# print(squares_of_numbers)
# print(len(squares_of_numbers))
#
# # intersing_number = list(range(1, 1000000))
# # for int_number in intersing_number:
# #     print(int_number)
# #
# # new_numbers = list(range(1, 1000000))
# # print(min(new_numbers))
# # print(max(new_numbers))
# # print(sum(new_numbers))
#
# next_numbers = []
# for n_number in range(1, 20, 2):
#     next_numbers.append(n_number)
#
# print(next_numbers)

# import turtle
# turtle.shape('turtle')
# turtle.shapesize(2)
# turtle.color('green')
# turtle.speed(1)
#
# for step_1 in range(6):
#     for step_2 in range(3):
#         turtle.forward(50)
#         turtle.left(360 / 3)
#     turtle.end_fill()
#
#     turtle.forward(50)
#     turtle.right(60)

# def code_of_cornate():
#     x = int(input('Enter your x: '))
#     y = int(input('Enter your y: '))
#
#     if x > 0 and y > 0:
#         print('You choose 1 area')
#     elif x < 0 and y > 0:
#         print('You choose 2 area')
#     elif x < 0 and y < 0:
#         print('You choose 3 area')
#     elif x > 0 and y < 0:
#         print('You choose 4 area')
#     else:
#         print('Restart your programm, please.')

numbers = list(range(3, 31, 3))
for number in numbers:
    print(number)


my_food = ['pizza', 'falafel', 'carrot', 'cake']
friend_foods = my_food[:]

print('My favorite food is: ')
print(my_food)

print('\nMy favorite\'s foods are (friend): ')
print(friend_foods)

favorive_cars = []
print('Enter your favorite car about 3 case: ')
for car in range(3):
    print(f'Enter your favorive car number {car+1} below: ')
    favorive_cars.append(input())
print(favorive_cars)

if favorive_cars[0] == ['BMW']:
    print('\tModel:\nX, Z, M')
