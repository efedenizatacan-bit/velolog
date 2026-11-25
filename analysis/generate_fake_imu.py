import numpy as np
import pandas as pd

# array of samples (100 per second for 60 seconds)
time = np.linspace(0, 60, 6000, endpoint = False)

frequency = 2

# simulate running/walking in each axial direction (bounce)
ax = 0.4 * np.sin(2 * np.pi * time * frequency)
ay = 0.3 * np.cos(2 * np.pi * time * frequency)
az = 1.5 * np.sin(2 * np.pi * time * frequency) + 1.0

# ensure fake dataset produces same one each test
rng = np.random.default_rng(42)

# generate jitter for each of the axes
noisex = rng.normal(loc=0.0, scale=0.05, size=len(time))
noisey = rng.normal(loc=0.0, scale=0.05, size=len(time))
noisez = rng.normal(loc=0.0, scale=0.05, size=len(time))

# adding noise to each axis
ax += noisex
ay += noisey
az += noisez

# pack into dictionary and into dataframe, then create csv file
csv = {'time_s': time, 'ax': ax, 'ay': ay, 'az': az}

dataframe = pd.DataFrame(csv)

dataframe.to_csv("data/fake_imu.csv", index=False)