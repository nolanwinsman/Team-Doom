from matplotlib import pyplot as plt




def plotData(listX, listY):
    plt.plot(listX, listY)
    plt.title("Reward Per Episode")
    plt.xlabel("Episodes")
    plt.ylabel("Reward")
    plt.show()
def loadInData():
    print("This function will laod in the data in each result.txt file and make a list of x coordinates and y coordinates")
    x = []
    y = []
    return x,y


if __name__ == '__main__':
    x = [0, 1, 2]
    y = [4, 8, 2]
    plotData(x,y)