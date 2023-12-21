import csv
import numpy as np
import random


def convert_csv2array(name: str) -> tuple[np.ndarray, np.ndarray]:
    file = open(name, 'r')
    data = []
    reader = csv.reader(file)
    for line in reader:
        data.append(line)
    data = np.array(data)
    return data[0, :], data[1:, :].astype(int)

header, data = convert_csv2array('data.csv')
_, data_test = convert_csv2array('data_test.csv')


print(data_test)

FN, FP, TN, TP = range(4)

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
    newdata = data.copy()
    np.random.shuffle(newdata)
    return newdata[indices], newdata[last_indices[1:]]

trees = []
training = []
test = []
for i in range(5):
    data_training, data_tests = get_percentage_of_data(data, 80)
    training.append(data_training)
    test.append(data_tests)
    trees.append(id3(data_training, header, 5))

def eval(mytree, data: np.ndarray, header: np.ndarray, target: int) -> int:
    tree = mytree.copy()
    data = np.array(data).astype(int)
    while type(tree) != int:
        keys = list(tree.keys())
        index = np.where(header == keys[0])[0][0]
        tree = tree[header[index]]
        keys = list(tree.keys())
        if data[index] not in keys:
            if data[target] == 0:
                return TN
            return FP
        tree = tree[data[index]]
    if data[target] == 1 and tree == 1:
        return TP
    if data[target] == 0 and tree == 1:
        return FN
    if data[target] == 0 and tree == 0:
        return TN
    if data[target] == 1 and tree == 0:
        return FP

# Comparer profondeur arbres....

def evaluation(tree, test: np.ndarray, header: np.ndarray, target: int):
    n = len(test)
    FN_count = 0
    FP_count = 0
    TN_count = 0
    TP_count = 0
    for i in test:
        result = eval(tree, i, header, target)
        if result == FN: FN_count += 1
        if result == FP: FP_count += 1
        if result == TN: TN_count += 1
        if result == TP: TP_count += 1
    return FN_count/n, FP_count/n, TN_count/n, TP_count/n

print(evaluation(tree, data_test, header, 5))

def accuracy(tree, test: np.ndarray, header: np.ndarray, target: int) -> float:
    fn, fp, tn, tp = evaluation(tree, test, header, target)
    print(evaluation(tree, test, header, target))
    return (fp + fn)/(tp + tn + fp + fn)

def precision(tree, test: np.ndarray, header: np.ndarray, target: int):
    fn, fp, tn, tp = evaluation(tree, test, header, target)
    return tp / (tp + fp), tp / (tp + fn)

# Moyenne de la moyenne des inverses...
def f1_score(tree, test: np.ndarray, header: np.ndarray, target: int) -> float:
    p, r = precision(tree, test, header, target)
    return (2 * p * r) / (p + r)

accuracy_target = accuracy(tree, data_test, header, 5)
precision_target_p, precision_target_r = precision(tree, data_test, header, 5)
f1_score_target = f1_score(tree, data_test, header, 5)

average_accuracy = 0
average_precision_p = 0
average_precision_r = 0
average_f1_score = 0
for i in range(len(trees)):
    average_accuracy += accuracy(trees[i], data_test, header, 5)
    p, r = precision(trees[i], data_test, header, 5)
    average_precision_p += p
    average_precision_r += r
    average_f1_score += f1_score(trees[i], data_test, header, 5)

average_accuracy /= len(trees)
average_precision_p /= len(trees)
average_precision_r /= len(trees)
average_f1_score /= len(trees)

print("Tree")
print("accuracy: " + str(accuracy_target))
print("precision (p, r): (" + str(precision_target_p) + ", " + str(precision_target_r) + ")")
print(f"F1 score: {f1_score_target}")

print("Average")
print(f"accuracy: {average_accuracy}")
print(f"precision (p, r): ({average_precision_p}, {average_precision_r})")
print(f"F1 score: {average_f1_score}")

