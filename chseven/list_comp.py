# # Double prize weekend money bonanza

# prizes = [5, 10, 50, 100, 1000]


# dbl_prizes = []

# for prize in prizes:
#     dbl_prizes.append(prize * 2)

# print(dbl_prizes)


# # comprehension method

# dbl_prizes = [prize * 2 for prize in prizes]
# print(dbl_prizes)

# # Squaring of Numbers

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squared_even_nums = []

# for num in nums:
#     if (num ** 2) % 2 == 0:
#         squared_even_nums.append(num ** 2)
# print(squared_even_nums)


# # comprehension method

# squared_even_nums = [num ** 2 for num in nums if(num ** 2 ) % 2 == 0]
# print(squared_even_nums)

nums = [2, 4, 6, 8, 10]

doubled = []

for num in nums:
    doubled.append(num ** 2)
print(doubled)

doubled = [num ** 2 for num in nums]
print(doubled)

marks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]

even_marks = []

for mark in marks:
    if (mark ** 2 ) % 2 == 0:
        even_marks.append(mark)
print(even_marks)


even_marks = [mark ** 2 for mark in marks if (mark  ** 2) % 2 == 0]
print(even_marks)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate over each number in the list
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        # Print the square of the even number
        print(num ** 2)
