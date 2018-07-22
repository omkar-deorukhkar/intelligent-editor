# Omkar Deorukhkar

from tkinter import *
from tkinter import filedialog
import speech_recognition as sr
import pyaudio
from gtts import gTTS
import playsound
import pyttsx3
from recorder import record_audio
from googletrans import Translator


fname = ''


root = Tk()
root.title("Intelligent-Editor")
root.configure(background='black')
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
root.wm_iconbitmap("magichat.ico")

txt = Text(root, width=500, height=500, background='gray20', foreground='floral white',font='Arial 14 bold')
txt.pack()
translator = Translator()



def NewFile():
    global fname
    fname='Untitled'
    txt.delete(0.0,END)
    
def Openfile():
    global fname
    fname = filedialog.askopenfilename()
    f = open(fname,mode='r')
    root.title("Omkar-text_editor  "+fname)
    t = f.read()
    txt.delete(0.0, END)
    txt.insert(0.0,t)

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
    print(fname)
    if fname=='':
        Sas()
    else:
        f = open(fname,'w')
        f.write(t)
        f.close()
    
def sp_recog():
    '''global fname
    if fname=='':
        fwrap=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        fname = str(fwrap.name)'''
    r = sr.Recognizer()
    audio = filedialog.askopenfilename()
    with sr.AudioFile(audio) as source:
        txt_audio = r.record(source)
    t=(str(r.recognize_google(txt_audio)))
    txt.insert(END,t)
    

def mic():
    record_audio()
    r = sr.Recognizer()
    audio = "C:\\Users\\Omkar\\Desktop\\file.wav"
    with sr.AudioFile(audio) as source:
        txt_audio = r.record(source)
    t=(str(r.recognize_google(txt_audio)))
    txt.insert(END,t)
    
    
def narrate():
    engine = pyttsx3.init(driverName='sapi5');
    t = txt.get(0.0,END)
    engine.setProperty('rate', 120)
    engine.say(t);
    engine.runAndWait() ;
    
def convert():
    record_audio()
    r = sr.Recognizer()
    audio = "C:\\Users\\Omkar\\Desktop\\file.wav"
    with sr.AudioFile(audio) as source:
        txt_audio = r.record(source)
    t=(str(r.recognize_google(txt_audio)))
    a=translator.translate(t,src='en',dest='hi')
    txt.insert(END,a.text)
    

    
    

mbar = Menu(root)
menc = Menu(mbar)
menc.add_command(label ="New File", command=NewFile)
menc.add_command(label ="Open File", command=Openfile)
menc.add_command(label ="Save As", command=Sas)
menc.add_command(label ="Save File", command=save_f)
menc.add_command(label ="Audio Mode", command=sp_recog)
menc.add_command(label ="Microphone Mode", command=mic)
menc.add_command(label ="Narrate", command=narrate)
menc.add_command(label ="Hindi Coverter", command=convert)
#menc.add_command(label ="Close", command=root.close)

mbar.add_cascade(label='Menu', menu=menc)

root.config(menu=mbar)
print(fname)
root.mainloop()

