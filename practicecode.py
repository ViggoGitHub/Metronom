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
label.pack()

# to open a window
root.mainloop()
