# ⚡ EV Vehicle Imports in Sri Lanka — Data Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/pandas-data%20analysis-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/status-complete-brightgreen" />
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" />
</p>

<p align="center">
  An end-to-end analysis of Sri Lanka's EV import boom — from messy government data to
  forecasting, geographic patterns, and machine-learning clustering.
</p>

---

## 📋 Table of Contents
- [Overview](#-project-overview)
- [Key Findings](#-key-findings)
- [Data Source](#-data-source)
- [Repository Structure](#-repository-structure)
- [Methodology](#-methodology)
- [Tech Stack](#-tech-stack)
- [How to Run](#-how-to-run)
- [Author](#-author)

---

## 🔎 Project Overview

Sri Lanka has seen a dramatic recent surge in EV imports. This project cleans and analyzes
**6,536 aggregated import records (65,197 total vehicles, 2011–2025)** from the Department
of Motor Traffic to answer:

- What types of EVs are being imported, and by whom?
- How has EV adoption changed over time, and where might it be headed?
- Are there regional differences in EV adoption patterns across Sri Lanka's 25 districts?

---

## 📊 Key Findings

<table>
<tr>
<td width="33%" valign="top">

### 🏍️ Motorcycles Dominate
~79% of all EV imports are motorcycles. A single brand, **YADEA**, holds ~45% of the
entire market — more than every other brand combined.

</td>
<td width="33%" valign="top">

### 📈 Explosive Recent Growth
Imports grew from 4,041 (2023) to 33,418 (2025) — an **8x increase** in two years. A
model trained on the recent trend predicts nearly **3x higher** 2026 volume than one
trained on the full 15-year history.

</td>
<td width="33%" valign="top">

### 🗺️ Surprising Regional Split
K-means clustering reveals 3 adoption profiles. **Kandy edges out Colombo** for highest
car-share of EVs — not the assumption most would start with.

</td>
</tr>
</table>

<p align="center">
  <img src="visuals/yearly_trend.png" width="48%" />
  <img src="visuals/car_share_by_district.png" width="48%" />
</p>

<details>
<summary><b>📉 See the long-term vs. short-term forecast comparison</b></summary>
<br>

| Model | 2026 Prediction | 2027 Prediction |
|---|---|---|
| Full history (2011–2025) | 13,937 | 15,136 |
| Recent trend only (2022–2025) | 41,336 | 52,264 |

The ~3x disagreement between these two models *is* the finding: Sri Lanka's EV growth
rate has fundamentally shifted in the last 2–3 years, and any model trained on the full
history dilutes that signal.

</details>

---

## 🗂️ Data Source

Raw data provided by Sri Lanka's **Department of Motor Traffic (DMT)**. Each row
represents an aggregated count of vehicles by category, make, model, manufacture year,
and district — not one row per individual vehicle.

---

## 📁 Repository Structure

```
ev-sri-lanka-analysis/
├── data/
│   ├── raw/            # original untouched data
│   └── processed/      # cleaned dataset
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   └── 02_eda.ipynb
├── src/
│   └── cleaning.py     # reusable data cleaning functions
├── visuals/             # exported chart images
├── requirements.txt
└── README.md
```

---

## 🧪 Methodology

<details open>
<summary><b>1. Data Cleaning</b></summary>

- Fixed a district name typo (`invalid vavuniaya` → `VAVUNIYA`)
- Resolved 12 implausible/missing `manufacture_year` values, with the decision to retain
  (not drop) affected rows for non-time-based analysis
- Standardized and merged brand-name inconsistencies using **fuzzy string matching**
  (`difflib`), verifying each candidate against its `model` field before merging

</details>

<details>
<summary><b>2. Exploratory Data Analysis</b></summary>

- Vehicle category distribution
- Top makes by import volume
- District-level import totals

</details>

<details>
<summary><b>3. Advanced Analysis</b></summary>

- Time-series trend analysis + linear regression forecasting (long-term vs. short-term
  comparison)
- Geographic category-mix analysis (car vs. motorcycle share by district)
- **K-means clustering** of districts by EV adoption profile (elbow method for choosing k)

</details>

---

## 🛠️ Tech Stack

`Python` · `pandas` · `numpy` · `matplotlib` · `seaborn` · `scikit-learn` · `statsmodels` · `Jupyter`

---

## ▶️ How to Run

```bash
git clone https://github.com/kaushalsenevirathna/ev-sri-lanka-analysis.git
cd ev-sri-lanka-analysis
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
```

Then open the notebooks in `notebooks/` in VS Code or Jupyter, in order (`01` → `02`).

---

## 👤 Author

**Kaushal Senevirathna**
[LinkedIn](#) · [GitHub](https://github.com/kaushalsenevirathna)

<p align="center">⭐ If you found this project interesting, consider giving it a star!</p>
