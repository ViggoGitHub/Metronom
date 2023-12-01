import winsound
import time
import tkinter as tk


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("400x400")
        self.root.title("Metronome")

        self.label = tk.Label(self.root, text="Metronome", font=("Arial", 18))
        # padx och pady är padding för x och y axel
        self.label.pack(padx=100, pady=20)

        self.label2 = tk.Label(self.root, text="BPM", font=("Arial", 16))
        self.label2.pack()

        def bpm_entry():
            self.bpm1 = int(self.entry.get())

        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.enter = tk.Button(self.root, text="Ange", command=bpm_entry)
        self.enter.pack(pady=10)

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

    def start_metronome(self, stop):
        print("Hello World!")
        self.freq2 = 440
        self.freq1 = 600
        self.duration = 900
        self.beat = 0
        self.bpm2 = 60 / self.bpm1

        while not stop:
            self.beat += 1
            if self.beat == 1:
                winsound.Beep(self.freq1, self.duration)
                time.sleep(self.bpm2)
            else:
                winsound.Beep(self.freq2, self.duration)
                time.sleep(self.bpm2)

            if self.beat == 4:
                self.beat = 0


MyGUI()
