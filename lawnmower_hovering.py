import holoocean as H
import numpy as np

cfg = {
    "name": "test_hovering",
    "world": "OpenWater",
    "package_name": "Ocean",
    "main_agent": "auv0",
    "ticks_per_sec": 60,
    "agents": [
        {
            "agent_name": "auv0",
            "agent_type": "HoveringAUV",
            "sensors": [
                {
                    "sensor_type": "DVLSensor"
                }
            ],
            "control_scheme": 1,    # Using PD Control Scheme
            "location": [35.0, -40.5, -292.5]
        }
    ]
}

env = H.make(scenario_cfg=cfg)
env.reset()

# env.act('auv0', np.array([0,0,0,0,20,20,20,20]))
# env.act('auv0', np.array([30.0,-40.5,-292.5,0,0,0]))

command = np.array([30.0,-40.5,-292.5,0,0,0])

for i in range(300):
    # command = np.array([35.0+i,-40.5,-292.5,0,0,0])
    # env.act('auv0', command)
    state = env.step(command)

    # states is a dictionary
    vel = state["DVLSensor"]

    print(vel)