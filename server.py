import time
import socket
import thread
import csv
import matplotlib.pyplot as plt
from Tkinter import *
import ttk
from shutil import copyfile

root = None
topframe= None
Combo_box= None
notebook = None
client_list = []
count = 0
text_label = None

def plot_csv(path):
    with open(path, "rb") as file:
        cr = csv.reader(file)
        lines = [row for row in cr]
    testList2 = []
    i = 1
    for line in lines[-12:]:
        testList2.append((i,(float(line[0]),float(line[1]),float(line[2]),float(line[3]))))
        i = i + 1
    print(testList2)
    zip(*testList2)
    plt.plot(*zip(*testList2))
    plt.show()

def print_config(c):
    global root
    global notebook
    global Combo_box
    global client_list
    global count
    global text_label

    count = count + 1

    text_label['text'] = "Number of clients connected: " + str(count)
    client_name = c.recv(1024)
    frame2 = Frame(notebook,bg="white",colormap="new")
    frame2.pack(side = TOP)
    notebook.add(frame2, text=client_name)
    notebook.pack()
    frame2.configure(background="white")
    leftframe = Frame(frame2, height=400, width=200, bg="yellow")
    leftframe.pack_propagate(0)
    leftframe.pack(side=LEFT, expand=True)
    rightframe = Frame(frame2, height=400, width=450, bg="white")
    rightframe.pack_propagate(0)
    rightframe.pack(side=RIGHT, expand=True)
    S = Scrollbar(leftframe)
    T = Text(leftframe, height=350, width=200)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    time.sleep(1)
    #bottomframe = Frame(root,width=768, height=576,bg="white",colormap="new")
    #bottomframe.pack(side=TOP)
    #bottomframe.configure(background="white")
    frameup = Frame(rightframe, height=60, width=450)
    #frameup.pack_propagate(0)
    frameup.pack(side=TOP)
    framemid1 = Frame(rightframe, height=60, width=450)
    #framedown.pack_propagate(0)
    framemid1.pack(side=TOP)
    framemid2 = Frame(rightframe, height=60, width=450)
    # frameup.pack_propagate(0)
    framemid2.pack(side=TOP)
    framedown = Frame(rightframe, height=60, width=450)
    # framedown.pack_propagate(0)
    framedown.pack(side=TOP)

    frameCPU = Frame(frameup, height=60, width=200)
    frameCPU.pack_propagate(0)
    frameCPUs = Frame(frameup, height=60, width=250)
    frameCPUs.pack_propagate(0)
    frameCPU.pack(side=LEFT, expand=True)
    frameCPUs.pack(side=RIGHT, expand=True)

    frameCPU2 = Frame(framemid1, height=60, width=200)
    frameCPU2.pack_propagate(0)
    frameCPU2.pack(side=LEFT, expand=True)
    frameCPU2s = Frame(framemid1, height=60, width=250)
    frameCPU2s.pack_propagate(0)
    frameCPU2s.pack(side=RIGHT, expand=True)

    frameMEM = Frame(framemid2, height=60, width=200)
    frameMEM.pack_propagate(0)
    frameMEM.pack(side=LEFT, expand=True)
    frameMEMs = Frame(framemid2, height=60, width=250)
    frameMEMs.pack_propagate(0)
    frameMEMs.pack(side=RIGHT, expand=True)

    frameDISK = Frame(framedown, height=60, width=200)
    frameDISK.pack_propagate(0)
    frameDISK.pack(side=LEFT, expand=True)
    frameDISKs = Frame(framedown, height=60, width=250)
    frameDISKs.pack_propagate(0)
    frameDISKs.pack(side=RIGHT, expand=True)

    label1 = Label(frameCPU, text="CPU count: ",font = "Verdana 12 bold",pady= 15,bg="white")
    label1.pack(side=TOP)
    w = Scale(frameCPUs, from_=0, to=100, orient=HORIZONTAL,length=220,tickinterval=10,bg="white")
    w.pack()

    label2 = Label(frameCPU2, text="CPU percentage: ",font = "Verdana 12 bold",pady= 15,bg="white")
    label2.pack(side=TOP)
    r = Scale(frameCPU2s, from_=0, to=100, orient=HORIZONTAL,length=220,tickinterval=10,bg="white")
    r.pack()

    label3 = Label(frameMEM, text="Memory Percentage: ",font = "Verdana 12 bold",pady= 15,bg="white")
    label3.pack(side=TOP)
    s = Scale(frameMEMs, from_=0, to=100, orient=HORIZONTAL,length=220,tickinterval=10,bg="white")
    s.pack()

    label4 = Label(frameDISK, text="Disk percentage: ",font = "Verdana 12 bold",pady= 15,bg="white")
    label4.pack(side=TOP)
    x = Scale(frameDISKs, from_=0, to=100, orient=HORIZONTAL,length=220,tickinterval=10,bg="white")
    x.pack()

    framegraph = Frame(rightframe, height=90, width=450, bg="blue")
    framegraph.pack_propagate(0)
    framegraph.pack(side=TOP)
    button1 = Button(framegraph, text="Generate Graph", command=lambda: buttonPushed(client_name),height=60, width=450, bg="white")
    button1.pack(side=TOP)
    path = "C:\\Users\\Abhishek Singla\\Desktop\\csv_folder\\" + client_name + ".csv"
    """#plot_csv(path)
data_file = open(path, 'ab')
data_file.truncate()
data_file.close()"""
    t=0
    while True:
        lst = c.recv(1024).split()
        cpu = lst[0]
        cpu2 = lst[1]
        mem = lst[2]
        disk = lst[3]
        #print(lst[1])
        data_file = open(path, 'ab')
        writer = csv.writer(data_file, dialect='excel')
        writer.writerow(lst)
        data_file.close()
        # label5.config(text=cpu)
        w.set(cpu)
        # label6.config(text=cpu2)
        r.set(cpu2)
        # label7.config(text=mem)
        s.set(mem)
        # label8.config(text=disk)
        x.set(disk)
        t=t+1
        if t==10:
            T.insert(END, time.strftime('%X %x - \n'))
            T.insert(END, "No. of CPU Cores:"+cpu+"\nCPU Percentage:"+cpu2+"\nMemory Percentage"+mem+"\nDisk Percentage:"+disk+"\n\n")
            t=0
        time.sleep(2)

