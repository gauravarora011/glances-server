import csv
import matplotlib.pyplot as plt
from shutil import copyfile

ylabel = ['CPU Process (count)' , 'CPU Percentage(%)' , 'Memory Consuption (%)','Disk Usuage (%)']

def plot_csv(path,j):
    with open(path, "rb") as file:
        cr = csv.reader(file)
        lines = [row for row in cr]
    testList2 = []
    i = 1
    for line in lines[-100:]:
        testList2.append((i,float(line[j-1])))
        i = i + 1
    print(testList2)
    zip(*testList2)
    plt.plot(*zip(*testList2))
    plt.ylabel(ylabel[j-1])
    plt.title(ylabel[j-1])
    plt.xlabel('TIME ---->')
    plt.show()

def buttonPushed(client_name,j):
    path = "C:\\Users\\Gaurav Arora\\Desktop\\csv_folder\\" + client_name +".csv"
    path2 = "C:\\Users\\Gaurav Arora\\Desktop\\csv_folder\\" + client_name + "_temp.csv"
    copyfile(path, path2)
    plot_csv(path2,j)

#buttonPushed('client1',2)