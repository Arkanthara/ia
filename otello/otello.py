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
    #z = np.abs(x - size + 1)
    z = x
    return w, z

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

    for i in range(1, len(mylist) - indice):
        if mylist[indice + i] == None:
            break
        if mylist[indice + i] is item and i > 1:
            return True
    for i in range(1, indice):
        if mylist[indice - i] == None:
            break
        if mylist[indice - i] is item and i > 1:
            return True
    return False

# print(verification([[True, None True], [False, True, False]], 
    
def is_possible(otello: np.ndarray, x: int, y: int, item: bool) -> bool:
    a = np.arange(16).reshape(4, 4);
    offset = x - y
    diag_1 = np.diagonal(a, offset)
    indice = y - np.abs(offset)
    if otello[x, y] != None:
        return False
    rotate_otello = np.rot90(otello)
    w, z = rotate_indices(x, y)
    return (verification(otello, x, y, item)
            or verification(otello, x, y, item, True)
            or verification(rotate_otello, w, z, item)
            or verification(rotate_otello, w, z, item, True))

def place_element(otello: np.ndarray, x: int, y: int, item: bool) -> np.ndarray:
    if is_possible(otello, x, y, item):
        print("It's possible")
    else:
        print("It's not possible")
    otello[x, y] = item
    return otello
otello = init_otello()
print_otello(otello)


print(is_possible(otello, 3, 1, True))

place_element(otello, 3, 2, True) 
print_otello(otello)
