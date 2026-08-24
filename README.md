# Generate Markdown README for the GitHub repository

readme_content =  If I Were Reborn, Where Would I Live? 
> **A Mathematical Probability Model of Global Reincarnation**

This project was inspired by watching anime, especially stories featuring reincarnation and Isekai. While watching these stories, I started wondering:

**"If reincarnation were real, and I were randomly reborn somewhere on Earth, where would I most likely be born?"**

This led me to turn a fictional anime concept into a mathematical probability model.

<p align="center">
  <img src="https://m.media-amazon.com/images/M/MV5BYWQwNjk3MDItNDAxMS00YTQ2LWEyNDctMGYyZTE5OGQxNGQ1XkEyXkFqcGc@._V1_.jpg" width="30%">
  <img src="https://m.media-amazon.com/images/M/MV5BNGRjMzE3ZGQtN2QyNC00YzRlLWI1ZTgtZmI4MTJlYTZlNThkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg" width="30%">
  <img src="https://m.media-amazon.com/images/M/MV5BYWMwYWVjMzctYTc2YS00YjVmLWJiOWQtMGJlMzVlOTE4NWQ2XkEyXkFqcGc@._V1_.jpg" width="30%">
</p>

Instead of relying purely on geography, this repository builds a step-by-step probability model using Earth's physical geometry, global population distribution, demographic crude birth rates (CBR), and Python Monte Carlo simulations.

The goal is to explore how the probability of being reborn in different parts of the world changes as increasingly realistic factors are added to the model.
---

## 📌 Project Overview

Many stories describe people being reborn into another world. But what if reincarnation happened randomly on Earth? 

1. **Model 0 (Random Earth Geometry)**: Uniform random drop coordinates across latitude/longitude ($\approx 29\%$ chance of hitting land).
2. **Model 1 (Land Only)**: Filtering out ocean coordinates to isolate land masses.
3. **Model 2 (Population Weighted)**: Weighing reincarnation probabilities strictly by sovereign nation population sizes.
4. **Model 3 & 4 (Annual Birth Rate & Final Spatial Model)**: Adjusting population by crude birth rates ($B_i = N_i \\times b_i$) to reflect actual annual new births, combined with a 1,000,000-run Monte Carlo simulation and physical noise perturbations.

---

## 📊 Key Results

Under the final demographic model ($N_i \\times b_i$), a person is statistically most likely to be reborn in:

| Rank | Country | Probability (%) |
| :---: | :--- | :---: |
| **1** | **India** 🇮🇳 | **17.3%** |
| **2** | **China** 🇨🇳 | **6.5%** |
| **3** | **Nigeria** 🇳🇬 | **5.8%** |
| **4** | **Pakistan** 🇵🇰 | **5.2%** |
| **5** | **DR Congo** 🇨🇩 | **3.4%** |
| - | United States 🇺🇸 | 2.7% |
| - | Japan 🇯🇵 | 0.57% |
| - | Canada 🇨🇦 | 0.27% |
| - | South Korea 🇰🇷 | 0.19% |

### 💡 Philosophical Takeaway
Being born in countries like South Korea ($0.19\%$) or Canada ($0.27\%$) is mathematically a rare event (less than 0.3% chance). Rather than placing hopes on a hypothetical next life, this project statistically highlights the extraordinary rarity of our present existence and the importance of making the most of our current lives.

---

## 📁 Repository Structure

```text
.
├── ne_110m_admin_0_countries/       # Natural Earth shapefile directory for map visualization
├── Model0_RandomEarth.py            # Model 0: Unweighted spatial random drops
├── Model1_LandOnly.py               # Model 1: Land coordinate filtering
├── Model2_Population.py             # Model 2: Population-weighted probability
├── Model3_BirthRate.py              # Model 3: Birth rate x Population probability
├── Model4_Final_RebirthMap.py       # Model 4: Final Monte Carlo simulation & Choropleth Map
├── WPP2024_Demographic_Indicators_Medium.csv # UN Population & Birth Rate Dataset
├── If I Were Reborn, Where Would I Live_.pdf # Full Paper / Research Report (PDF)
└── README.md                        # Documentation


