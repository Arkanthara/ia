import numpy as np
from copy import deepcopy

class Morpion:

    # Init morpion
    def __init__(self):
        self.grid = np.zeros((3, 3), int)
        self.computer = True
        self.user_symbol = 2
        self.begin = 2
        self.computer_begin = True

    # Print morpion
    def __str__(self):
        n = 3
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
                self.user_symbol = 1
            case "2":
                print("Symbol choosed: 'x'")
                self.user_symbol = 2
            case _ :
                print("Bad value !")
                self.choose_symbol()
    
    def choose_begin(self):
        print("Do you want to play with computer ? ('y' or 'n'. Default: 'y')")
        value = input(">")
        match value:
            case "n":
                self.computer = False
            case _:
                self.computer = True
        print("Do you want to begin ('y' or 'n'. Default: 'y')")
        value = input(">")
        match value:
            case "n":
                print("Ennemy begin")
                self.begin = (self.user_symbol + 1) % 2 + 1
                if self.computer:
                    self.user_begin = False
            case _:
                print("You begin")
                self.begin = self.user_symbol
                self.user_begin = True
    
    def play(self):
        self.choose_symbol()
        self.choose_begin()
        print(self.computer)
        if self.computer:
            while self.win(self.grid) == 0:
                self.play_computer(10)
                print(self)
                self.user_begin = False
                self.play_user()

        else:
            while self.win(self.grid) == 0:
                print(self)
                self.play_user()
        
        if self.win(self.grid) == self.user_symbol:
            print("You win !")
        else:
            print("Ennemy win !")
        print(self)

    def who_should_play(self, current):
        count = np.sum(self.grid != 0)
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
        for i in range(3):
            for j in range(3):
                if current[i, j] == 0:
                    newgrid = deepcopy(current)
                    newgrid[i, j] = symbol
                    result.append(newgrid)
        return result
    
    
    def play_computer(self, max_depth):
        if self.win(self.grid) != 0 or self.user_begin:
            return
        possibilities = self.list_possibilities(self.grid)
        print(possibilities)
        evaluation_table = np.zeros(len(possibilities)).tolist()
        for i in range(len(possibilities)):
            evaluation_table[i] = self.MinMax(possibilities[i], 1, max_depth)
        print(evaluation_table)
        self.grid = possibilities[evaluation_table.index(max(evaluation_table))]



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
        self.grid[i, j] = self.who_should_play(self.grid)
        return 0


    def MinMax(self, current: np.ndarray, depth: int, max_depth: int) -> int:
        if self.win(current) != 0:
            if self.who_should_play(current) != self.user_symbol: return -1
            else: return 1
        if depth < max_depth:
            possibilities = self.list_possibilities(current)
            evaluation_table = np.zeros(len(possibilities))
            if len(possibilities) == 0: return 0
            for i in range(len(possibilities)):
                evaluation_table[i] = self.MinMax(possibilities[i], depth + 1, max_depth)
            if self.who_should_play(current) != self.user_symbol:
                return np.max(evaluation_table)
            else:
                return np.min(evaluation_table)
        else:
            return 0


