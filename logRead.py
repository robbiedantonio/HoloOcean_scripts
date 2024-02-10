

import numpy as np


file = open('HoceanLog.txt', 'r')


for i, line in enumerate(file):
	npstring = np.fromstring(line)
	print(npstring)
	if i == 3: 
		break