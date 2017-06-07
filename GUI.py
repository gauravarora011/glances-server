from Tkinter import *
import ttk
import data_house as dh
from PIL import ImageTk, Image

def GUI():
    dh.root = Tk()
    dh.root.iconbitmap(default='transparent.ico')
    dh.root.wm_title("Server ~ Glances 'An Eye On Your Netwrok'")
    dh.root.geometry('650x500')
    dh.root.configure(background = 'white')
    dh.root.resizable(width=False, height=False)
    #logo = PhotoImage(file="C:\Users\Gaurav Arora\Downloads\server_cover.gif")
    dh.topframe = Frame(dh.root,height = 100 ,width = 650, bg='#89bdd3', pady=10)
    dh.topframe.pack_propagate(0)
    dh.topframe.pack(side=TOP,expand=True)

    dh.text_label = Label(dh.topframe,text = "Number of clients connected: " + str(dh.count),font=("Trebuchet MS", 12), bg="#e3e3e3",pady = 10)
    dh.text_label.pack(side=TOP)
    bottomframe = Frame(dh.root,height = 400,width = 650,bg="white")
    bottomframe.pack_propagate(0)
    bottomframe.pack(side=TOP)
    dh.notebook = ttk.Notebook(bottomframe)
    frame1 = Frame(dh.notebook, height=400, width=650, bg="white")
    frame1.pack_propagate(0)
    frame1.pack(side = LEFT)
    dh.notebook.add(frame1, text='Home      ')
    dh.notebook.pack(side=TOP)

    img = ImageTk.PhotoImage(Image.open("image.jpg"))
    panel = Label(frame1, image=img)
    panel.pack(side=LEFT)

    """Combo_box = ttk.Combobox(frame1)
    Combo_box['values'] = client_list
    Combo_box.pack(side=LEFT)
    Combo_box.set(" ")
    label1 = Label(topframe, text="Check your system config  ")
    label1.pack(side=LEFT)
    button1 = Button(topframe, text="Display", command=buttonPushed)
    button1.pack(side=RIGHT)"""

    dh.root.mainloop()    