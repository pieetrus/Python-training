import numpy as np
import matplotlib.pyplot as plot
import math as math
PI = math.pi


time = np.arange(0,2*PI,0.1)

amplitude_sin = np.sin(time)
amplitude_cos = np.cos(time)

plot.plot(time,amplitude_sin)
plot.plot(time,amplitude_cos)

plot.axis([0,2*PI,-1.5,1.5])

plot.title('Funkcja sinus i cosinus')
plot.xlabel('Time')
plot.ylabel('Amplitue')

plot.grid(True, which='both')

plot.show()