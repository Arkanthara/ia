import csv
import numpy as np


def convert_csv2array(name: str) -> tuple[np.ndarray, np.ndarray]:
    file = open(name, 'r')
    data = []
    reader = csv.reader(file)
    for line in reader:
        data.append(line)
    data = np.array(data)
    return data[0, :], data[1:, :]

header, data = convert_csv2array('data_train.csv')

# P(label == 1)
def ampiric_distribution(data: np.ndarray, target: int) -> float:
    return np.sum(data[:, target].astype(int))/len(data)

print(ampiric_distribution(data, -1))

for i in range(len(header)):
    print(np.unique(data[:, i]))

def ampiric_distribution_str(data: np.ndarray, target: int) -> float:
    return np.sum(data[:, target] == data[:, 0])/ len(data)


