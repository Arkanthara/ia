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

counter = lambda data, x, y: list(data[1:, y]).count(x)

print(counter(data, '1', -1) / (len(data) - 1))

#print(entropy(np.sum(np.array([int(i) for i in data[1:,-1]])) / (len(data) - 1) ))
print(entropy(counter(data, '1', -1) / (len(data) - 1) ))
print(entropy(counter(data, '0', -1) / (len(data) - 1) ))
