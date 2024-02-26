def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(str(num) for num in row).center(len(triangle) * 2))

rows = 5
triangle = generate_pascals_triangle(rows)
print_pascals_triangle(triangle)
 