import csv
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from shutil import copyfile

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
path = None
j = None
def plot_csv(i):
    global path
    global j
    xar = []
    yar = []
    with open(path, "rb") as file:
        cr = csv.reader(file)
        lines = [row for row in cr]
    i = 1
    for line in lines[-12:]:
        xar.append(i)
        yar.append(float(line[j]))
        i = i + 1
    ax1.clear()
    ax1.plot(xar,yar)

def buttonPushed(client_name,i):
    path_original = "C:\\Users\\Gaurav Arora\\Desktop\\csv_folder\\" + client_name +".csv"
    path_temp = "C:\\Users\\Gaurav Arora\\Desktop\\csv_folder\\" + client_name + "_temp.csv"
    copyfile(path_original, path_temp)
    global path
    global j
    j=i
    path = path_temp
    #plot_csv(path2,j)
    ani = animation.FuncAnimation(fig,plot_csv, interval=1000)
    plt.show()

buttonPushed('hello',1)