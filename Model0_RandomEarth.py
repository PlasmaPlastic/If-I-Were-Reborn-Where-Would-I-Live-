
import numpy as np
import matplotlib.pyplot as plt

N = 1_000_000   

longitude = np.random.uniform(
    -180,
    180,
    N
)


u = np.random.uniform(
    -1,
    1,
    N
)

latitude = np.degrees(
    np.arcsin(u)
)



print("Total simulations:", N)

print(
    "Average latitude:",
    np.mean(latitude)
)

print(
    "Average longitude:",
    np.mean(longitude)
)



plt.figure(
    figsize=(14,7)
)


plt.hexbin(
    longitude,
    latitude,
    gridsize=250,
    cmap="inferno",
    bins="log"
)


plt.xlabel(
    "Longitude (degrees)"
)

plt.ylabel(
    "Latitude (degrees)"
)


plt.title(
    "Model 0: Random Needle Drops on Earth"
)


plt.colorbar(
    label="Number of Drops"
)


plt.xlim(
    -180,
    180
)

plt.ylim(
    -90,
    90
)


plt.grid(
    alpha=0.3
)


plt.show()