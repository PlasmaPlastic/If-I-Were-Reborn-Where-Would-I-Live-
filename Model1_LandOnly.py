
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
from shapely.prepared import prep


N = 1_000_000


world = gpd.read_file(
    "ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"
)



land = world.geometry.union_all()


land = prep(land)


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


land_points_lon = []
land_points_lat = []


for lon, lat in zip(
    longitude,
    latitude
):

    point = Point(
        lon,
        lat
    )


    if land.contains(point):

        land_points_lon.append(
            lon
        )

        land_points_lat.append(
            lat
        )


land_points_lon = np.array(
    land_points_lon
)

land_points_lat = np.array(
    land_points_lat
)


land_probability = (
    len(land_points_lon)
    /
    N
)

print("-------------------------")

print(
    "Total simulations:",
    N
)

print(
    "Land hit probability:",
    land_probability
)


print(
    "Land points:",
    len(land_points_lon)
)

print("-------------------------")

fig, ax = plt.subplots(
    figsize=(14,7)
)

world.plot(
    ax=ax,
    color="lightgray"
)

ax.scatter(
    land_points_lon,
    land_points_lat,
    s=1,
    alpha=0.2,
    color="red"
)

plt.title(
    "Model 1: Rebirth Probability on Land Only"
)

plt.xlabel(
    "Longitude"
)

plt.ylabel(
    "Latitude"
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