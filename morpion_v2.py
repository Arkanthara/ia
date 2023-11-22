import numpy as np
from copy import deepcopy

class Morpion:

    # Init morpion
    def __init__(self):
        self.shape = 3
        self.grid = np.zeros((self.shape, self.shape), int)
        self.computer = False
        self.computer_symbol = 1
        self.play_computer = True
        self.user_symbol = 2
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
        print("Do you want to play with computer ? ('y' or 'n'. Default: 'y')")
        value = input(">")
        match value:
            case "n":
                self.play_computer = False
            case "y":
                self.play_computer = True
        print("Do you want to begin ('y' or 'n'. Default: 'y')")
        value = input(">")
        match value:
            case "n":
                print("Ennemy begin")
                self.computer = True
                self.begin = self.computer_symbol
            case _:
                print("You begin")
                self.begin = self.user_symbol
    
    def play(self):
        self.choose_symbol()
        self.choose_begin()
        while self.win(self.grid) == 0:
            if self.play_computer:
                self.play_computer()
                print(self)
                self.computer = True
                self.play_user()

            else:
                print(self)
                self.play_user()
        
        if self.win(self.grid) == self.computer_symbol:
            print("Ennemy win !")
        else:
            print("You win !")
        print(self)

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
        self.place_element(self.grid, int(value), int(value_2))


    def place_element(self, current: np.ndarray, i: int, j: int) -> int:
        if current[i, j] != 0:
            print(f"You can't place 'x' at index ({i}, {j}) !")
            return -1
        current[i, j] = self.who_should_play(self.grid)
        #self.grid[i, j] = k
        return 0


