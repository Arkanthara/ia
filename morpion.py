""" import numpy as np
from copy import deepcopy

class Morpion:

    # Init morpion
    def __init__(self):
        self.shape = 3
        self.grid = np.zeros((self.shape, self.shape), int)
        self.computer = False
        self.computer_symbol = 1
        self.user_symbol = 2
        self.table_win = []
        self.index = 0

    # Print morpion
    def __str__(self):
        n = self.shape
        result = ""
        for i in range(n):
            for j in range(n):
                if self.grid[i, j] == 1:
                    result += " o "
                elif self.grid[i, j] == 2:
                    result += " x "
                else:
                    result += " - "
            result += "\n"
        return result
    
    def choose_symbol(self):
        print("Choose your symbol:")
        print("1: 'o'")
        print("2: 'x'")
        value = input(">")
        match value:
            case "1":
                print("Symbol choosed: 'o'")
                self.computer_symbol = 2
                self.user_symbol = 1
            case "2":
                print("Symbol choosed: 'x'")
                self.computer_symbol = 1
                self.user_symbol = 2
            case _ :
                print("Bad value !")
                self.choose_symbol()
    
    def choose_begin(self):
        print("Do you want to begin ('y' or 'n'. default: 'y')")
        value = input(">")
        match value:
            case "n":
                print("Computer begin")
                self.computer = True
            case _:
                print("You begin")
    
    def play(self):
        self.choose_symbol()
        self.choose_begin()
        while self.win(self.grid) == 0:
            self.play_computer()
            print(self)
            self.play_user()
        
        if self.win(self.grid) == 1:
            if self.computer_symbol == 1:
                print("Looser !")
            else:
                print("You win !")
        else:
            if self.computer_symbol == 2:
                print("Looser !")
            else:
                print("You win !")

    # Return 1 or 2 if symbol 1 or symbol 2 win
    def win(self, current) -> int:
        for i in range(3):
            if current[i, 0] == current[i, 1] == current[i, 2]:
                return current[i, 0]
            if current[0, i] == current[1, i] == current[2, i]:
                return current[0, i]
            if current[0, 0] == current[1, 1] == current[2, 2] or current[2, 0] == current[1, 1] == current[0, 2]:
                return current[1, 1]
        return 0

    # Give list of possibilities for computer or user
    def list_possibilities(self, current: np.ndarray) -> list[np.ndarray]:
        result = []
        if self.computer:
            for i in range(self.shape):
                for j in range(self.shape):
                    if current[i, j] == 0:
                        newgrid = deepcopy(current)
                        newgrid[i, j] = self.computer_symbol
                        result.append(newgrid)
        else:
            for i in range(self.shape):
                for j in range(self.shape):
                    if current[i, j] == 0:
                        newgrid = deepcopy(current)
                        newgrid[i, j] = self.user_symbol
                        result.append(newgrid)
        return result
    
    def next_choice_critical(self) -> bool:
        if self.computer:
            for i in range(self.shape):
                for j in range(self.shape):
                    if self.grid[i, j] == 0:
                        self.grid[i, j] == self.user_symbol
                        if self.win(self.grid) != 0:
                            self.grid[i, j] = self.computer_symbol
                            return True
                        self.grid[i, j] = 0
        return False

    def next_choice(self, current: np.ndarray, table: np.ndarray, index: int):
        win = self.win(current)
        if win == 0:
            self.computer = not self.computer
            possibilities = self.list_possibilities(current)
            print("rec:")
            for i in possibilities:
                self.next_choice(i, table, index)
                print(i)
        elif win == self.computer_symbol: 
            table[index] += 1
        elif win == self.user_symbol: 
            table[index] -= 1

    def play_computer(self):
        if self.computer:
            if self.next_choice_critical() == False:
                possibilities = self.list_possibilities(self.grid)
                table = np.zeros(len(possibilities))
                print(table)
                for i in range(len(possibilities)):
                    self.next_choice(possibilities[i], table, i)
                max_path = table[0]
                print(table)
                index = 0
                for i in range(len(possibilities)):
                    print(i)
                    if table[i] > max_path:
                        max_path = table[i]
                        index = i
                self.grid = possibilities[index]
                self.computer = False

    def play_user(self):
        print("row (choose a number in {0, 1, 2})")
        value = input(">")
        while value != "0" and value != "1" and value != "2":
            print("Bad value !")
            print("row (choose a number in {0, 1, 2}):")
            value = input(">")
        print("column (choose a number in {0, 1, 2})")
        value_2 = input(">")
        while value_2 != "0" and value_2 != "1" and value_2 != "2":
            print("Bad value !")
            print("column (choose a number in {0, 1, 2}):")
            value_2 = input(">")
        self.place_element(int(value), int(value_2))


    def place_element(self, i: int, j: int) -> int:
        if self.grid[i, j] != 0:
            print(f"You can't place 'x' at index ({i}, {j}) !")
            return -1
        self.grid[i, j] = self.user_symbol
        self.computer = True
        return 0




morpion = Morpion()
morpion.play() """
import numpy as np
from copy import deepcopy

