import csv
import matplotlib.pyplot as plt
from shutil import copyfile
def plot_csv(path,j):

    labels_data = '0-20%', '20-40%', '40-70%', '70-100%'
    sizes = [0, 0, 0, 0]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode_data = (0.1, 0.05, 0.1, 0.05)

    with open(path, "rb") as file:
        cr = csv.reader(file)
        lines = [row for row in cr]
    testList2 = []
    for line in lines:
        if 0 <= float(line[j-1]) <= 5:
            sizes[0]+=1
        elif 5 < float(line[j-1])<=20 :
            sizes[1] += 1
        elif 20 < float(line[j-1])<= 70:
            sizes[2] += 1
        else:
            sizes[3] += 1
    labels=[]
    size=[]
    explode=[]
    for i in range(0,4):
        if sizes[i]>0:
            size.append(float(sizes[i]))
            labels.append(str(labels_data[i]))
            explode.append(float(explode_data[i]))

    plt.pie(size, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('CPU Percentage')
    plt.show()

def buttonPushed_cpu_pie(client_name):
    path = "C:\\Users\\Gaurav Arora\\Desktop\\csv_folder\\" + client_name +".csv"
    path2 = "C:\\Users\\Gaurav Arora\\Desktop\\csv_folder\\" + client_name + "_temp.csv"
    copyfile(path, path2)
    plot_csv(path2,2)
