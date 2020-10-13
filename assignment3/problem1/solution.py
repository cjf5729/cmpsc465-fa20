# Solution for programming assignment 3, problem 1.
# For Cmpsc 465
# with Professor Mingfu Shao
# By Carson Forsyth; cjf5729@psu.edu
# Olajide Ogun; oxo5057@psu.edu
# Agha Arib Hyder; aah5469@psu.edu
from typing import List


# Declare global variables.
num_connected = 0
post_list: List[int] = []
visited_vertices = []


# 
def dfs(adjacency_list, num_vert, explore_order):
    global visited_vertices
    global num_connected
    global post_list
    num_connected = 0
    visited_vertices = [-1] * num_vert
    post_list = []
    
    for vertex in explore_order:
        if visited_vertices[vertex] == -1:
            num_connected += 1
            explore(adjacency_list, vertex, num_vert)
    return


def explore(adjacency_list, vertex, num_vert):
    global post_list
    global num_connected
    global visited_vertices
    visited_vertices[vertex] = num_connected
    
    for edge in adjacency_list[vertex]:
        if visited_vertices[edge] == -1:
            explore(adjacency_list, edge, num_vert)
    
    post_list.append(vertex)
    return


def get_post_list():
    return post_list


def get_connected():
    return num_connected


inp_list = [int(vertex) for vertex in input().split(" ") if vertex.isdigit()]

numV, numE = inp_list[0], inp_list[1]

# Create an adjacency list and store the transpose of the graph within.
adjacency_list = [[]]*numV
reverse_adjacency_list = [[]]*numV
for edge in range(numE):
    vertex1, vertex2 = [int(vertex) for vertex in input().split(" ") if vertex.isdigit()]
    if not adjacency_list[vertex1-1]:
        adjacency_list[vertex1-1] = [vertex2-1]
    else:
        adjacency_list[vertex1-1].append(vertex2-1)
    if not reverse_adjacency_list[vertex2-1]:
        reverse_adjacency_list[vertex2-1] = [vertex1-1]
    else:
        reverse_adjacency_list[vertex2-1].append(vertex1-1)

dfs(reverse_adjacency_list, numV, range(numV))
post_order = get_post_list()
post_order.reverse()

dfs(adjacency_list, numV, post_order)
print(get_connected())
