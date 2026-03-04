import  tkinter as tk

def button_click():
    print("button clicked")
    label1.config(bg="red")
    label2.config(bg="red")

    button.config(bg="red")

    print("YOU clicked", entry.get())


window = tk.Tk()
window.title("MY FIRST GUI APP")
window.geometry("1200x1400")
label1 = tk.Label(window, text="hlo,tkinter!",font=("Arial", 20),bg="green")
label1.pack()
label2 = tk.Label(window, text="hi,tinker!",font=("Arial", 30),bg="black")
label2.pack()

label3 = tk.Label(window, text="bye,tkinter!",font=("Arial", 40),bg="blue")
label3.pack()

label4 = tk.Label(window, text="ok,tkinter!",font=("Letter Gothic ", 50),bg="orange")
label4.pack()


button=tk.Button(window,text="Click here", command= button_click)
button.pack()

entry=tk.Entry(window, width=50, text="HI")
entry.pack()




window.mainloop()