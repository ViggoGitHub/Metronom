import winsound
import time
import tkinter as tk


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("900x500")
        self.root.title("Metronome")

        self.label = tk.Label(self.root, text="Metronome", font=("Arial", 18))
        # padx och pady är padding för x och y axel
        self.label.pack(padx=100, pady=20)

        self.label2 = tk.Label(self.root, text="BPM", font=("Arial", 16))
        self.label2.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.buttonframe = tk.Frame(self.root)

        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        self.start = tk.Button(
            self.buttonframe,
            text="Start",
            font=("Arial", 12),
            command=self.start_metronome,
        )
        self.start.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.stop = tk.Button(self.buttonframe, text="Stop", font=("Arial", 12))
        self.stop.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.buttonframe.pack(fill="x", pady=30)

        # to open a window
        self.root.mainloop()

    def start_metronome(self):
        print("Hello World!")
        self.freq2 = 440
        self.freq1 = 600
        self.duration = 900
        self.beat = 0
        self.bpm = 0.5

        while True:
            self.beat += 1
            if self.beat == 1:
                winsound.Beep(self.freq1, self.duration)
                time.sleep(self.bpm)
            else:
                winsound.Beep(self.freq2, self.duration)
                time.sleep(self.bpm)

            if self.beat == 4:
                self.beat = 0


MyGUI()
