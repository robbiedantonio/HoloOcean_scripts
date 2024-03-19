

import numpy as np

with open('nav_agent_log.txt', 'r') as log_file:
    lines = log_file.readlines()

# Convert back to numpy array
sidescan_sonar_array = np.array([list(map(float, line.strip().split(','))) for line in lines])

# Print or use the array as needed
print(sidescan_sonar_array)