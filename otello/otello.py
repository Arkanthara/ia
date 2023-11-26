import numpy as np
import matplotlib.pyplot as plt


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
            return i - 1
    # Browse in the other direction if we meet an item
    for i in range(1, indice + 1):
        if mylist[indice - i] == None:
            break
        if mylist[indice - i] is item and i == 1:
            break
        if mylist[indice - i] is item and i > 1:
            return i - 1
    return 0

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

def evaluation(otello: np.ndarray, x: int, y: int, item: bool) -> int:
    w, z = rotate_indices(x, y)
    result = verification(otello, x, y, item) + verification(otello, x, y, item, True)
    otello = np.rot90(otello, 1)
    result += verification(otello, w, z, item) + verification(otello, w, z, item, True)
    otello = np.rot90(otello, -1)
    return result
    
def is_possible(otello: np.ndarray, x: int, y: int, item: bool) -> bool:
    if otello[x, y] != None:
        return False
    if evaluation(otello, x, y, item) == 0:
        return False
    return True


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
            if win_otello(otello) == item: return 10
            else: return -10
        else:
            if win_otello(otello) == item: return -10
            else: return 10
    cost = np.zeros(len(possibilities))
    if path <= Max_depth:
        for i in range(len(possibilities)):
            x, y = possibilities[i]
            newotello = place_element(otello.copy(), x, y, item)
            if Max:
                cost[i] = evaluation(otello, x, y, item)
            else:
                cost[i] = - evaluation(otello, x, y, item)
            cost[i] += minmax(newotello, path + 1, Max_depth, not item, not Max)
        if Max:
            return np.max(cost)
        return np.min(cost)
    return 0
        
def play_minmax(otello: np.ndarray, max_depth, item) -> np.ndarray:
    possibilities = list_possibilities(otello, item)
    if len(possibilities) == 0:
        return otello
    cost = np.zeros(len(possibilities)).tolist()
    for i in range(len(possibilities)):
        x, y = possibilities[i]
        newotello = place_element(otello.copy(), x, y, item)
        cost[i] = minmax(newotello, 1, max_depth, not item, False)
    x, y = possibilities[cost.index(max(cost))]
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


print("My function of evaluation give me the number of tokens which are changed by the player")
print("In MinMax, we alway calculate the cost of a possibility thanks to the evaluation function")
print("and then, we add the result of minmax on next step.")
print("The cost is positive if we are in a max, and negative if we are in a min.")
print("My code run slowly (10 s for a depth of 2...), so I don't know if it's normal... But I made the graphs and answer to the questions..."
print("\n")
def play_otello_minmaxvsminmax(max_depth_1: int, max_depth_2: int):
    otello = init_otello()
    item = True
    number_of_moves = 0
    possibilities = list_possibilities(otello, item)
    while len(possibilities) != 0:
        if item:
            otello = play_minmax(otello, max_depth_1, item)
            item = not item
        else:
            otello = play_minmax(otello, max_depth_2, item)
            item = not item
        number_of_moves += 1
        possibilities = list_possibilities(otello, item)
    if win_otello(otello):
        return 1, number_of_moves
    else:
        return 0, number_of_moves

def variation_depth_minmax(size: int):
    grid_variation_depth = np.zeros((size + 1, size + 1))
    number_of_moves = np.zeros((size + 1, size + 1))
    for i in range(size + 1):
        for j in range(size + 1):
            grid_variation_depth[i, j], number_of_moves[i, j] = play_otello_minmaxvsminmax(i, j)
    result = "Variation of depth of MinMax for max depth of " + str(size) + ":\n"
    result += "grid[i, j] = 1: minmax of depth i win\ngrid[i, j] = 0: minmax of depth j win\n"
    result += "i alway start\n"
    result += "   "
    for i in range(size + 1):
        result += " " + str(i) + " "
    result += "\n"
    for i in range(size + 1):
        result +=" " + str(i) + " "
        for j in range(size + 1):
            result +=" " + str(int(grid_variation_depth[i, j])) + " "
        result += "\n"
    print(result)

    average_number_of_moves = np.mean(number_of_moves, axis = 0) + np.mean(number_of_moves, axis = 1) / 2*(size + 1)
    success = np.zeros(size + 1)
    for i in range(size + 1):
        for j in range(size + 1):
            if grid_variation_depth[i, j] == 1:
                success[i] += 1
            if grid_variation_depth[i, j] == 0:
                success[j] += 1
    success /= size + 1 * size + 1
    print("Success rate:")
    for i in range(size + 1):
        print("")
        print(f"Depth {i}: {success[i]}")
        print(f"Average number of moves: {average_number_of_moves[i]}")
        print("")

    x = [i for i in range(size + 1)]
    plt.figure()
    plt.title("success rate as a function of depth")
    plt.plot(x, success)
    plt.xlabel("Depth")
    plt.ylabel("Success rate")
    plt.legend()
    plt.show()

variation_depth_minmax(2)
