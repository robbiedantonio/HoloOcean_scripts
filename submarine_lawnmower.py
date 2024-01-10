'''
Boston University ECE Senior Design: SLAM for Underwater Robotics

UUV follows classic "lawnmower" path over the underwater submarine
environment.

Largely adopted from: https://holoocean.readthedocs.io/en/master/usage/examples/sonar_sidescan.html
'''
import holoocean
import matplotlib.pyplot as plt
import numpy as np

#### GET SONAR CONFIG
scenario = "OpenWater-TorpedoSidescanSonar"
config = holoocean.packagemanager.get_scenario(scenario)
config = config['agents'][0]['sensors'][-1]["configuration"]
maxR = config['RangeMax']   # Range of each sonar chanel
binsR = config['RangeBins'] # Number of bins in each sonar chanel



#### INITIALIZE SONAR PLOT PARAMETERS
num_pings = 50  # Number of pings in simulation?

#### GET PLOT READY
plt.ion()       # Interactive mode

t = np.arange(0, num_pings)
r = np.linspace(-maxR, maxR, binsR)
R, T = np.meshgrid(r, t)
data = np.zeros_like(R)

plt.grid(False)
plot = plt.pcolormesh(R, T, data, cmap='copper', shading='auto', vmin=0, vmax=1)
plt.tight_layout()
plt.gca().invert_yaxis()
plt.gcf().canvas.flush_events()

#### RUN SIMULATION
num_timesteps = 2    # Number of ticks in environment

command = np.array([0,0,0,0,20])
with holoocean.make(scenario) as env:
    for i in range(num_timesteps):
        env.act("auv0", command)
        state = env.tick()

        if 'SidescanSonar' in state:
            data = np.roll(data, 1, axis=0)
            data[0] = state['SidescanSonar']

            print(data)

            plt.set_array(data.ravel())

            plt.draw()
            plt.gcf().canvas.flush_events()

print("Finished Simulation!")
plt.ioff()
plt.show()