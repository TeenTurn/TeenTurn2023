# IMPORTING PACKAGES THAT WE WILL USE LATER ON
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fftshift
from scipy.fft import fft, fftfreq


# defining the frequencies for the chord we will play (in Hz)
f_1 = 261.626  # Hz, middle C note, signal frequency
f_2 = 329.628  # Hz, middle E
f_3 = 391.995  # Hz, middle G


# defining how long our signal will last (in seconds)
signal_duration = 1  # in s

# defining how much time there will be in between samples
step_size1 = 0.0001

# in order to plot the signal we need to define an array for time
t1 = np.arange(0, signal_duration, step_size1)

# defining our three signals - one for each note/ frequency of the chord
def get_signal(harmonic):
    if harmonic == 1:
        frequency = f_1
    if harmonic == 2:
        frequency = f_2
    if harmonic == 3:
        frequency = f_3

    return np.sin(2*np.pi*frequency*t1) + np.random.random(len(t1))