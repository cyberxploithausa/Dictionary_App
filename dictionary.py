from tkinter import *
from PyDictionary import PyDictionary

root = Tk()
root.geometry('300x350')
root.title('Cyber Dictionary')

def nemo_maana():
    kalma = entry.get()
    dictionary = PyDictionary(kalma)
    maana = dictionary.printMeanings()
    print(maana)

entry = Entry(root, font=("times", 15, "bold"))
entry.pack(pady=20)

btn = Button(root, text="Nemo Ma`ana", command=nemo_maana)
btn.pack(pady=20)


label = Label(root, font=('Arial', 15, "bold"))
label.pack(pady=20)

root.mainloop()
