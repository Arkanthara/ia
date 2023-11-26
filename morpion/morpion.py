import numpy as np



def init_otello() -> np.ndarray:
    otello = np.empty(shape=(3, 3), dtype='object')
    return otello

def print_otello(otello: np.ndarray):
    result = "    0  1  2\n"
    for i in range(3):
        result += " " + str(i) + " "
        for j in range(3):
            match otello[i, j]:
                case None:
                    result += " - "
                case 0:
                    result += " o "
                case 1:
                    result += " x "
        result += "\n"
    print(result)


def who_should_play(morpion: np.ndarray, begin: bool) -> bool:
    count = np.sum(morpion[morpion != None])
    if count % 2 == 1:
        if begin: return not begin
        else: return begin
    else:
        return begin

def is_possible(morpion: np.ndarray, x: int, y: int, item: bool) -> bool:
    if morpion[x, y] != None:
        return False
    return True

def test_win(morpion: np.ndarray, item: bool):
    diag = np.diagonal(moprion)
    for i in range(3):
        if len(morpion[morpion == item]) == 3:
            return item
    if len(diag[diag == item]) == 3:
        return item
    return not item

def list_possibilities(morpion: np.ndarray, item: bool) -> list[tuple[int, int]]:
    for i in range(3):
        for j in range(3):
            if is_possible(morpion, i, j, item):

