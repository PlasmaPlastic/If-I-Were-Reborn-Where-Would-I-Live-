import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


FILE = r"WPP2024_Demographic_Indicators_Medium.csv"

YEAR = 2026

SIMULATION = 1_000_000


print("Loading UN data...")


df = pd.read_csv(
    FILE,
    low_memory=False
)


print("Data loaded")


data = df[
    df["Time"] == YEAR
]



data = data[
    data["LocTypeName"] == "Country/Area"
]



population = "TPopulation1July"

birth_rate = "CBR"



data = data[
    [
        "Location",
        population,
        birth_rate
    ]
]


data = data.dropna()



data = data[
    (data[population] > 0)
    &
    (data[birth_rate] > 0)
]


data["BirthScore"] = (
    data[population]
    *
    data[birth_rate]
)


data["Probability"] = (
    data["BirthScore"]
    /
    data["BirthScore"].sum()
)



print("Running simulation...")


results = np.random.choice(
    data["Location"],
    size=SIMULATION,
    p=data["Probability"]
)


result = (
    pd.Series(results)
    .value_counts()
)


percentage = (
    result
    /
    SIMULATION
    *
    100
)


print("\n==============================")
print("Model 3: Population × Birth Rate")
print("Rebirth Probability Top 20")
print("==============================\n")


print(
    percentage.head(20)
)



print("\n==============================")
print("Selected Countries")
print("==============================\n")


selected_countries = [
    "Canada",
    "Republic of Korea",
    "Japan",
    "United States of America"
]


for country in selected_countries:

    if country in percentage.index:

        print(
            country,
            ":",
            round(
                percentage[country],
                5
            ),
            "%"
        )

    else:

        print(
            country,
            ": Not Found"
        )


plt.figure(
    figsize=(12,6)
)

percentage.head(20).plot(
    kind="bar"
)

plt.ylabel(
    "Probability (%)"
)

plt.xlabel(
    "Country"
)

plt.title(
    "Model 3: Population × Birth Rate Rebirth Probability"
)

plt.xticks(
    rotation=70
)

plt.tight_layout()

plt.show()