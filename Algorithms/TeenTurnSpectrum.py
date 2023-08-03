# IMPORTING PACKAGES THAT WE WILL USE LATER ON
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# CREATING A SINE WAVE
# A sine wave has the following equation: np.sin(2*np.pi*frequency*time)
# frequency = how often the signal repeats
# time = duration of the signal

# define a frequency for the signal
frequency = 5 # Hz 

# define a time duration for the signal
duration = 2 # seconds

# in order to plot the sine signal against time we have to create an array for the time
# defining how often a sample is taken from the signal - step_size
step_size1 = 0.001
sampling_frequency = 1/step_size1 # 1,000 Hz

# In order to plot the signal we need to define an array for time
time_array = np.arange(0, duration, step_size1)

# Now we can calculate our sine signal
sine_signal1 = np.sin(2*np.pi*frequency*time_array)

# ADD A SECOND SINE WAVE TO YOUR ORIGINAL SIGNALS
# Now we can add another sine wave (with a different frequency) to our original sine wave signal
frequency2 = 10 # Hz

sine_signal2 = np.sin(2*np.pi*frequency2*time_array)

sine_signal = sine_signal1 + sine_signal2


# CALCULATING THE SPECTRUM FOR OUR COMBINED SIGNAL

# Explanation
# In order for us to see which notes are playing on the piano, we need to see which frequencies are dominating the signal. 
# When we calculate the spectrum of each signal we show which frequencies (or sine waves with certain frequencies) work 
# together to create the chord.

N = len(sine_signal)
spectrum = np.abs(fft(sine_signal)[:N//2])
frequencies = fftfreq(N, 1/sampling_frequency)[:N//2]



# Now we can plot our sine signal
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time_array, sine_signal)
plt.plot(time_array, sine_signal1, "r--")
plt.plot(time_array, sine_signal2, "g--")
plt.xlim([0, time_array[-1]])
plt.legend(["Combined signal", "Signal 1", "Signal 2"])
plt.xlabel("Time (seconds)")
plt.ylabel("Signal Amplitude")
plt.title("Sine wave with a frequency of "+str(frequency)+" Hz")

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(spectrum))
plt.xlim([0, frequencies[-1]])
plt.ylim([0, np.max(spectrum)+100])
plt.title("Spectrum of Note 2")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()