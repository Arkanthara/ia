import numpy as np


def init_otello() -> np.ndarray:
    otello = np.empty(shape=(8, 8), dtype='object')
    for i in range(2):
        otello[3 + i, 3 + i] = 0
        otello[4 - i, 3 + i] = 1
    return otello

def print_otello(otello: np.ndarray):
    result = ""
    for i in range(8):
        for j in range(8):
            match otello[i, j]:
                case None:
                    result += " - "
                case 0:
                    result += " o "
                case 1:
                    result += " x "
        result += "\n"
    print(result)

def place_element(otello: np.ndarray, x: int, y: int, item: int) -> np.ndarray:
    if x > 8 or x < 1 or y > 8 or y < 1:
        print("Error: x and y must be in range [1, 8] !")
        return otello
    if otello[x, y] != 0:
        print("Error ! You can't place an element here !")
        return otello
'''
def is_possible(otello: np.ndarray, x: int, y: int, item: bool) -> bool:
    if otello[x, y] != None:
        print("Error ! You can't place an element here !")
        return False
    enemy = not item
    print(enemy)
    match x:
        case 0:
            if otello[x + 1, y] == not item:
                return True
            break
        case 7:
            if otello[x - 1, y] == not item:
                return True
            break
        case _:
            if otello[x + 1, y] == not item or otello[x - 1, y] == not item:
                return True
    match y:
        case 0:
            if otello[x, y + 1] == not item:
                return True
            break
        case 7:
            if otello[x, y - 1] == not item:
                return True
            break
        case _:
            if otello[x, y + 1] == not item or otello[x, y - 1] == not item:
                return True
'''

def verification(otello: np.ndarray, x: int, y: int, item: bool, diag: bool = False) -> bool:
    indice = 0
    mylist = []
    offset = x - y

    # Get the line to verify
    if diag:
        mylist = np.diagonal(otello, offset)
        indice = y - np.abs(offset)
    else:
        mylist = otello[x, :]
        indice = y

    # Calculate index of 
    if indice < 0:
        indice += len(mylist)

    for i in range(len(mylist) - indice):
        if diag_1[i] == None:
            break
        if diag_1[i] == item:
            return True
    for i in range(indice):
        if diag_1[i] == None:
            break
        if diag_1[i] == item:
            return True
    return False


def is_possible(otello: np.ndarray, x: int, y: int, item: bool) -> bool:
    a = np.arange(16).reshape(4, 4);
    offset = x - y
    diag_1 = np.diagonal(a, offset)

    indice = y - np.abs(offset)
    print(indice)
    print(diag_1[indice])
    print(a)

    return True


otello = init_otello()
print_otello(otello)


print(is_possible(otello, 3, 1, False))
