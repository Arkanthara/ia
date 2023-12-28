import csv
import numpy as np
from scipy.stats import norm

def convert_csv2array(name: str) -> tuple[np.ndarray, np.ndarray]:
    file = open(name, 'r')
    data = []
    reader = csv.reader(file)
    for line in reader:
        data.append(line)
    data = np.array(data)
    return data[0, :], data[1:, :]

header, data = convert_csv2array('data_train.csv')
print(data)
# P(label == 1)
def ampiric_distribution(data: np.ndarray, target: int) -> float:
    return np.sum(data[:, target].astype(int))/len(data)

print(ampiric_distribution(data, -1))

for i in range(len(header)):
    print(np.unique(data[:, i]))

def ampiric_distribution_str(data: np.ndarray, target: int) -> float:
    return np.sum(data[:, target] == data[:, 0])/ len(data)

def distrib_param(data: np.ndarray, header: np.ndarray, target: int):
    result = {}
    values = np.unique(data[:, target])
    for i in range(len(values)):
        newdata = data[data[:, target] == values[i]]
        tmp = {}
        for j in range(len(data[0])):
            if j != target:
                tmp_2 = {}
                newvalues, count = np.unique(newdata[:, j], return_counts = True)
                if len(newvalues) == 2:
                    for k in range(len(newvalues)):
                        tmp_2[newvalues[k]] = count[k] / len(newdata)
                else:
                    tmp_2["Mean"] = np.mean(newdata[:, j].astype(float))
                    tmp_2["Variance"] = np.var(newdata[:, j].astype(float))
                tmp[header[j]] = tmp_2
        result[values[i]] = tmp
    return result


print(distrib_param(data, header, 3))

def naive_base(distrib: dict, header: np.ndarray, data: np.ndarray):
    values_keys = list(distrib.keys())
    maximum = 0
    value = values_keys[0]
    for i in values_keys:
        denom = 1
        for j in range(len(header)):
            if list(distrib[i][header[j]].keys())[0] == "Mean" or list(distrib[i][header[j]].keys())[1] == "Mean":
                denom *= norm.cdf(float(data[j]), distrib[i][header[j]]["Mean"], distrib[i][header[j]]["Variance"])
            else:
                denom *= distrib[i][header[j]][data[j]]
        if denom > maximum:
            maximum = denom
            value = i
    return value

print(naive_base(distrib_param(data, header, 3), ["Gender", "Age"], ["Male", '35']))

_, data_test = convert_csv2array('data_test.csv')
print(data_test)


FN, FP, TN, TP = range(4)

def test_naive_base(distrib: dict, header: np.ndarray, data: np.ndarray):
    if 
