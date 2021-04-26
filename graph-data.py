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
    for e in y1:
        plt.plot(x, e, color='#0D87F2', label = "Original Net") #Net Blue
    for e in y2:
        plt.plot(x, y2, color='#12F00E', label = "DuelQNet") #DQN Green
    #plt.legend(loc=2)
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


if __name__ == '__main__':
    #path = "results/result_rocket_basic_epochs_20_index_3_DuelQNet/"
    #filename = "Nolan_model_rocket_basic_epoch_"
    #path2 = "results/result_rocket_basic_epochs_20_index_4/"
    #filename2 = "Nolan_model_rocket_basic_epoch_"
    default = default_data()
    pathNet = []
    pathDQN = []
    x = 1
    for x in range(1,6):
        l1 = []
        l2 = []
        for i in default.eval_epoch:
            #filename = "results/OGNET_Rocket_Training_"+ str(x) +"/Nolan_model_rocket_basic_epoch_"+str(i)
            #filename2 = "results/DQN_Rocket_Training_"+ str(x)+ "/Nolan_model_rocket_basic_epoch_"+str(i)
            filename = "results/OGNET_Rocket_Training_"+ str(x) +"/Nolan_model_rocket_basic_epoch_"+str(i)
            filename2 = "results/DQN_Rocket_Training_"+ str(x)+ "/Nolan_model_rocket_basic_epoch_"+str(i)
            l1.append(filename)
            l2.append(filename2)
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
    plotData(default.eval_epoch, Net, DQN, "Rocket Basic")
            


    #plotData(default.eval_epoch, Net, DQN,  "Rocket Basic")