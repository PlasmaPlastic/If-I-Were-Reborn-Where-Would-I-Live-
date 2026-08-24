
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd




FILE = r"WPP2024_Demographic_Indicators_Medium.csv"

MAP_FILE = r"ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"

YEAR = 2026

SIMULATION = 1_000_000



print("Loading UN data...")


df = pd.read_csv(
    FILE,
    low_memory=False
)


print("Data loaded")



data = df[
    (df["Time"] == YEAR)
    &
    (df["LocTypeName"] == "Country/Area")
]



population = "TPopulation1July"

birth_rate = "CBR"



data = data[
    [
        "Location",
        "ISO3_code",
        population,
        birth_rate
    ]
]


data = data.dropna()



# Remove invalid data

data = data[
    (data[population] > 0)
    &
    (data[birth_rate] > 0)
]



data["Score"] = (
    data[population]
    *
    data[birth_rate]
)



data["Probability"] = (
    data["Score"]
    /
    data["Score"].sum()
)


print("Running simulation...")


result = np.random.choice(
    data["ISO3_code"],
    size=SIMULATION,
    p=data["Probability"]
)


result = (
    pd.Series(result)
    .value_counts()
)


probability_result = (
    result
    /
    SIMULATION
    *
    100
)


print("\n==============================")
print("Final Rebirth Probability")
print("==============================\n")


print(
    probability_result.head(20)
)


print("\n==============================")
print("Selected Countries")
print("==============================\n")


for country in [
    "CAN",
    "KOR",
    "JPN",
    "USA"
]:

    if country in probability_result.index:

        print(
            country,
            ":",
            round(
                probability_result[country],
                5
            ),
            "%"
        )


print("\nLoading world map...")


world = gpd.read_file(
    MAP_FILE
)


map_data = world.merge(
    probability_result.rename("Probability"),
    left_on="ADM0_A3",
    right_index=True,
    how="left"
)


map_data["Probability"] = (
    map_data["Probability"]
    .fillna(0)
)


fig, ax = plt.subplots(
    figsize=(15,8)
)


map_data.plot(
    column="Probability",
    ax=ax,
    legend=True,
    cmap="hot",
    linewidth=0.1
)


plt.title(
    "Final Rebirth Probability Map\nPopulation × Birth Rate Model"
)

plt.axis(
    "off"
)


plt.show()