import tkinter as tk

window=tk.Tk()
window.geometry("500x500")

def button_Chng():
    button_clr=button.cget("bg")
    if(button_clr=="red"):
        button.config(bg="green")
    else:
        button.config(bg="red")




button=tk.Button(window,text="Click me",bg="red", command=button_Chng)
button.pack()

window.mainloop()