def buttonPushed(client_name):
    path = "C:\\Users\\Abhishek Singla\\Desktop\\csv_folder\\" + client_name +".csv"
    path2 = "C:\\Users\\Abhishek Singla\\Desktop\\csv_folder\\" + client_name + "_temp.csv"
    copyfile(path, path2)
    plot_csv(path2)
    print "hi"


def connection():
    s = socket.socket()
    host = socket.gethostname()
    port = 12348
    s.bind((host, port))
    s.listen(10)
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        c.send('Thank you for connecting')
        thread.start_new_thread(print_config, (c,))

def GUI():
    global root
    global Combo_box
    global topframe
    global client_list
    global notebook
    global count
    global text_label
    root = Tk()
    root.wm_title("SERVER")
    root.geometry('650x500')
    root.configure(background = 'white')
    root.resizable(width=False, height=False)
    logo = PhotoImage(file="C:\Users\Abhishek Singla\Downloads\server_cover.gif")
    topframe = Frame(root,height = 100 ,width = 650, bg="red",pady=10)
    topframe.pack_propagate(0)
    topframe.pack(side=TOP,expand=True)
    text_label = Label(topframe,text = "Number of clients connected: " + str(count),font=("Helvetica", 12), bg="white",pady = 10)
    text_label.pack(side=TOP)
    bottomframe = Frame(root,height = 400,width = 650,bg="green")
    bottomframe.pack_propagate(0)
    bottomframe.pack(side=TOP)
    notebook = ttk.Notebook(bottomframe)
    frame1 = Frame(notebook, height=400, width=650, bg="white")
    frame1.pack_propagate(0)
    frame1.pack(side = LEFT)
    notebook.add(frame1, text='+')
    notebook.pack(side=TOP)

    """Combo_box = ttk.Combobox(frame1)
    Combo_box['values'] = client_list
    Combo_box.pack(side=LEFT)
    Combo_box.set(" ")
    label1 = Label(topframe, text="Check your system config  ")
    label1.pack(side=LEFT)
    button1 = Button(topframe, text="Display", command=buttonPushed)
    button1.pack(side=RIGHT)"""
    root.mainloop()


al =0
thread.start_new_thread(connection, ())
thread.start_new_thread(GUI, ())
print("Hello")
time.sleep(1000)