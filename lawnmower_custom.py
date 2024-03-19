import holoocean
import numpy as np


# A custom scenario with point-to-point navigation
# env = holoocean.make(scenario_name="OpenWater-SideScanLawnmower")
scenario="OpenWater-SideScanLawnmower"
config = holoocean.packagemanager.get_scenario(scenario)

print(config['agents'][0]['control_scheme'], holoocean.agents.ControlSchemes.UAV_TORQUES)

env = holoocean.make(scenario)

env.reset() 

env.set_control_scheme("auv0", control_scheme = holoocean.agents.ControlSchemes.NAV_TARGET_LOCATION)


# Parameters
num_timesteps = 10000    # Number of ticks in environment

# command = np.array([50, 100, -292.5])
command = np.array([0,0,0,0,20])

for i in range(num_timesteps):
        env.act("auv0", command)
        state = env.tick()

        if 'GPSSensor' in state:
                print(state['GPSSensor'])

        # Get depth data from state         # Prob need to initialize this and other sensors up top
        # if 'DepthSensor' in state:
        #     depth = state['DepthSensor']

        # Get sonar data from state
        # if 'SidescanSonar' in state:
        #     data = np.roll(data, 1, axis=0)
        #     data[0] = state['SidescanSonar']
        #     # sonar_str = np.array2string(data[0])
        #     sonar_str = np.array2string(data[0], precision=8, separator=', ', threshold=np.inf)
        #     # log_file.write(sonar_str + '\n')
        '''
        CONTROL PLAN GOES HERE
        '''

        
print("Finished Simulation!")



























