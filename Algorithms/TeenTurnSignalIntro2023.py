from pydataset import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal
from scipy.fft import fftshift
# rng = np.random.default_rng()

f = 100     # signal frequency
fs = 1000   # sampling frequency
signal_duration = 0.2 # in s

step_size1 = 0.0005  # 0.1ms
t1 = np.arange(0,signal_duration,step_size1) # arange([start,] stop[, step,])
signal1 = np.sin(2*np.pi*f*t1)

step_size2 = 0.002
t2 = np.arange(0,signal_duration,step_size2) # arange([start,] stop[, step,])
signal2 = np.sin(2*np.pi*f*t2)


plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t1, signal1,'bo-')
plt.title('Sine signal')
plt.xlabel('Time [s]')

plt.subplot(2,1,2)
plt.plot(t2, signal2,'bo-')
plt.title('Sine signal with not enough sampling points (step size too large)')
plt.xlabel('Time [s]')
plt.tight_layout()

## longer sine signal
f = 100     # signal frequency
fs = 1000   # sampling frequency
signal_duration = 1 # in s

step_size1 = 0.0005  # 0.1ms
t1 = np.arange(0,signal_duration,step_size1) # arange([start,] stop[, step,])
signal1 = np.sin(2*np.pi*f*t1)

## Create noise 
mean = 0
std = 1
num_samples = len(signal1)
noise = np.random.normal(mean, std, size=num_samples)

plt.figure(2)
plt.subplot(3,2,1)
plt.plot(t1, signal1, 'b-')
plt.title('Sine signal')
plt.xlabel('Time [s]')

plt.subplot(3,2,3)
plt.plot(t1, noise, 'b')
plt.title('Noise signal')
plt.xlabel('Time [s]')

plt.subplot(3,2,5)
plt.plot(t1, signal1+noise, 'b')
plt.title('Noise + sine signal')
plt.xlabel('Time [s]')
plt.tight_layout()


## spectrograms
plt.subplot(3,2,2)
f, t, Sxx = signal.spectrogram(signal1, fs)
plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

plt.subplot(3,2,4)
f, t, Sxx = signal.spectrogram(noise, fs)
plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

plt.subplot(3,2,6)
f, t, Sxx = signal.spectrogram(signal1+noise, fs)
plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

plt.tight_layout()

plt.show()