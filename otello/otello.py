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
        otello[x, y] = item
        w, z = rotate_indices(x, y)
        otello = update_otello(otello, x, y, item)
        otello = update_otello(otello, x, y, item, True)
        otello = np.rot90(otello, 1)
        otello = update_otello(otello, w, z, item)
        otello = update_otello(otello, w, z, item, True)
        otello = np.rot90(otello, -1)
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

def minmax(otello: np.ndarray, path: int, Max_depth: int, item: bool, Max: bool) -> int:
    possibilities = list_possibilities(otello, item)
    if len(possibilities) == 0:
        if Max:
            if win_otello(otello) == item: return 1
            else return -1
        else:
            if win_otello(otello) == item: return -1
            else return 1
    evaluation = np.zeros(len(possibilities))
    if path <= Max_depth:
        for i in range(len(possibilities)):
            x, y = possibilities[i]
            newotello = place_element(otello.copy(), x, y, item)
            evaluation[i] = minmax(newotello, path + 1, Max_depth, not item, not Max)
        if Max:
            return np.max(evaluation)
        return np.min(evaluation)
    return 0
        
def play_minmax(otello: np.ndarray, max_depth, item) -> np.ndarray:
    possibilities = list_possibilities(otello, item)
    if len(possibilities) == 0:
        return otello
    evaluation = np.zeros(len(possibilities)).tolist()
    for i in range(len(possibilities)):
        x, y = possibilities[i]
        newotello = place_element(otello.copy(), x, y, item)
        evaluation[i] = minmax(newotello, 1, max_depth, not item, False)
    x, y = possibilities[evaluation.index(max(evaluation))]
    return place_element(otello, x, y, item)
    
def play_otello_minmax(max_depth: int, mode: bool = True):
    if mode:
        otello = init_otello()
        print("Do you want to start ?")
        begin = input("('y' or 'n'. Default: 'y'): ")
        match begin:
            case 'n':
                item = True
            case _:
                item = False
 
        print_otello(otello)
        possibilities = list_possibilities(otello, item)
        while len(possibilities) != 0:
            if item:
                print("'x' must play")
                otello = play_minmax(otello, max_depth, item)
                item = not item
                print_otello(otello)
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


play_otello_minmax(3)

