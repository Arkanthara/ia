import csv
import numpy as np


file = open('data.csv', 'r')
#with open('data.csv', 'r') as file:

A = []
B = []
C = []
D = []
c = []

data = []

reader = csv.reader(file)

for row in reader:
    data.append(row)

datacsv = np.array(data)
data = datacsv[1:, :]
header = datacsv[0, :]


def entropy(data: np.ndarray, column: int) -> float:
    values = np.unique(data[1:, column])
    result = 0
    for i in values:
        nb = np.sum(data[1:, column] == i)
        nb = nb / len(data)
        result += -nb * np.log2(nb)
    return result

# H(column_1|column_2)
def conditionnal_entropy(data: np.ndarray, column_1: int, column_2: int) -> float:
    values = np.unique(data[1:, column_2])
    result = 0
    for i in values:
        newdata = data[data[:, column_2] == i]
        nb = len(newdata)
        nb = nb / len(data)
        result += nb * entropy(newdata, column_1)
    return result
# I(column_1; column_2)
def mutual_information(data: np.ndarray, column_1: int, column_2: int) -> float:
    return entropy(data, column_1) - conditionnal_entropy(data, column_1, column_2)


def gini(data: np.ndarray, column: int) -> float:
    values = np.unique(data[1:, column])
    result = 0
    for i in values:
        nb = np.sum(data[:, column] == i) / len(data)
        result += nb * nb
    return 1 - result

print(entropy(data, 5))
print(conditionnal_entropy(data, 5, 3))
print(mutual_information(data, 5, 3))
print(gini(data, 5))


def id3(data: np.ndarray):
    print("Hellooooo !!!")

id3(data)
