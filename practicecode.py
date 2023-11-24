"""
number = 0
index = 0
score = 0

words = []
translation_words = []

language1 = input('Vilket språk vill du översätta från? ')
language2 = input('Vilket språk vill du översätta till? ')
antal = int(input('Hur många glosor vill du öva på? '))

for i in range(antal):
    number += 1 # för varje gång loopen körs så blir nummret på glosan ett högre
    word = input('Skriv glosa '+str(number)+' på '+language1+': ')
    words.append(word)
    translation = input('Skriv glosa '+str(number)+' på '+language2+': ')
    translation_words.append(translation)

for j in range(len(words)):
    # index i guess tar det objekt ur listan som har samma nummer som index har just då.
    guess = input(('Skriv '+words[index]+' på '+language2+': '))
    if guess == translation_words[index]:
        print('Du gissade rätt. Du får ett poäng!')
        score += 1
    else:
        print('Du gissade fel!')
    index += 1

print('Glosförhöret är avklarat!')
print('Du fick '+str(score)+' poäng av totalt '+str(antal)+' poäng!')
"""

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
buttonframe.pack(fil="x")


# to open a window
root.mainloop()
