# Solution for programming assignment 4, problem 1.
# For Cmpsc 465
# with Professor Mingfu Shao
# Group:
# Carson Forsyth; cjf5729@psu.edu
# Olajide Ogun; oxo5057@psu.edu
# Agha Arib Hyder; aah5469@psu.edu
# Praharsh Verma; pbv5036@psu.edu

import sys

inp_list = [int(vertex) for vertex in input().split(" ") if vertex.isdigit()]


n, m, s = inp_list[0], inp_list[1], inp_list[2]
edges = []
dp_table = []
for edge in range(0, m):
	edges.append([0]*3)
	
for vertex in range(0, n):
	dp_table.append([sys.maxsize]*n)
	

for line in range(m):
	inp = input()
	edges[line][0], edges[line][1], edges[line][2] = [int(num) for num in inp.split(" ")]

contains_negative_cycle = False
dp_table[0][s-1] = 0
for row in range(1, n):
	for column in range(0, n):
		dp_table[row][column] = dp_table[row-1][column]
		for edge in edges:
			if edge[1]-1 == column:
				if dp_table[row][column] > dp_table[row-1][edge[0]-1] + edge[2]:
					if row == n-1:
						contains_negative_cycle = True
					dp_table[row][column] = dp_table[row - 1][edge[0]-1] + edge[2]

print(contains_negative_cycle)
