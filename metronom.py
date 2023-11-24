import winsound
import time
import tkinter as tk

root = tk.Tk()

root.geometry("900x500")
root.title("Metronome")

label = tk.Label(root, text="Metronome", font=("Arial", 18))
# padx och pady är padding för x och y axel
label.pack(padx=100, pady=20)

label2 = tk.Label(root, text="BPM", font=("Arial", 16))
label2.pack()

entry = tk.Entry(root)
entry.pack()

buttonframe = tk.Frame(root)

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

start = tk.Button(buttonframe, text="Start", font=("Arial", 12))
start.grid(row=0, column=0, sticky=tk.W + tk.E)

stop = tk.Button(buttonframe, text="Stop", font=("Arial", 12))
stop.grid(row=0, column=1, sticky=tk.W + tk.E)

buttonframe.pack(fill="x", pady=15)

# to open a window
root.mainloop()

freq2 = 440
freq1 = 600
duration = 900
beat = 0
bpm = 0.5

while True:
    beat += 1
    if beat == 1:
        winsound.Beep(freq1, duration)
        time.sleep(bpm)
    else:
        winsound.Beep(freq2, duration)
        timetsleep(bpm)

    if beat == 4:
        beat = 0
