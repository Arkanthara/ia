import csv
import numpy as np


file = open('data.csv', 'r')
#with open('data.csv', 'r') as file:

data = []

reader = csv.reader(file)

for row in reader:
    data.append(row)

datacsv = np.array(data)
data = datacsv[1:, :]
header = datacsv[0, :]


def entropy(data: np.ndarray, column: int) -> float:
    values = np.unique(data[:, column])
    result = 0
    for i in values:
        nb = np.sum(data[:, column] == i)
        nb = nb / len(data)
        result += -nb * np.log2(nb)
    return result

# H(column_1|column_2)
def conditionnal_entropy(data: np.ndarray, column_1: int, column_2: int) -> float:
    values = np.unique(data[:, column_2])
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
    values = np.unique(data[:, column])
    result = 0
    for i in values:
        nb = np.sum(data[:, column] == i) / len(data)
        result += nb * nb
    return 1 - result

print(entropy(data, 5))
print(conditionnal_entropy(data, 5, 3))
print(mutual_information(data, 5, 3))
print(gini(data, 5))


def id3(data: np.ndarray, header: np.ndarray, index_data_to_train: int):
    
    # Get the number of column of data
    n = len(data[0])

    # Case 1 column: count number of each element and return priority element
    if n == 1:
        values, count = np.unique(data[:], return_counts=True)
        maximum = 0
        index = 0
        for i in range(len(values)):
            if count[i] > maximum:
                maximum = count[i]
                index = i
        return int(values[i])

    # Test if there is some different values for the column to train
    # If not, return the value
    test_unique = np.unique(data[:, index_data_to_train])
    if len(test_unique) == 1:
        return int(test_unique[0])

    # Compute mutual information between the column to train and each other column
    # The column choosen maximise the mutual information
    maximum = 0
    index = 0
    for i in range(n):
        if i != index_data_to_train:
            info = mutual_information(data, index_data_to_train, i)
            if info > maximum:
                maximum = info
                index = i

    # Get all the values of the column choosen.
    # For each values, compute id3 on a new data with just the line
    # where the value of the column choosen is equal to the selected value
    # and with the column choosen deleted.
    # Compute a tree thanks to the results of id3 for each new data
    values = np.unique(data[:, index])
    tree = {}
    for i in values:
        newdata = np.delete(data[data[:, index] == i], index, 1)
        newheader = np.delete(header, index, 0)
        if (index < index_data_to_train):
            tree[int(i)] = id3(newdata, newheader, index_data_to_train - 1)
        else:
            tree[int(i)] = id3(newdata, newheader, index_data_to_train)
    
    # Return the tree obtained
    return {header[index]: tree}

print(id3(data, header, 5))
