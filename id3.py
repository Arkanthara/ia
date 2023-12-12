import csv
import numpy as np
import random

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
    values, count = np.unique(data[:, column], return_counts=True)
    result = 0
    for i in range(len(values)):
        nb = count[i] / len(data)
        result += -nb * np.log2(nb)
    return result

# H(column_1|column_2)
def conditionnal_entropy(data: np.ndarray, column_1: int, column_2: int) -> float:
    values, count = np.unique(data[:, column_2], return_counts=True)
    result = 0
    for i in range(len(values)):
        newdata = data[data[:, column_2] == values[i]]
        nb = count[i] / len(data)
        result += nb * entropy(newdata, column_1)
    return result
# I(column_1; column_2)
def mutual_information(data: np.ndarray, column_1: int, column_2: int) -> float:
    return entropy(data, column_1) - conditionnal_entropy(data, column_1, column_2)


def gini(data: np.ndarray, column: int) -> float:
    values, count = np.unique(data[:, column], return_counts=True)
    result = 0
    for i in range(len(values)):
        nb = count[i] / len(data)
        result += nb * nb
    return 1 - result

print(mutual_information(data, 5, 3))
print(mutual_information(data, 5, 1))
print(mutual_information(data, 5, 2))
print(gini(data, 3))
print(gini(data, 1))
print(gini(data, 2))


def id3(data: np.ndarray, header: np.ndarray, index_data_to_train: int, use_gini: bool = False):
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
    minimum = 1
    index = 0
    for i in range(n):
        if i != index_data_to_train:
            if use_gini:
                info = gini(data, i)
                if info < minimum:
                    minimum = info
                    index = i
            else:
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
            tree[int(i)] = id3(newdata, newheader, index_data_to_train - 1, use_gini)
        else:
            tree[int(i)] = id3(newdata, newheader, index_data_to_train, use_gini)
    
    # Return the tree obtained
    return {header[index]: tree}
print(id3(data, header, 5, True))
tree = id3(data, header, 5)
print(tree)

# Gen data thanks to a tree
def gen_data(tree, item_unknow):
    data = {}
    mytree = tree
    while type(mytree) != int and len(list(mytree.keys())) != 0:
        item = list(mytree.keys())[0]
        mytree = mytree[item]
        if type(mytree) != int:
            keys = list(mytree.keys())
            randnumber = random.randint(0, len(keys) - 1)
            data[item] = keys[randnumber]
            mytree = mytree[keys[randnumber]]
        else:
            data[item_unknow] = mytree
    if type(mytree) == int:
        data[item_unknow] = mytree

    return data

# Complete datas generated thanks to the tree
def complete_gen_data(tree, item_unknow, header):
    data = gen_data(tree, item_unknow)
    keys = list(header.keys())
    for i in keys:
        if i not in data:
            values = header[i]
            random_number = random.randint(0, len(header[i]) - 1)
            data[i] = values[random_number]
    return data
complete_header = {}
for i in range(len(header)):
    complete_header[header[i]] = np.unique(data[i])

# Allow to generate multiple datas from a tree
def gen_multiple_datas(tree, item_unknow, header, number):
    result = []
    keys = list(header.keys())
    result.append(keys)
    for i in range(number):
        data = complete_gen_data(tree, item_unknow, header)
        newdata = []
        for j in range(len(keys)):
            newdata.append(data[keys[j]])
        result.append(newdata)
    result = np.array(result)
    return result


print(gen_multiple_datas(tree, 'c', complete_header, 10))

def get_percentage_of_data(data: np.ndarray, percentage: int) -> np.ndarray:
    indices = np.arange(len(data))
    indices = np.unique((indices * percentage/100).round().astype(int))
    last_indices = np.arange(len(data))
    mask = np.isin(last_indices, indices).astype(int)
    mask -= 1
    mask[mask < 0] = 1
    last_indices = np.unique(last_indices * mask).astype(int)
    print(last_indices)
    newdata = data.copy()
    np.random.shuffle(newdata)
    return newdata[indices], newdata[last_indices[1:]]

list_tree = []
for i in range(5):
    list_tree.append(id3(get_percentage_of_data(data, 80)[0], header, 5))
for i in range(5):
    print(list_tree[i])