class Morpion:

    # Init morpion
    def __init__(self):
        self.shape = 3
        self.grid = np.zeros((self.shape, self.shape), int)
        self.computer = False
        self.computer_symbol = 1
        self.user_symbol = 2
        self.table_win = []
        self.index = 0
        self.begin = 2

    # Print morpion
    def __str__(self):
        n = self.shape
        result = ""
        for i in range(n):
            for j in range(n):
                if self.grid[i, j] == 1:
                    result += " o "
                elif self.grid[i, j] == 2:
                    result += " x "
                else:
                    result += " - "
            result += "\n"
        return result
    
    def choose_symbol(self):
        print("Choose your symbol:")
        print("1: 'o'")
        print("2: 'x'")
        value = input(">")
        match value:
            case "1":
                print("Symbol choosed: 'o'")
                self.computer_symbol = 2
                self.user_symbol = 1
            case "2":
                print("Symbol choosed: 'x'")
                self.computer_symbol = 1
                self.user_symbol = 2
            case _ :
                print("Bad value !")
                self.choose_symbol()
    
    def choose_begin(self):
        print("Do you want to begin ('y' or 'n'. default: 'y')")
        value = input(">")
        match value:
            case "n":
                print("Computer begin")
                self.computer = True
                self.begin = self.computer_symbol
            case _:
                print("You begin")
                self.begin = self.user_symbol
    
    def play(self):
        self.choose_symbol()
        self.choose_begin()
        while self.win(self.grid) == 0:
            self.play_computer()
            print(self)
            self.computer = True
            self.play_user()
        
        if self.win(self.grid) == self.computer_symbol:
            print("Looser !")
        else:
            print("You win !")

    def who_should_play(self, current):
        count = 0
        for i in range(self.shape):
            for j in range(self.shape):
                if current[i, j] != 0:
                    count += 1
        if count % 2 == 1:
            if self.begin == 1: return 2
            else: return 1
        else:
            return self.begin

    # Return 1 or 2 if symbol 1 or symbol 2 win
    def win(self, current) -> int:
        for i in range(3):
            if current[i, 0] == current[i, 1] == current[i, 2]:
                return current[i, 0]
            if current[0, i] == current[1, i] == current[2, i]:
                return current[0, i]
            if current[0, 0] == current[1, 1] == current[2, 2] or current[2, 0] == current[1, 1] == current[0, 2]:
                return current[1, 1]
        return 0

    # Give list of possibilities for computer or user
    def list_possibilities(self, current: np.ndarray) -> list[np.ndarray]:
        result = []
        symbol = self.who_should_play(current)
        for i in range(self.shape):
            for j in range(self.shape):
                if current[i, j] == 0:
                    newgrid = deepcopy(current)
                    newgrid[i, j] = symbol
                    result.append(newgrid)
        return result
    
    def next_choice_critical(self) -> bool:
        if self.computer:
            for i in range(self.shape):
                for j in range(self.shape):
                    if self.grid[i, j] == 0:
                        self.grid[i, j] == self.user_symbol
                        if self.win(self.grid) != 0:
                            self.grid[i, j] = self.computer_symbol
                            return True
                        self.grid[i, j] = 0
        return False

    def next_choice(self, current: np.ndarray, table: np.ndarray, index: int):
        win = self.win(current)
        print("current")
        print(current)
        print(win)
        if win == 0:
            possibilities = self.list_possibilities(current)
            print("possibilities")
            print(possibilities)
            for i in possibilities:
                self.next_choice(i, table, index)
        elif win == self.computer_symbol:
            table[index] += 1
        elif win == self.user_symbol: 
            table[index] -= 1

    def play_computer(self):
        if self.computer:
            if not self.next_choice_critical():
                possibilities = self.list_possibilities(self.grid)
                table = np.zeros(len(possibilities))
                print(table)
                for i in range(len(possibilities)):
                    if self.win(possibilities[i]) == self.computer_symbol:
                        self.grid = possibilities[i]
                        return
                    self.next_choice(possibilities[i], table, i)
                max_path = table[0]
                print(table)
                index = 0
                for i in range(len(possibilities)):
                    print(i)
                    if table[i] > max_path:
                        max_path = table[i]
                        index = i
                self.grid = possibilities[index]

    def play_user(self):
        print("row (choose a number in {0, 1, 2})")
        value = input(">")
        while value != "0" and value != "1" and value != "2":
            print("Bad value !")
            print("row (choose a number in {0, 1, 2}):")
            value = input(">")
        print("column (choose a number in {0, 1, 2})")
        value_2 = input(">")
        while value_2 != "0" and value_2 != "1" and value_2 != "2":
            print("Bad value !")
            print("column (choose a number in {0, 1, 2}):")
            value_2 = input(">")
        self.place_element(int(value), int(value_2))


    def place_element(self, i: int, j: int) -> int:
        if self.grid[i, j] != 0:
            print(f"You can't place 'x' at index ({i}, {j}) !")
            return -1
        self.grid[i, j] = self.user_symbol
        return 0




morpion = Morpion()
morpion.play()