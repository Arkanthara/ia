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

graph = build_graph(10, 0.3)

def visualize_graph(datapoints: list[tuple[float]], graph: dict[int, list[int]]) -> None:
    for i in datapoints:
        plt.plot(i[0], i[1], 'mo')
    for i in graph.keys():
        for j in graph.get(i):
            plt.plot([datapoints[i][0], datapoints[j][0]], [datapoints[i][1], datapoints[j][1]], 'c-')
    plt.show()

visualize_graph(sample_datapoints(10), graph)

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

print(shortest_path_length_bfs(graph, 2, 7))

def DLS(graph: dict[int, list[int]], start: int, goal: int, limit: int) -> bool:
    if (start == goal): return True;
    if (limit <= 0): return False;
    for i in graph[start]:
        if DLS(graph, i, goal, limit - 1): return True;
    return False;

def IDDFS(graph: dict[int, list[int]], start: int, goal: int, limit: int) -> int:
    for i in range(limit):
        if DLS(graph, start, goal, i): return i;

print(IDDFS(graph, 2, 7, 10))
