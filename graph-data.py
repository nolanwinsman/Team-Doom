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

def plotData(x, y1, y2, title):
    plt.plot(x, y1[0], color='#0D87F2', label = "Original Net") #Net Blue
    plt.plot(x, y2[0], color='#12F00E', label = "DuelQNet") #DQN Green
    plt.scatter(x, y1[0], color='#0D87F2') #Net Blue
    plt.scatter(x, y2[0], color='#12F00E') #DQN Green

    print("OGNet Epoch: " + "1 " + str(y1[0]))
    print("DQN   Epoch: " + "1 " + str(y2[0]))

    for i in range(1,len(y1)):
        plt.plot(x, y1[i], color='#0D87F2') #Net Blue
        plt.plot(x, y2[i], color='#12F00E') #DQN Green
        plt.scatter(x, y1[i], color='#0D87F2') #Net Blue
        plt.scatter(x, y2[i], color='#12F00E') #DQN Green

        print("OGNet Epoch: " + str(default.eval_epoch[i]) +" " + str(y1[i]))
        print("DQN   Epoch: " + str(default.eval_epoch[i]) +" " + str(y2[i]))
        
    plt.legend(loc=2)
    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel("Average Reward")
    plt.show()

def plotDataAvg(x, y1, y2, title):
    val1 = []
    val2 = []
    title = "Average " + title
    for i in range(0,len(y1)):
        temp1 = []
        temp2 = []
        for j in range(0,len(y1[i])):
            temp1.append(y1[j][i])
            temp2.append(y2[j][i])
        val1.append(np.average(temp1))
        val2.append(np.average(temp2))

    plt.plot(x, val1, color='#0D87F2', label = "Original Net Avg") #Net Blue
    plt.plot(x, val2, color='#12F00E', label = "DuelQNet Avg") #DQN Green
    plt.scatter(x, val1, color='#0D87F2') #Net Blue
    plt.scatter(x, val2, color='#12F00E') #DQN Green
        
    plt.legend(loc=2)
    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel("Average Reward")
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


default = default_data()


if __name__ == '__main__':
    pathNet = []
    pathDQN = []
    title = "Rocket Basic"
    print(title)

    #rocket basic
    rocket_basic = []
    rocket_basic.append("results/OGNET_Rocket_Training_")
    rocket_basic.append("results/DQN_Rocket_Training_")
    rocket_basic.append("/Nolan_model_rocket_basic_epoch_")
    rocket_basic.append("/Nolan_model_rocket_basic_epoch_")

    #deadly corridor
    deadly_corridor = []
    deadly_corridor.append("results/OGNET_Deadly_Training_")
    deadly_corridor.append("results/DQN_Deadly_Training_")
    deadly_corridor.append("/Nolan_model_deadly_corridor_epoch_")
    deadly_corridor.append("/Nolan_model_deadly_corridor_epoch_")

    #Take Cover
    take_cover = []
    take_cover.append("results/OGNET_Cover_Training_")
    take_cover.append("results/null")
    take_cover.append("/Ethan_model_take_cover_epoch_")
    take_cover.append("/null")

    #Health Gathering
    health_gathering = []
    health_gathering.append("results/OGNET_HealthSimple_Training_")
    health_gathering.append("results/DQN_HealthSimple_Training_")
    health_gathering.append("/Ethan_model_health_gathering_epoch_")
    health_gathering.append("/Nolan_model_health_gathering_epoch_")

    toChoose = rocket_basic
    x = 1
    for x in range(1,6):
        l1 = []
        l2 = []
        for i in default.eval_epoch:
            l1.append(toChoose[0] + str(x) + toChoose[2] + str(i))
            l2.append(toChoose[1] + str(x) + toChoose[3] + str(i))
        pathNet.append(l1)
        pathDQN.append(l2)
    Net = []
    DQN = []
    for x in range(0,5):
        l1 = []
        l2 = []
        for i in range(len(default.eval_epoch)):
            l1.append(averageOfList(pathNet[x][i]))
            l2.append(averageOfList(pathDQN[x][i]))
        Net.append(l1)
        DQN.append(l2)
    #plotData(default.eval_epoch, Net, DQN, title)
    plotDataAvg(default.eval_epoch, Net, DQN, title)
            