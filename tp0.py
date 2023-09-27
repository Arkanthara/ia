import random
import numpy as np
import matplotlib.pyplot as plt

def sample_datapoints(n: int) -> list[tuple[float]]:
    result = [];
    for i in np.arange(n):
        x = random.randint(-10000, 10000)/10000
        y = random.randint(-10000, 10000)/10000
        tmp = (x, y)
        result.append(tmp)
    return result

def build_graph(n: int, connec_factor: float) -> dict[int, list[int]]:
    vertex = sample_datapoints(n)
    result = dict()
    for i in np.arange(len(vertex)):
        tmp = []
        for j in np.arange(len(vertex)):
            if i > j and i in result.get(j):
                tmp.append(j)
            elif np.random.binomial(1, connec_factor) and i < j:
                tmp.append(j)
        result[i] = tmp
    return result

graph = build_graph(5, 0.5)

def visualize_graph(datapoints: list[tuple[float]], graph: dict[int, list[int]]) -> None:
    for i in datapoints:
        plt.plot(i[0], i[1], 'mo')
    for i in graph.keys():
        for j in graph.get(i):
            plt.plot([datapoints[i][0], datapoints[j][0]], [datapoints[i][1], datapoints[j][1]], 'c-')
    plt.show()

visualize_graph(sample_datapoints(5), graph)

def shortest_path_length_bfs(graph: dict[int, list[int]], start: int, goal: int) -> int:
    visited = []
    tab = []
    tab.append(start)
    tovisit = []
    path_length = 1
    while (len(tab) != 0):
        vertex = tab.pop(0)
        for i in graph[vertex]:
            if (i not in visited):
                visited.append(i)
                if (i == goal):
                    print("Success")
                    return path_length
                tovisit.append(i)
        if (len(tab) == 0 and len(tovisit) != 0):
            tab = tovisit.copy()
            tovisit = []
            path_length += 1
    print("Failure")
    return -1

print(shortest_path_length_bfs(graph, 2, 4))


# def shortest_path_length_dfs(graph: dict[int, list[int]], start: int, goal: int) -> int:
#     tab = []
#     visited = []
#     tab.append(start)
#     while (len(tab) != 0):
#         vertex = tab.pop(0)
#         for i in graph[vertex]:
#             if i not in visited:
#                 visited.append(i)
#                 if (i == goal):
#                     print("Success")
#                     return 0
#                 tab.insert(0, i)
#     print("Failure")
#     return -1
# shortest_path_length_dfs(graph, 2, 4)

var = 0

def dfs(graph: dict[int, list[int]], start: int, goal: int, visited: list[int], path: int) -> int:
    if (start == goal):
        print("Success: path_length=" + str(path))
        return path
    visited.append(start)
    for i in graph[start]:
        if (i not in visited):
            return dfs(graph, i, goal, visited, path + 1)

print(dfs(graph, 2, 4, [], 0))

def shortest_path_length_dfs(graph: dict[int, list[int]], start: int, goal: int) -> int:
    return dfs(graph, start, goal, [], 0)

print(shortest_path_length_dfs(graph, 2, 4))

def dfs_2(graph: dict[int, list[int]], start: int, goal: int) -> list[int]:
    if (start == goal):
        return start
    explored = []
    tab = []
    tab.append(start)
    while (len(tab) != 0):
        vertex = tab.pop(0)
        explored.append(vertex)
        for i in graph[vertex]:
            if (i not in explored):
                if i == goal: return i
                tab.append(i)
    return -1
def dfs(graph, start, target, path = [], visited = set()):
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for neighbour in graph[start]:
        if neighbour not in visited:
            result = dfs(graph, neighbour, target, path, visited)
            if result is not None:
                return result
    path.pop()
    return None
        
print(dfs(graph, 2, 4))
# def shortest_path_length_bfs(graph: dict[int, list[int]], start: int, goal: int) -> int:
#     tab = []
#     visited = []
#     tab.append(start)
#     while (len(tab) != 0):
#         vertex = tab.pop(0)
#         for i in graph[vertex]:
#             if i not in visited:
#                 visited.append(i)
#                 if (i == goal):
#                     print("Succes")
#                     return -1
#                 tab.append(i)
#     return -1
# shortest_path_length_bfs(build_graph(5, 0.5), 2, 4)
