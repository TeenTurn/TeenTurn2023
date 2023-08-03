# IMPORTING PACKAGES THAT WE WILL USE LATER ON
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import sounddevice as sd
from secret_chords import get_signal

# DEFINING SIGNALS THAT WILL COMBINE TO MAKE ONE SIGNAL WHICH WILL BE PLOTTED AND PLAYED

# Load the secret signals from a secret folder
signal1 = get_signal(1)
signal2 = get_signal(2)
signal3 = get_signal(3)
signals = signal1 + signal2 + signal3

# Defining the number of times per second that a sample from our signal will be taken
fs = 10000  # sampling frequency

# Defining how long our signal will last (in seconds)
signal_duration = 1

# Defining how many samples the signal will last for
step_size1 = 0.0001  # 0.1ms

# In order to plot the signal we need to define an array for time
t1 = np.arange(0, signal_duration, step_size1)

# PLAY THE SIGNALS INDIVIDUALLY
# Increasing the sampling frequency to help the recording sound better
fs_high = 48000

print("Playing the first note")
sd.play(signal1, fs_high)
sd.wait()

print("Playing the second note")
sd.play(signal2, fs_high)
sd.wait()

print("Playing the third note")
sd.play(signal3, fs_high)
sd.wait()

print("Playing the chord")
sd.play(signals, fs_high)
sd.wait()

# CALCULATING THE SPECTRUM FOR EACH SIGNAL

# Explanation
# In order for us to see which notes are playing on the piano, we need to see which frequencies are dominating the signal. 
# When we calculate the spectrum of each signal we show which frequencies (or sine waves with certain frequencies) work 
# together to create the chord.

N = len(signal1)
spectrum1 = np.abs(fft(signal1)[:N//2])
frequencies1 = fftfreq(N, 1/fs)[:N//2]

spectrum2 = np.abs(fft(signal2)[:N//2])
frequencies2 = fftfreq(N, 1/fs)[:N//2]

spectrum3 = np.abs(fft(signal3)[:N//2])
frequencies3 = fftfreq(N, 1/fs)[:N//2]

spectrum_all = np.abs(fft(signals)[:N//2])
frequencies_all = fftfreq(N, 1/fs)[:N//2]

# PLOTTING THE SIGNALS AND THEIR SPECTRA 

# Create a figure
plt.figure(figsize=(10, 10))

# Add many plots to the figure so we can show multiple things on the same page
plt.subplot(4, 2, 1)
plt.plot(t1, signal1)
plt.ylabel("Signal Amplitude")
plt.xlabel("Time (s)")
plt.title("Note 1")
plt.xlim([0, t1[-1]])
plt.ylim([np.min(signal1), np.max(signal1)])

plt.subplot(4, 2, 2)
plt.plot(frequencies1, spectrum1)
plt.xlim([0, frequencies1[-1]])
plt.ylim([0, np.max(spectrum1)/10])
plt.title("Spectrum of Note 1")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(4, 2, 3)
plt.plot(t1, signal2)
plt.title("Note 2")
plt.ylabel("Signal Amplitude")
plt.xlabel("Time (s)")
plt.xlim([0, t1[-1]])
plt.ylim([np.min(signal2), np.max(signal2)])

plt.subplot(4, 2, 4)
plt.plot(frequencies2, spectrum2)
plt.xlim([0, frequencies2[-1]])
plt.ylim([0, np.max(spectrum2)/10])
plt.title("Spectrum of Note 2")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(4, 2, 5)
plt.plot(t1, signal3)
plt.title("Note 3")
plt.ylabel("Signal Amplitude")
plt.xlabel("Time (s)")
plt.xlim([0, t1[-1]])
plt.ylim([np.min(signal3), np.max(signal3)])

plt.subplot(4, 2, 6)
plt.plot(frequencies3, spectrum3)
plt.xlim([0, frequencies3[-1]])
plt.ylim([0, np.max(spectrum3)/10])
plt.title("Spectrum of Note 3")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(4, 2, 7)
plt.plot(t1, signals)
plt.title("Chord")
plt.ylabel("Signal Amplitude")
plt.xlabel("Time (s)")
plt.xlim([0, t1[-1]])
plt.ylim([np.min(signals), np.max(signals)])

plt.subplot(4, 2, 8)
plt.plot(frequencies_all, spectrum_all)
plt.xlim([0, frequencies_all[-1]])
plt.ylim([0, np.max(spectrum_all)/10])
plt.title("Spectrum of Chord")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.tight_layout()

print(np.max(spectrum_all))
# After all this figure "creating", show the figure (this will pop up on your screen once this is run)
plt.show()
