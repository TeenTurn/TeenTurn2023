# IMPORTING PACKAGES THAT WE WILL USE LATER ON
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
step_size1 = 0.0001  # 0.1ms

# In order to plot the signal we need to define an array for time
time_array = np.arange(0, duration, step_size1)

# Now we can calculate our sine signal
sine_signal = np.sin(2*np.pi*frequency*time_array)

### COMMENT THIS OUT WHEN YOU'VE FINISHED THE FIRST SECTION
# # Now we can add another sine wave (with a different frequency) to our original sine wave signal
# frequency2 = 10 # Hz

# sine_signal2 = np.sin(2*np.pi*frequency2*time_array)

# sine_signal = sine_signal + sine_signal2

# Now we can plot our sine signal
plt.figure()
plt.plot(time_array, sine_signal)
plt.xlabel("Time (seconds)")
plt.ylabel("Signal Amplitude")
plt.title("Sine wave with a frequency of "+str(frequency)+" Hz")
plt.show()