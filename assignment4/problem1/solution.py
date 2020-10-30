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

for vertex in range(0, n):
	dp_table.append([sys.maxsize]*n)
	edges.append([])

for line in range(m):
	inp = input()
	outV, inV, edgeDist = [int(num) for num in inp.split(" ")]
	edges[inV - 1].append([outV-1, edgeDist])

contains_negative_cycle = False
dp_table[0][s-1] = 0
for row in range(1, n):
	for column in range(0, n):
		dp_table[row][column] = dp_table[row-1][column]
		for edge in edges[column]:
			# edge will be an in edge of vertex column.
			if dp_table[row][column] > dp_table[row - 1][edge[0]] + edge[1]:
				if row == n - 1:
					contains_negative_cycle = True
				dp_table[row][column] = dp_table[row - 1][edge[0]] + edge[1]

print(contains_negative_cycle)
