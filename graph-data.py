from matplotlib import pyplot as plt



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
    x, y = loadInData(name)
    plotData(x,y, "Defend The Center")