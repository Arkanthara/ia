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

data = np.array(data)

print(data)

entropy = lambda x:  -x * np.log2(x)

def join_entropy(data, w, x, y, z):
    return entropy(len(data[(data[:, w] == y) & (data[:, x] == z)]) / (len(data) - 1))

counter = lambda data, x, y: list(data[1:, y]).count(x)

conditionnal_entropy = lambda data, w, x, y, z: join_entropy(data, w, x, y, z) - entropy(counter(data, z, x) / (len(data) - 1))

print(conditionnal_entropy(data, 1, 3, '1', '0'))

print(join_entropy(data, 1, 3, '1', '0'))

print(counter(data, '1', -1) / (len(data) - 1))

#print(entropy(np.sum(np.array([int(i) for i in data[1:,-1]])) / (len(data) - 1) ))
print(entropy(counter(data, '1', -1) / (len(data) - 1) ))
print(entropy(counter(data, '0', -1) / (len(data) - 1) ))
