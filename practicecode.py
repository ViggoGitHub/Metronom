# tkinter

import tkinter as tk

root = tk.Tk()

root.geometry("900x500")
root.title("Metronome")

label = tk.Label(root, text="Hej", font=("Arial", 18))
# padx och pady är padding för x och y axel
label.pack(padx=100, pady=20)

# textbox för om användaren vill skriva in någonting
textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack()

# entry för mindre rutor där man bara skriver in något enstaka på en rad
entry = tk.Entry(root)
entry.pack()

buttonframe = tk.Frame(root)
# weight används för att knapparna ska stretcha över hela spannet och inte lämna mellanrum
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

button = tk.Button(root, text="Klicka här!", font=("Arial", 16))
button.pack()

btn1 = tk.Button(buttonframe, text="1", font=("Arial", 16))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 16))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

# fill="x" fyller i x riktning
buttonframe.pack(fill="x")


# to open a window
root.mainloop()
