
def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

# def check(dictionary):
#     for keys, val in dictionary.items():
#         print(f'I am {keys}, I am having {val} belt.')


kolawole_belts = {}

while True:
    kolawole_name = input("Enter your name: ")
    kolawole_belt = input("Enter your belt colour: ")
    kolawole_belts[kolawole_name] = kolawole_belt

    another = input('You wanna enter another? y/n ')

    if another == 'y':
        continue
    else:
        break

belt_count(kolawole_belts)