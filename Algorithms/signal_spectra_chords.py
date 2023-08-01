from pydataset import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal
from scipy.fft import fftshift
from scipy.fft import fft, fftfreq
import sounddevice as sd

# rng = np.random.default_rng()

f_1 = 261.63   # Hz, middle C note, signal frequency
f_2 = 329.628  # Hz, middle E
f_3 = 391.995  # Hz, middle G

fs = 1000  # sampling frequency

signal_duration = 1  # in s

step_size1 = 0.0005  # 0.1ms
t1 = np.arange(0, signal_duration, step_size1)
signal1 = np.sin(2*np.pi*f_1*t1)
signal2 = np.sin(2*np.pi*f_2*t1)
signal3 = np.sin(2*np.pi*f_3*t1)

signals = signal1+signal2+signal3

## Spectra ##
N = len(signal1)
spectrum1 = fft(signal1)[:N//2]
frequencies1 = fftfreq(N, 1/fs)[:N//2]

spectrum2 = fft(signal2)[:N//2]
frequencies2 = fftfreq(N, 1/fs)[:N//2]

spectrum3 = fft(signal3)[:N//2]
frequencies3 = fftfreq(N, 1/fs)[:N//2]

spectrum_all = fft(signals)[:N//2]
frequencies_all = fftfreq(N, 1/fs)[:N//2]

plt.figure(figsize=(20, 20))

plt.subplot(4, 2, 1)
plt.plot(t1, signal1)
plt.xlabel("Signal Amplitude")
plt.ylabel("Time (s)")
plt.xlim([0, t1[-1]])
plt.ylim([-3, 3])
plt.title("Middle C ("+str(f_1)+" Hz)")

plt.subplot(4, 2, 2)
plt.plot(frequencies1, np.abs(spectrum1))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(4, 2, 3)
plt.plot(t1, signal2)
plt.xlabel("Signal Amplitude")
plt.ylabel("Time (s)")
plt.title("Middle E ("+str(f_2)+" Hz)")
plt.xlim([0, t1[-1]])
plt.ylim([-3, 3])

plt.subplot(4, 2, 4)
plt.plot(frequencies2, np.abs(spectrum2))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(4, 2, 5)
plt.plot(t1, signal3)
plt.xlabel("Signal Amplitude")
plt.ylabel("Time (s)")
plt.title("Middle G ("+str(f_3)+" Hz)")
plt.xlim([0, t1[-1]])
plt.ylim([-3, 3])

plt.subplot(4, 2, 6)
plt.plot(frequencies3, np.abs(spectrum3))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(4, 2, 7)
plt.plot(t1, signals)
plt.xlabel("Signal Amplitude")
plt.ylabel("Time (s)")
plt.xlim([0, t1[-1]])
plt.ylim([-3, 3])
plt.title("Chord of C ("+str(f_1)+" + "+str(f_2)+" + "+str(f_3)+" Hz)")

plt.subplot(4, 2, 8)
plt.plot(frequencies_all, np.abs(spectrum_all))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')


plt.show()

# sd.play(signal, fs)
# sd.wait()
