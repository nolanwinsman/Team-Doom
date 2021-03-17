from matplotlib import pyplot as plt



def plotData(listX, listY):
    plt.plot(listX, listY)
    plt.title("Reward Per Episode")
    plt.xlabel("Episodes")
    plt.ylabel("Reward")
    plt.show()
def loadInData():
    x = []
    y = []
    file = open(r"results/results1.txt", "r")
    for line in file:
        seperator = line.split(",")
        x.append(float(seperator[0]))
        y.append(float(seperator[1]))
    return x,y


if __name__ == '__main__':
    x, y = loadInData()
    plotData(x,y)