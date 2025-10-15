from tkinter import *
import speech_recognition as sr
from tkinter.filedialog import *
from tkinter import messagebox
root = Tk()
root.geometry("700x700")
root.title("Translate Speech to Text")
Label(root, text="Voice notepad").place(x=620, y=620)
textoutput = Text(root, width="60", height="4")
textoutput.place(x=100, y=100)
def startspeak():
    a = sr.Recognizer() #initialize Recognizer tool.
    with sr.Microphone() as source: #storage where your voice are fetched onto
        Label(root, text="Please start speaking..").place(x=100, y=400)
        audio=a.listen(source)
        try:
            text=a.recognize_google(audio)
        except:
            text="Error 404:Couldn't recognize your voice-"
        textoutput.delete(1.0, END)
        textoutput.insert(END, text)
def savetext():
    filee = asksaveasfile(defaultextension=".txt")
    if filee:
        print(textoutput.get(1.0, END), file=filee)
    else:
        messagebox.showwarning("Warning", "Text not saved.")

Label(root, text="Voice output").place(x=200, y=50)
Button(root, text="Save", command=savetext).place(x=320, y=100)
Button(root, text="Speak", command=startspeak).place(x=320, y=320)

root.mainloop()