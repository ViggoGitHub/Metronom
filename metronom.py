import winsound
import time
import tkinter as tk
import threading


class MyGUI:
    def start_metronome(self):
        print("Hello World!")
        self.freq2 = 440
        self.freq1 = 600
        self.duration = 900
        self.beat = 0
        self.bpm2 = 60 / self.bpm1
        self.running = True

        # Starting the metronome in a diferent thread
        self.metronome_thread = threading.Thread(target=self.playing_metronome)
        self.metronome_thread.start()

    def playing_metronome(self):
        while self.running:
            self.beat += 1
            if self.beat == 1:
                winsound.Beep(self.freq1, self.duration)
                time.sleep(self.bpm2)
            else:
                winsound.Beep(self.freq2, self.duration)
                time.sleep(self.bpm2)

            if self.beat == 4:
                self.beat = 0

    def stop_metronome(self):
        self.running = False
        if self.metronome_thread.is_alive():
            self.metronome_thread.join()

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
            self.bpm_label = tk.Label(self.root, text="BPM set at " + str(self.bpm1))
            self.bpm_label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.enter = tk.Button(self.root, text="Enter", command=bpm_entry)
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

        self.stop = tk.Button(
            self.buttonframe,
            text="Stop",
            font=("Arial", 12),
            command=self.stop_metronome,
        )
        self.stop.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.running = False

        self.buttonframe.pack(fill="x", pady=30)

        # to open a window
        self.root.mainloop()


MyGUI()
