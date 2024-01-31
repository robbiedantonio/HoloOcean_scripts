

import holoocean
import matplotlib.pyplot as plt
import numpy as np

## Basic HoloOcean Configuration Stuff
scenario = "OpenWater-TorpedoSidescanSonar"
config = holoocean.packagemanager.get_scenario(scenario)
config = config['agents'][0]['sensors'][-1]["configuration"]
maxR = config['RangeMax']   # Range of each sonar chanel
binsR = config['RangeBins'] # Number of bins in each sonar chanel


## This is what's used to control the UUV
'''
From HoloOcean:

Takes in a 5 length vector. The first element is the right fin 
angle from -45 to 45 degrees, then top, left, and bottom. The 
last element is the “thruster” with a value of -100 to 100.
'''
## Initialize UUV controls setup - 20% thrust and all fins in neutral positions
command = np.array([0,0,0,0,20])



## Open log file to record simulation data 
log_file = open('HoceanLog.txt', 'a')   # Set to only append

#### RUN SIMULATION
num_timesteps = 10000    # Number of ticks in environment

with holoocean.make(scenario) as env:
    for i in range(num_timesteps):
        env.act("auv0", command)
        state = env.tick()

        if 'SidescanSonar' in state:
            data = np.roll(data, 1, axis=0)
            data[0] = state['SidescanSonar']


        log_file.write(data[0])
        '''
        CONTROL PLAN GOES HERE
        '''
        if(num_timesteps == 1000):          # Turn top rudder 45º 
            # Attempt to turn the UUV
            command = [0,45,0,0,20]


        if(num_timesteps == 2000)

        
print("Finished Simulation!")










































