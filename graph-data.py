from matplotlib import pyplot as plt
import numpy as np
#abs_path = "./models/model_basic_epochs_20_index_1/"

def averageOfList(filename):
    l = []
    file = open("results/"+filename+".txt", "r")
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
    file = open("results/"+n+".txt", "r")
    for line in file:
        seperator = line.split(",")
        x.append(float(seperator[0]))
        y.append(float(seperator[1]))
    return x,y


if __name__ == '__main__':
    name = input("Filename? ")
    pthFiles = ["model_basic_epoch_5", "model_basic_epoch_10", "model_basic_epoch_15", "model_basic_epoch_20"]
    x = []
    y = []
    for n in pthFiles:
        x.append(averageOfList(n))
        y.append(len(x))
    #plotData(x,y, "Test")
    plt.bar(y,x)
    plt.show()