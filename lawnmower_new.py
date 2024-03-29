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

t = np.arange(0, num_timesteps)
r = np.linspace(-maxR, maxR, binsR)
R, T = np.meshgrid(r, t)
data = np.zeros_like(R)

with holoocean.make(scenario) as env:
    for i in range(num_timesteps):
        env.act("auv0", command)
        state = env.tick()

        # Get depth data from state         # Prob need to initialize this and other sensors up top
        if 'DepthSensor' in state:
            depth = state['DepthSensor']

        # Get sonar data from state
        if 'SidescanSonar' in state:
            data = np.roll(data, 1, axis=0)
            data[0] = state['SidescanSonar']
            # sonar_str = np.array2string(data[0])
            sonar_str = np.array2string(data[0], precision=8, separator=', ', threshold=np.inf)
            log_file.write(sonar_str + '\n')
        '''
        CONTROL PLAN GOES HERE
        '''
        if(num_timesteps == 1000):          # Turn top rudder 45º 
            # Attempt to turn the UUV
            command = [0,45,0,0,20]


        if(num_timesteps == 2000):
            # Return fins to straight
            command = [0,0,0,0,20]

        
print("Finished Simulation!")










































