# kolawoles = ['Ayodeji', 'Emmanuel', 'Ayobami', 'Damilola']

# for kolawole in kolawoles:
#     print(kolawole)

# for kolawole in kolawoles[1:3]:
    # print(kolawole)

# for kolawole in kolawoles:
#         if kolawole == 'Ayobami':
#             print(f'{kolawole} - black belt')
#         else:
#             print(kolawole)


# fruits = ['mango', 'cashew', 'orange', 'pineapple', 'pawpaw']

# for fruit in fruits:
#     if fruit == 'pineapple':
#         print(f'{fruit}: This is my favourite fruits of all')
#         break
#     else:
#         print(fruit)

age = 25
num = 0

while num < age:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num += 1
