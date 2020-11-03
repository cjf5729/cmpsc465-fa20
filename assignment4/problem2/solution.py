# Solution for programming assignment 4, problem 2.
# For Cmpsc 465
# with Professor Mingfu Shao
# Group:
# Carson Forsyth; cjf5729@psu.edu
# Olajide Ogun; oxo5057@psu.edu
# Agha Arib Hyder; aah5469@psu.edu
# Praharsh Verma; pbv5036@psu.edu

input_string = input()
n = len(input_string)
# init dp table
dp_table = []
for row in range(n):
    this_row = []
    for column in range(n):
        if row == column:
            this_row.append(1)
        else:
            this_row.append(0)
    dp_table.append(this_row)
# fill out from bottom to top, table not needed below F(i,i)
for row in reversed(range(n-1)):
    for column in range(row+1, n):
        if input_string[row] == input_string[column]:
            dp_table[row][column] = dp_table[row+1][column-1] + 2
        else:
            dp_table[row][column] = max(dp_table[row+1][column], dp_table[row][column-1])
print(dp_table[0][n-1])
