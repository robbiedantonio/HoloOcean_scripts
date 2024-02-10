import holoocean
import numpy as np


# A custom scenario with point-to-point navigation
env = holoocean.make(scenario_name="OpenWater-SideScanLawnmower")

config = config['agents'][0]['sensors'][-1]["configuration"]
print(config)



