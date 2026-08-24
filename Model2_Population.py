
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


population_column = "TPopulation1July"



countries = data[
    [
        "Location",
        population_column
    ]
]


countries = countries.dropna()


countries = countries[
    countries[population_column] > 0
]



countries["Probability"] = (
    countries[population_column]
    /
    countries[population_column].sum()
)



print("Running simulation...")


results = np.random.choice(
    countries["Location"],
    size=SIMULATION,
    p=countries["Probability"]
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
print("Model 2: Population Weighted")
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
    "Model 2: Rebirth Probability Based on Population"
)

plt.xticks(
    rotation=70
)

plt.tight_layout()

plt.show()