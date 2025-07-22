def generate(numRows):
    triangle = []

    for row_num in range(numRows):
        row = [1] * (row_num + 1)  # initialize with 1s

        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)

    return triangle
