# Write a function that calculate the perimeter of a rectangle choosing the length and breath that you prefer

def perimeter(length, breath):
    answer = 2 * (length * breath )
    return answer

output =  perimeter(5, 4)
print(f'The perimeter of the rectangle for the inputed length and breadth is: {output}cm')
