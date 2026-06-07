import matplotlib.pyplot as plt
import numpy as np
import random
import time
from copy import deepcopy

N = 25000
List = [random.randint(-1000, 1000) for _ in range(N)]

def sort_stright(List):
    start_time = time.time()
    l = deepcopy(List)
    min = sorted(l)[0]
    end_time = time.time()
    return int((end_time - start_time)*10000)


def sort_bubble(List):
    start_time = time.time()
    L = deepcopy(List)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    end_time = time.time()
    return int((end_time - start_time)*10000)

def sort_insert(List):
    start_time = time.time()
    L = deepcopy(List)
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j] < L[j - 1]:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1
    end_time = time.time()
    return int((end_time - start_time)*10000)

def sort_div(List):
    start_time = time.time()
    L = deepcopy(List)
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j] < L[j - 1]:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1
    end_time = time.time()
    return int((end_time - start_time)*10000)


f1 = sort_stright(List)
f2 = sort_bubble(List)
f3 = sort_insert(List)
f4 = sort_div(List)

print(f"sort stright time: {f1}")
print(f"sort bubble time: {f2}")
print(f"sort insert time: {f3}")
print(f"sort div time: {f4}")

labels = ['sort stright', 'sort bubble', 'sort insert', 'sort div']
values = [f1, f2, f3, f4]

# Create figure and axis
fig, ax = plt.subplots(figsize=(6,4))

# Draw vertical bars
ax.bar(labels, values, color=['#4C72B0','#55A868','#C44E52','#8172B2'])

# Add value labels above bars
for i, v in enumerate(values):
    ax.text(i, v + max(values)*0.02, str(v), ha='center')

# Labels and title
ax.set_ylabel('Time, mks')
ax.set_title('Column diagram (4 values)')
ax.set_ylim(0, max(values) * 1.15)

plt.tight_layout()
plt.show()