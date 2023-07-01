# def greet(time, name, year):
#     print(f'Good {time} {name}; hope you are well and where are you going after the {year} election?')

# time = input('Enter the time of the day: ')
# name = input('Enter your name: ')
# year = int(input('Enter the year: '))

# greet('morning', 'Kolawole', 2023)



# def area(radius):
#     return 3.142 * radius * radius


# def vol(area, length):
#     print(area * length)

# radius = int(input('Enter the radius of the circle: '))
# length = int(input('Enter the length of the cylinder: '))

# area_calc = area(radius)

# vol(area_calc, length)



# Write a function that calculate the volume of a cylinder

def area(radius):
    return 3.142 * radius * radius

def volume(area, length):
    print(area * length)

radius = int(input('Kindly input the radius of the circle: '))
length = int(input('Kindly input the length of the cylinder: '))

volume(area(radius), length)


