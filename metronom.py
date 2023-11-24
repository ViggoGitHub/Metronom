import winsound
import time
import tkinter as tk

root = tk.Tk()

root.geometry("900x500")
root.title("Metronome")

label = tk.Label(root, text="Metronome", font=("Arial", 18))
# padx och pady är padding för x och y axel
label.pack(padx=100, pady=20)

label2 = tk.Label(root, text="BPM", font=("Arial", 10))
label2.pack()

entry = tk.Entry(root)
entry.pack()

start = tk.Button(root, text="Start")
start.pack(pady=10)

stop = tk.Button(root, text="Stop")
stop.pack(pady=10)

# to open a window
root.mainloop()

freq2 = 440
freq1 = 600
duration = 900
beat = 0
bpm = time.sleep(0.5)

# while True:
#     beat += 1
#     if beat == 1:
#         winsound.Beep(freq1, duration)
#         bpm
#     else:
#         winsound.Beep(freq2, duration)
#         bpm

#     if beat == 4:
#         beat = 0
