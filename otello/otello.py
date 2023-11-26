import numpy as np


def init_otello() -> np.ndarray:
    otello = np.empty(shape=(8, 8), dtype='object')
    for i in range(2):
        otello[3 + i, 3 + i] = False
        otello[4 - i, 3 + i] = True
    return otello

def print_otello(otello: np.ndarray):
    result = "    0  1  2  3  4  5  6  7\n"
    for i in range(8):
        result += " " + str(i) + " "
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

# def place_element(otello: np.ndarray, x: int, y: int, item: int) -> np.ndarray:
#     if x > 8 or x < 1 or y > 8 or y < 1:
#         print("Error: x and y must be in range [1, 8] !")
#         return otello
#     if otello[x, y] != 0:
#         print("Error ! You can't place an element here !")
#         return otello
# 
# def is_possible(otello: np.ndarray, x: int, y: int, item: bool) -> bool:
#     if otello[x, y] != None:
#         print("Error ! You can't place an element here !")
#         return False
#     enemy = not item
#     print(enemy)
#     match x:
#         case 0:
#             if otello[x + 1, y] == not item:
#                 return True
#             break
#         case 7:
#             if otello[x - 1, y] == not item:
#                 return True
#             break
#         case _:
#             if otello[x + 1, y] == not item or otello[x - 1, y] == not item:
#                 return True
#     match y:
#         case 0:
#             if otello[x, y + 1] == not item:
#                 return True
#             break
#         case 7:
#             if otello[x, y - 1] == not item:
#                 return True
#             break
#         case _:
#             if otello[x, y + 1] == not item or otello[x, y - 1] == not item:
#                 return True


def rotate_indices(x: int, y: int, size: int = 8):
    w = np.abs(y - size + 1)
    z = x
    return w, z

def verification(otello: np.ndarray, x: int, y: int, item: bool, diag: bool = False) -> bool:
    indice = 0
    mylist = []
    offset = y - x

    # Get the line to verify
    if diag:
        mylist = np.diagonal(otello, offset)
        if offset < 0:
            indice = x + offset
        else:
            indice = y - offset
    else:
        mylist = otello[x, :]
        indice = y

    # Browse in one direction if we meet other item
    for i in range(1, len(mylist) - indice):
        if mylist[indice + i] == None:
            break
        if mylist[indice + i] is item and i == 1:
            break
        if mylist[indice + i] is item and i > 1:
            return True
    # Browse in the other direction if we meet an item
    for i in range(1, indice + 1):
        if mylist[indice - i] == None:
            break
        if mylist[indice - i] is item and i == 1:
            break
        if mylist[indice - i] is item and i > 1:
            return True
    return False

def insert_diag(otello: np.ndarray, mylist, offset: int) -> np.ndarray:
    if offset < 0:
        for i in range(len(mylist)):
            otello[i - offset, i] = mylist[i]
    else:
        for i in range(len(mylist)):
            otello[i, i + offset] = mylist[i]
    return otello

def update_otello(otello: np.ndarray, x: int, y: int, item: bool, diag: bool = False) -> np.ndarray:
    indice = 0
    mylist = []
    offset = y - x

    # Get the line to verify
    if diag:
        mylist = list(np.diagonal(otello, offset))
        if offset < 0:
            indice = x + offset
        else:
            indice = y - offset
    else:
        mylist = list(otello[x, :])
        indice = y
    for i in range(1, len(mylist) - indice):
        if mylist[indice + i] == None:
            break
        if mylist[indice + i] is item and i == 1:
            break
        if mylist[indice + i] is item and i > 1:
            for j in range(i):
                mylist[indice + i - j] = item
            break
    for i in range(1, indice + 1):
        print(indice - i)
        if mylist[indice - i] == None:
            break
        if mylist[indice - i] is item and i == 1:
            break
        if mylist[indice - i] is item and i > 1:
            for j in range(i):
                mylist[indice - i + j] = item
            break
    if diag:
        otello = insert_diag(otello, mylist, offset)
    else:
        otello[x, :] = mylist
    return otello
# print(verification([[True, None True], [False, True, False]], 
    
def is_possible(otello: np.ndarray, x: int, y: int, item: bool) -> bool:
    if otello[x, y] != None:
        return False
    w, z = rotate_indices(x, y)
    if verification(otello, x, y, item) or verification(otello, x, y, item, True):
        return True
    otello = np.rot90(otello, 1)
    if verification(otello, w, z, item) or verification(otello, w, z, item, True):
        otello = np.rot90(otello, -1)
        return True
    otello = np.rot90(otello, -1)
    return False


def place_element(otello: np.ndarray, x: int, y: int, item: bool) -> np.ndarray:
    if is_possible(otello, x, y, item):
        print("It's possible")
        otello[x, y] = item
        w, z = rotate_indices(x, y)
        otello = update_otello(otello, x, y, item)
        otello = update_otello(otello, x, y, item, True)
        otello = np.rot90(otello, 1)
        otello = update_otello(otello, w, z, item)
        otello = update_otello(otello, w, z, item, True)
        otello = np.rot90(otello, -1)
    else:
        print("It's not possible")
    return otello

def win_otello(otello: np.ndarray) -> bool:
    # Count number of True
    player_1 = len(otello[otello == True])
    # Count number of False.
    player_2 = len(otello[otello == False])
    # Return the winner
    if player_1 > player_2: return True
    return False

def list_possibilities(otello: np.ndarray, item: bool) -> list[tuple[int, int]]:
    result = []
    for i in np.arange(8):
        for j in np.arange(8):
            if is_possible(otello, i, j, item):
                result.append((i, j))
    return result

def play_otello():
    otello = init_otello()
    item = False
    print_otello(otello)
    possibilities = list_possibilities(otello, item)
    while len(possibilities) != 0:
        if item:
            print("'x' must play")
        else:
            print("'o' must play")
        possibilities = list_possibilities(otello, item)
        print("Possibilities: " + str(possibilities))
        try:
            x = int(input("Row: "))
            y = int(input("Column: "))
            if is_possible(otello, x, y, item):
                otello = place_element(otello, x, y, item)
                item = not item
                print_otello(otello)
        except ValueError:
            print("You must enter a digit !")
    if win_otello(otello):
        print("'x' win")
    else:
        print("'o' win")



play_otello()

# a = np.arange(16).reshape(4, 4)
# print(a)
# print(np.diagonal(a, -1))
# print(insert_diag(a, np.diagonal(a, -1), -1))

