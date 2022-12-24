import utm
import numpy as np
import matplotlib.pyplot as plt
v = utm.from_latlon(np.array([51.2, 51.3]),np.array([7.4, 7.5]))
print(v)
plt.plot(np.array([51.2, 51.3]),np.array([7.4, 7.5]))
plt.show()