from tkinter import *
from tkinter import filedialog

fname = ''


root = Tk()
root.title("Omkar")
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

txt = Text(root, width=500, height=500)
txt.pack()

def NewFile():
    global fname
    fname='Untitled'
    txt.delete(0.0,END)
    
def Openfile():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    txt.delete(0.0, END)
    txt.insert(0.0,t)
    fname = f
def Sas():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    print(f)
    t = txt.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Error!!",message="Could not Save File")
        
def save_f():
    global fname
    t = txt.get(0.0,END)
    f = open(fname,'w')
    f.write()
    f.close()





mbar = Menu(root)
menc = Menu(mbar)
menc.add_command(label ="New File", command=NewFile)
menc.add_command(label ="Open File", command=Openfile)
menc.add_command(label ="Save As", command=Sas)
menc.add_command(label ="Save File", command=save_f)
menc.add_command(label ="Close", command=root.quit)

mbar.add_cascade(label='Menu', menu=menc)

root.config(menu=mbar)
root.mainloop()

