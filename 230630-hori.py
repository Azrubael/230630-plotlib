#!/usr/bin/env python3
"""
Horizontal bars chart
"""

import numpy as np
from matplotlib import pyplot as plt

# plt.style.use("dark_background")
# plt.style.use("Solarize_Light2")
plt.style.use("fivethirtyeight")

indexes = np.arange(9)
width = 0.4
Annual = [x for x in range(2015, 2024)]
RealPIL = [2.5,4,5,3,1.7,3.2,1,2,0.7]
VirtualPIL = [3.2,3,2,4,5,0.1,2.6,4,1]

plt.figure(figsize=(12,8))
plt.bar(indexes, RealPIL, label="PIL REAL", width=width, color="#00aaaa")
plt.bar(indexes+width, VirtualPIL, label="PIL VIRTUAL", width=width, color="#ffcc00")
plt.legend()

plt.title("Preformance of PIL in vitro from 2015 to 2023")
plt.xlabel("\nAnnually from 2015 to 2023")
plt.ylabel("Trend of GDP")
plt.xticks(indexes+width/2, Annual)

plt.show()
