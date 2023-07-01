grades = ['A', 'B', 'C', 'D', 'E', 'F', 'F', 'E']

def failed_grades(grade):
    return grade != 'F'

# print(list(filter(failed_grades, grades)))
# failed_grades = []

# for grade in grades:
#     if grade != 'F':
#         failed_grades.append((grade))
# print(failed_grades)

print ([grade for grade in grades if grade != 'F'])
