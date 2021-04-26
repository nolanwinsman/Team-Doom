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
    plt.plot(x, y1, color='#0D87F2', label = "Original Net") #Net Blue
    plt.plot(x, y2, color='#12F00E', label = "DuelQNet") #DQN Green
    plt.legend(loc=2)
    plt.title(title)
    plt.xlabel("Epoch")
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
    #path = "results/result_rocket_basic_epochs_20_index_3_DuelQNet/"
    #filename = "Nolan_model_rocket_basic_epoch_"
    #path2 = "results/result_rocket_basic_epochs_20_index_4/"
    #filename2 = "Nolan_model_rocket_basic_epoch_"

    pathNet = []
    pathDQN = []
    x = 1
    for x in range(1,6):
        for i in default.eval_epoch:
            pathNet.append("results/DQN_Rocket_Training_"+ str(x)+ "/Nolan_model_rocket_basic_epoch_"+str(i))
            pathDQN.append("results/OGNET_Rocket_Training_"+ str(x) +"/Nolan_model_rocket_basic_epoch_"+str(i))
            x += 5
    print("Path: ")
    print(pathDQN)


    default = default_data()
    Net = []
    DQN = []
    for n in default.eval_epoch:
        Net.append(averageOfList(pathNet[n]))
        DQN.append(averageOfList(pathDQN[n]))
    #print(Net)
    #print(DQN)


    #plotData(default.eval_epoch, Net, DQN,  "Rocket Basic")