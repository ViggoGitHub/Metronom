import winsound
import time

# while True:
#     winsound.PlaySound("click_button.wav", winsound.SND_FILENAME)

freq2 = 440
freq1 = 600
duration = 900
beat = 0
bpm = time.sleep(0.5)

while True:
    beat += 1
    if beat == 1:
        winsound.Beep(freq1, duration)
        bpm
    else:
        winsound.Beep(freq2, duration)
        bpm

    if beat == 4:
        beat = 0
