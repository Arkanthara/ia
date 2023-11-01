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

    def list_possibilities(self) -> list[np.ndarray]:
        result = []
        if self.computer:
            for i in range(self.shape):
                for j in range(self.shape):
                    if self.grid[i, j] == 0:
                        newgrid = deepcopy(self.grid)
                        newgrid[i, j] = self.computer_symbol
                        result.append(newgrid)
        return result

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
