import numpy as np



def init_morpion() -> np.ndarray:
    morpion = np.empty(shape=(3, 3), dtype='object')
    return morpion

def print_morpion(morpion: np.ndarray):
    result = "    0  1  2\n"
    for i in range(3):
        result += " " + str(i) + " "
        for j in range(3):
            match morpion[i, j]:
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

def win_morpion(morpion: np.ndarray) -> bool:
    for i in range(3):
        if morpion[i, 0] == morpion[i, 1] == morpion[i, 2]:
            return morpion[i, 0]
        if morpion[0, i] == morpion[1, i] == morpion[2, i]:
            return morpion[0, i]
    if morpion[0, 0] == morpion[1, 1] == morpion[2, 2] or morpion[2, 0] == morpion[1, 1] == morpion[0, 2]:
        return morpion[1, 1]
    return None

def list_possibilities(morpion: np.ndarray, item: bool) -> list[tuple[int, int]]:
    result = []
    for i in range(3):
        for j in range(3):
            if is_possible(morpion, i, j, item):
                result.append((i, j))
    return result

def place_element(morpion: np.ndarray, x: int, y: int, item: bool) -> np.ndarray:
    if is_possible(morpion, x, y, item):
        morpion[x, y] = item
    return morpion

def play_morpion():
    morpion = init_morpion()
    item = False
    print_morpion(morpion)
    possibilities = list_possibilities(morpion, item)
    while win_morpion(morpion) == None:
        if item:
            print("'x' must play")
        else:
            print("'o' must play")
        possibilities = list_possibilities(morpion, item)
        print("Suggestions: " + str(possibilities))
        try:
            x = int(input("Row: "))
            y = int(input("Column: "))
            if is_possible(morpion, x, y, item):
                morpion = place_element(morpion, x, y, item)
                item = not item
                print_morpion(morpion)
        except ValueError:
            print("You must enter a digit !")
    if win_morpion(morpion):
        print("'x' win")
    elif win_morpion(morpion) != None:
        print("'o' win")
    else:
        print("No winner")

def minmax(morpion: np.ndarray, path: int, max_depth: int, item: bool, Max: bool) -> int:
    possibilities = list_possibilities(morpion, item)
    if Max:
        if win_morpion(morpion) != None: return -1
    else:
        if win_morpion(morpion) != None: return 1
    if len(possibilities) == 0: return 0
    evaluation = np.zeros(len(possibilities))
    if path <= max_depth:
        for i in range(len(possibilities)):
            x, y = possibilities[i]
            newmorpion = place_element(morpion.copy(), x, y, item)
            evaluation[i] = minmax(newmorpion, path + 1, max_depth, not item, not Max)
        if Max:
            return np.max(evaluation)
        return np.min(evaluation)
    return 0
         
def play_minmax(morpion: np.ndarray, max_depth, item) -> np.ndarray:
    possibilities = list_possibilities(morpion, item)
    if len(possibilities) == 0:
        return morpion
    evaluation = np.zeros(len(possibilities)).tolist()
    for i in range(len(possibilities)):
        x, y = possibilities[i]
        newmorpion = place_element(morpion.copy(), x, y, item)
        evaluation[i] = minmax(newmorpion, 1, max_depth, not item, False)
    x, y = possibilities[evaluation.index(max(evaluation))]
    return place_element(morpion, x, y, item)
 

def play_morpion_minmax(max_depth: int, mode: bool = True):
    if mode:
        morpion = init_morpion()
        print("Do you want to start ?")
        begin = input("('y' or 'n'. Default: 'y'): ")
        match begin:
            case 'n':
                item = True
            case _:
                item = False
        print_morpion(morpion)
        possibilities = list_possibilities(morpion, item)
        while win_morpion(morpion) == None and len(possibilities) != 0:
            if item:
                print("'x' must play")
                morpion = play_minmax(morpion, max_depth, item)
                item = not item
                print_morpion(morpion)
            else:
                print("'o' must play")
                possibilities = list_possibilities(morpion, item)
                print("Suggestions: " + str(possibilities))
                try:
                    x = int(input("Row: "))
                    y = int(input("Column: "))
                    if is_possible(morpion, x, y, item):
                        morpion = place_element(morpion, x, y, item)
                        item = not item
                        print_morpion(morpion)
                except ValueError:
                    print("You must enter a digit !")
        if win_morpion(morpion):
            print("'x' win")
        elif win_morpion(morpion) != None:
            print("'o' win")
        else:
            print("No winner")
    else:
        play_morpion()



def play_morpion_minmaxvsminmax(max_depth_1: int, max_depth_2: int):
    morpion = init_morpion()
    item = True
    possibilities = list_possibilities(morpion, item)
    while win_morpion(morpion) == None and len(possibilities) != 0:
        if item:
            morpion = play_minmax(morpion, max_depth_1, item)
            item = not item
        else:
            morpion = play_minmax(morpion, max_depth_2, item)
            item = not item
        possibilities = list_possibilities(morpion, item)
    if win_morpion(morpion):
        return 1
    elif win_morpion(morpion) != None:
        return 2
    else:
        return 0

def variation_depth_minmax(size: int):
    grid_variation_depth = np.zeros((size + 1, size + 1))
    for i in range(size + 1):
        for j in range(size + 1):
            grid_variation_depth[i, j] = play_morpion_minmaxvsminmax(i, j)
    result = "Variation of depth of MinMax for max depth of " + str(size) + ":\n"
    result += "grid[i, j] = 1: minmax of depth i win\ngrid[i, j] = 2: minmax of depth j win\ngrid[i, j] = 0: nobody win\n"
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

play_morpion_minmaxvsminmax(5, 5)

variation_depth_minmax(5)
