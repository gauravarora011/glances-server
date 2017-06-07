import time
import csv
from Tkinter import *
import graph
import data_house as dh
import pie_chart as pie

def print_config(c):

    dh.count += 1
    dh.text_label['text'] = "Number of clients connected: " + str(dh.count)
    client_name = c.recv(1024)
    frame2 = Frame(dh.notebook,bg="white",colormap="new")
    frame2.pack(side = TOP)
    dh.notebook.add(frame2, text=client_name+"               ")
    dh.notebook.pack()
    frame2.configure(background="white")
    leftframe = Frame(frame2, height=400, width=200, bg="yellow")
    leftframe.pack_propagate(0)
    leftframe.pack(side=LEFT, expand=True)
    rightframe = Frame(frame2, height=400, width=450, bg="#9ad3de")
    rightframe.pack_propagate(0)
    rightframe.pack(side=RIGHT, expand=True)
    S = Scrollbar(leftframe)
    T = Text(leftframe, height=350, width=200,font=("Impact",10))
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.config(state=DISABLED)
    time.sleep(1)
    #bottomframe = Frame(root,width=768, height=576,bg="white",colormap="new")
    #bottomframe.pack(side=TOP)
    #bottomframe.configure(background="white")
    frameup = Frame(rightframe, height=60, width=450, bg='#EEEEEE')
    # frameup.pack_propagate(0)
    frameup.pack(side=TOP)
    framemid1 = Frame(rightframe, height=60, width=450, bg='#EEEEEE')
    # framedown.pack_propagate(0)
    framemid1.pack(side=TOP)
    framemid2 = Frame(rightframe, height=60, width=450, bg='#EEEEEE')
    # frameup.pack_propagate(0)
    framemid2.pack(side=TOP)
    framedown = Frame(rightframe, height=60, width=450, bg='#EEEEEE')
    # framedown.pack_propagate(0)
    framedown.pack(side=TOP)

    frameCPU = Frame(frameup, height=60, width=200, bg='#EEEEEE')
    frameCPU.pack_propagate(0)
    frameCPUs = Frame(frameup, height=60, width=250, bg='#EEEEEE')
    frameCPUs.pack_propagate(0)
    frameCPU.pack(side=LEFT, expand=True)
    frameCPUs.pack(side=RIGHT, expand=True)

    frameCPU2 = Frame(framemid1, height=60, width=200, bg='#EEEEEE')
    frameCPU2.pack_propagate(0)
    frameCPU2.pack(side=LEFT, expand=True)
    frameCPU2s = Frame(framemid1, height=60, width=250, bg='#EEEEEE')
    frameCPU2s.pack_propagate(0)
    frameCPU2s.pack(side=RIGHT, expand=True)

    frameMEM = Frame(framemid2, height=60, width=200, bg='#EEEEEE')
    frameMEM.pack_propagate(0)
    frameMEM.pack(side=LEFT, expand=True)
    frameMEMs = Frame(framemid2, height=60, width=250, bg='#EEEEEE')
    frameMEMs.pack_propagate(0)
    frameMEMs.pack(side=RIGHT, expand=True)

    frameDISK = Frame(framedown, height=60, width=200, bg='#EEEEEE')
    frameDISK.pack_propagate(0)
    frameDISK.pack(side=LEFT, expand=True)
    frameDISKs = Frame(framedown, height=60, width=250, bg='#EEEEEE')
    frameDISKs.pack_propagate(0)
    frameDISKs.pack(side=RIGHT, expand=True)

    label1 = Label(frameCPU, text="Process count: ", font="Verdana 12 bold", bg='#EEEEEE',pady=15)
    label1.pack(side=TOP)
    w = Scale(frameCPUs, from_=0, to=200, orient=HORIZONTAL, length=220, tickinterval=25,bg='#818283',fg="white")
    w.pack()

    label2 = Label(frameCPU2, text="CPU Percentage: ", font="Verdana 12 bold", pady=15, bg='#EEEEEE')
    label2.pack(side=TOP)
    r = Scale(frameCPU2s, from_=0, to=100, orient=HORIZONTAL, length=220, tickinterval=10, bg='#818283')
    r.pack()

    label3 = Label(frameMEM, text="Memory Percentage: ", font="Verdana 12 bold", pady=15, bg='#EEEEEE')
    label3.pack(side=TOP)
    s = Scale(frameMEMs, from_=0, to=100, orient=HORIZONTAL, length=220, tickinterval=10, bg='#818283',fg="white")
    s.pack()

    label4 = Label(frameDISK, text="Disk Percentage: ", font="Verdana 12 bold", pady=15, bg='#EEEEEE')
    label4.pack(side=TOP)
    x = Scale(frameDISKs, from_=0, to=100, orient=HORIZONTAL, length=220, tickinterval=10, bg='#818283')
    x.pack()

    framelabel = Frame(rightframe, height=30, width=450, bg='#89bdd3')
    framelabel.pack_propagate(0)
    framelabel.pack(side=TOP)
    label4 = Label(framelabel, text="GRAPH FUNCTIONS", font="Arial 14 bold", pady=10, bg='#e3e3e3')
    label4.pack(side=TOP)

    framegraph = Frame(rightframe, height=50, width=450, bg="white")
    framegraph.pack_propagate(0)
    framegraph.pack(side=TOP)

    framegraph1 = Frame(framegraph, height=50, width=112, bg='#9ad3de',borderwidth=5)
    framegraph1.pack_propagate(0)
    framegraph1.pack(side=LEFT)
    framegraph2 = Frame(framegraph, height=50, width=112, bg='#9ad3de',borderwidth=5)
    framegraph2.pack_propagate(0)
    framegraph2.pack(side=LEFT)
    framegraph3 = Frame(framegraph, height=50, width=112, bg='#9ad3de',borderwidth=5)
    framegraph3.pack_propagate(0)
    framegraph3.pack(side=LEFT)
    framegraph4 = Frame(framegraph, height=50, width=112, bg='#9ad3de',borderwidth=5)
    framegraph4.pack_propagate(0)
    framegraph4.pack(side=LEFT)

    button1 = Button(framegraph1, text="Process count", command=lambda: graph.buttonPushed(client_name,1), height=40, width=100,bg="white")
    button1.pack_propagate(0)
    button1.pack(side=LEFT)
    button2 = Button(framegraph2, text="CPU percentage", command=lambda: graph.buttonPushed(client_name,2), height=40,width=100,bg="white")
    button2.pack_propagate(0)
    button2.pack(side=LEFT)
    button3 = Button(framegraph3, text="Memory Per", command=lambda: graph.buttonPushed(client_name,3), height=40,width=100,bg="white")
    button3.pack_propagate(0)
    button3.pack(side=LEFT)
    button4 = Button(framegraph4, text="Disk percentage", command=lambda: graph.buttonPushed(client_name,4), height=40,width=100,bg="white")
    button4.pack_propagate(0)
    button4.pack(side=LEFT)

    framepie = Frame(rightframe, height=50, width=200, bg='#9ad3de')
    framepie.pack_propagate(0)
    framepie.pack(side=TOP)
    buttonpie = Button(framepie, text="Pie Chart", command=lambda: pie.buttonPushed_cpu_pie(client_name), height=50,width=90, bg="white")
    buttonpie.pack_propagate(0)
    buttonpie.pack(side=LEFT)
    path = "C:\\Users\\Gaurav Arora\\Desktop\\csv_folder\\" + client_name + ".csv"
    """#plot_csv(path)
data_file = open(path, 'ab')
data_file.truncate()
data_file.close()"""
    t = 0
    k = 0
    while True:
        lst = c.recv(1024).split()
        cpu = lst[0]
        cpu2 = lst[1]
        mem = lst[2]
        disk = lst[3]

        k=k+1
        data_file = open(path, 'ab')
        writer = csv.writer(data_file, dialect='excel')
        writer.writerow(lst)
        data_file.close()

        w.config(state=NORMAL)
        r.config(state=NORMAL)
        s.config(state=NORMAL)
        x.config(state=NORMAL)
        # label5.config(text=cpu)
        w.set(cpu)
        # label6.config(text=cpu2)
        r.set(cpu2)
        # label7.config(text=mem)
        s.set(mem)
        # label8.config(text=disk)
        x.set(disk)
        w.config(state=DISABLED)
        r.config(state=DISABLED)
        s.config(state=DISABLED)
        x.config(state=DISABLED)
        t = t + 1
        if t == 4:
            l=((k/4-1)*6+1)
            T.config(state=NORMAL)
            T.insert(END , time.strftime('%X  %x -\t\t\t     \n'))
            T.tag_add("t"+str(k), str(l)+".0", str(l)+".40")
            T.tag_config("t"+str(k), background='#459ec3', foreground="white")
            T.insert(END ,"No. of CPU Cores:" + cpu + "\nCPU Percentage:" + cpu2 + "\nMemory Percentage" + mem + "\nDisk Percentage:" + disk + "\n\n")
            T.config(state=DISABLED)
            t = 0
        time.sleep(2)
