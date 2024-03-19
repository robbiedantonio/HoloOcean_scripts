import holoocean as H
import numpy as np

'''
This will be NavAgent agent in the operwater scenario
'''
scenario = "OpenWater-NavAgentSidescanSonar"
config = H.packagemanager.get_scenario(scenario)

timesteps = 1000    # Number of ticks in environment

log_file = open('nav_agent_log.txt', 'w')   # Overwrite existing content

command = np.array([50, 10000, -292.5])

with H.make(scenario, show_viewport=True) as env:
    for i in range(timesteps):
        env.act("agent0", command)
        state = env.tick()

        # print(state['agent0'].keys())
        # print(state['agent0']['SidescanSonar'].shape)

        if 'SidescanSonar' in state['agent0']:

            log_file.write(','.join(map(str, state['agent0']['SidescanSonar'])) + '\n')

        if 'GPSSensor' in state['agent0']:
            print(state['agent0']['GPSSensor'])

        if 'VelocitySensor' in state['agent0']:
            print(state['agent0']['VelocitySensor'])


print("Finished Simulation!")
