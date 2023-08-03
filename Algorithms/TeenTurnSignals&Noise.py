# IMPORTS
from pydataset import data
import numpy as np
import matplotlib.pyplot as plt

# SIGNALS AND NOISE

f = 10      # signal frequency
fs = 1000   # sampling frequency
signal_duration = 1 # in s

# Defining the signal 
step_size1 = 0.0005  # 0.1ms
t1 = np.arange(0,signal_duration,step_size1)
signal1 = np.sin(2*np.pi*f*t1)

# Defining constraints for the noise that will be added the signal
mean = 0 # mean of the noise
std = 1  # standard deviation of the noise
num_samples = len(signal1) # number of samples of the noise (which should match the number of samples of the "pure" signal)
noise = np.random.normal(mean, std, size=num_samples) # creating the noise signal with all these factors

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(t1, signal1, 'b-')
plt.xlim([0, t1[-1]])
plt.title('Sine signal')
plt.xlabel('Time (s)')
plt.ylabel("Signal Amplitude")

plt.subplot(3,1,2)
plt.plot(t1, noise, 'b')
plt.xlim([0, t1[-1]])
plt.title('Noise signal')
plt.xlabel('Time (s)')
plt.ylabel("Signal Amplitude")

plt.subplot(3,1,3)
plt.plot(t1, signal1+noise, 'b')
plt.xlim([0, t1[-1]])
plt.title('Noise + sine signal')
plt.xlabel('Time (s)')
plt.ylabel("Signal Amplitude")
plt.tight_layout()


plt.show()