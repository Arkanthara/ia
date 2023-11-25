import numpy as np

from morpion import Morpion

morpion = Morpion()

print(morpion)

def MinMax(morpion: Morpion, current: np.ndarray, depth: int, max_depth: int = 10, minmax: bool = True) -> int:
    if morpion.win(current) != 0:
        if minmax: return 1
        else: return -1
    if depth < max_depth:
        possibilities = morpion.list_possibilities(current)
        evaluation_table = np.zeros(len(possibilities))
        if len(possibilities) == 0: return 0
        for i in range(len(possibilities)):
            evaluation_table[i] = MinMax(morpion, possibilities[i], depth + 1, minmax= not minmax)
        if minmax:
            return np.max(evaluation_table)
        else:
            return np.min(evaluation_table)
    else:
        return 0
def PlayMinMax(morpion: Morpion, max_depth: int = 15):
    possibilities = morpion.list_possibilities(morpion.grid)
    evaluation_table = [0 for i in range(len(possibilities))]
    for i in range(len(possibilities)):
        evaluation_table[i] = MinMax(morpion, possibilities[i], 1, max_depth, False)
    return possibilities[evaluation_table.index(max(evaluation_table))]


def MinMaxVSMinMax(max_depth_1: int, max_depth_2: int):
    morpion = Morpion()

print(PlayMinMax(morpion))

#TODO change list possibilites because execution time too long !
