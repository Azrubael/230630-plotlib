#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

# plt.style.use("dark_background")
plt.style.use("grayscale")
# plt.style.use("fivethirtyeight")

indexes = np.arange(9)
height = 0.4
Annual = [x for x in range(2015, 2024)]
RealPIL = [2.5,4,5,3,1.7,3.2,1,2,0.7]
VirtualPIL = [3.2,3,2,4,5,0.1,2.6,4,1]

plt.figure(figsize=(12,8))
plt.barh(indexes, RealPIL, label="PIL REAL", height=height, color="#959595")
plt.barh(indexes+height, VirtualPIL, label="PIL VIRTUAL", height=height, color="#505050")
plt.legend()

plt.title("Preformance of PIL in vitro from 2015 to 2023")
plt.xlabel("\nAnnually from 2015 to 2023")
plt.ylabel("Trend of GDP")
plt.yticks(indexes+height/2, Annual)

plt.show()