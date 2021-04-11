from matplotlib import pyplot as plt
import numpy as np
from load_in_data import default_data


def averageOfList(filename):
    l = []
    file = open(filename+".txt", "r")
    for line in file:
        seperator = line.split(",")
        l.append(float(seperator[1]))
    return np.average(l)

def plotData(listX, listY, title):
    plt.plot(listX, listY)
    plt.title(title)
    plt.xlabel("Episodes")
    plt.ylabel("Reward")
    plt.show()
def loadInData(n):
    x = []
    y = []
    file = open(n+".txt", "r")
    for line in file:
        seperator = line.split(",")
        x.append(float(seperator[0]))
        y.append(float(seperator[1]))
    return x,y


if __name__ == '__main__':
    #name = input("Filename? ")
    path = "results/result_defend_the_center_epochs_20_index_0/"
    filename = "Nolan_model_defend_the_center_epoch_"
    default = default_data()
    x = []
    for n in default.eval_epoch:
        x.append(averageOfList(path + filename + str(n)))
    print(default.eval_epoch)
    plotData(default.eval_epoch, x, "Test")