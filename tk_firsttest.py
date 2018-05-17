from tkinter import *
#import messagebox
def antwort():
    messagebox.showinfo('Hier nicht!','Hier auch nicht!')

root=Tk()
but=Button(root,text="Wo ist Tommy?",command=antwort)
but.pack()
root.mainloop()
