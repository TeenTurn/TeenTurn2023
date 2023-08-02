#%% IMPORTS
from pydataset import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal
from scipy.fft import fftshift

#%% DEFINING A SINE WAVE SIGNAL
f = 100     # Hz, signal frequency
fs = 1000   # Hz, sampling frequency
signal_duration = 0.2 # in seconds

# defining the "original" signal
t_original = np.arange(0,signal_duration, 1/4000) 
original_signal = np.sin(2*np.pi*f*t_original)

# sampling that signal with a defined sampling step size
sampling_step_size1 = 0.0005  # gap between each sample (in samples)
t1 = np.arange(0,signal_duration, sampling_step_size1) 
signal1 = np.sin(2*np.pi*f*t1)

# sampling that same signal with different sampling step size
sampling_step_size2 = sampling_step_size1*10 # using a much lower sample size (x10)
t2 = np.arange(0,signal_duration, sampling_step_size2) 
signal2 = np.sin(2*np.pi*f*t2)

# plotting the signal and the signals obtained from sampling
plt.figure(figsize=(10, 5))
plt.subplot(2,1,1)
plt.plot(t_original, original_signal, "g")
plt.plot(t1, signal1,'bo-')
plt.legend(["Original signal",
            "Sampled signal with a sample step size of "+str(sampling_step_size1)+" samples"])
plt.title('Sine signal')
plt.xlim([0, t1[-1]])
plt.ylabel("Signal Amplitude")
plt.xlabel('Time (s)')

plt.subplot(2,1,2)
plt.plot(t_original, original_signal, "g")
plt.plot(t2, signal2,'ro-')
plt.legend(["Original signal",
            "Sampled signal with a sample step size of "+str(sampling_step_size2)+" samples"])
plt.title('Sine signal with not enough sampling points (step size too large)')
plt.xlabel('Time (s)')
plt.ylabel("Signal Amplitude")
plt.tight_layout()
plt.xlim([0, t2[-1]])