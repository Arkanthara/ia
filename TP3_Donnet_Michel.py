r"""°°°
# Exercise 1: Morpion
°°°"""
# |%%--%%| <mQM1MNiZwv|C90zsNh7zc>
r"""°°°
Dans cet exercice, nous allons essayer de créer un jeu du morpion...
°°°"""
# |%%--%%| <C90zsNh7zc|0>

import numpy as np
from copy import deepcopy

class Morpion:
    def __init__(self):
        self.shape = 3
        self.grid = np.zeros((self.shape, self.shape), int)
        self.computer = True
        self.computer_symbol = 1
        self.user_symbol = 2
        self.computer_win = 0
        self.user_win = 0
    
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

    def win(self, current) -> int:
        for i in {1, 2}:
            for i in range(self.shape):
                if current[i, 0] == current[i, 1] == current[i, 2]
                or current[0, i] == current[1, i] == current[2, i]
                or current[0, 0] == current[1, 1] == current[2, 2]
                    or current[2, 0] == current[1, 1] == current[0, 2]: return i
        return 0


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

    def chance_to_win(self, current: np.ndarray) -> int:
        match self.win(current):
            case self.computer_symbol:
                self.computer_win += 1
                break
            case self.user_symbol:
                self.user_win += 1
                break
            case 0:
                possibilities = self.list_possibilities(current)
                for i in possibilities:
                    self.next_choice(i)
            case _:
                break
        return 0

    def next_choice(self):
        possibilities = self.list_possibilities(self.grid)
        


    def place_element(self, i: int, j: int, k: int) -> int:
        if self.grid[i, j] != 0:
            print(f"You can't place 'x' at index ({i}, {j}) !")
            return -1
        self.grid[i, j] = 1
        return 0




morpion = Morpion()
morpion.place_element(1, 0, 1)
morpion.place_element(1, 1, 2)
print(morpion.list_possibilities())
print(morpion)

# |%%--%%| <0|Ewk14kPwDk>

print("coucou")

# |%%--%%| <Ewk14kPwDk|RvPbTkibqG>
r"""°°°
# Exercice 2
°°°"""
