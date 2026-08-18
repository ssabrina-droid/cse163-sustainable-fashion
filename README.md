# Does Eco-Friendly Manufacturing Reduce Waste? An Exploratory Analysis of Sustainable Fashion Brands

## Required Downloads / Installations

This project uses Python 3 and the following libraries:

- pandas
- matplotlib
- seaborn
- scipy

Install them with:

```
pip install pandas matplotlib seaborn scipy
```

### Data

This project uses the "Sustainable Fashion: Eco-Friendly Trends"
dataset from Kaggle, created by Waqar Ali:
https://www.kaggle.com/datasets/waqi786/sustainable-fashion-eco-friendly-trends

A copy of the exact CSV file used in this analysis is included in
this repository at `data/sustainable_fashion_trends.csv`, so no
download is required to reproduce the results. If you would like to
re-download it yourself, create a free Kaggle account, sign in, and
click "Download" on the dataset page (or retrieve it programmatically
with the `kagglehub` package), then place the CSV at
`data/sustainable_fashion_trends.csv`.

## Files

- `data_processing.py` — Loads the dataset from CSV and computes
  summary statistics: missing-value counts, the seven-number summary
  of `Waste_Production_KG`, and the value counts of
  `Eco_Friendly_Manufacturing`. Can be run on its own to print these
  summaries.
- `analysis.py` — Runs the independent-samples (Welch's) t-test
  comparing `Waste_Production_KG` between the `Eco_Friendly_
  Manufacturing` groups, and generates the two visualizations (a
  boxplot and a bar chart of group means) used in the report. Imports
  from `data_processing.py`. This is the main file to run to
  reproduce the report's results.
- `test_eda.py` — Tests for the functions in `data_processing.py` and
  `analysis.py`, using small hand-built DataFrames with known values,
  plus sanity checks against the real dataset.
- `data/sustainable_fashion_trends.csv` — The dataset used in this
  analysis.
- `output/` — Folder where generated plots (`waste_boxplot.png`,
  `waste_bar_means.png`) are saved.

## How to Run

1. Clone this repository and `cd` into it.
2. Install the required libraries listed above.
3. Make sure `data/sustainable_fashion_trends.csv` is present (it is
   included in this repo).
4. Run the analysis:

   ```
   python analysis.py
   ```

   This prints the missing-data check, summary statistics, and
   t-test results to the console, and saves the two plots to
   `output/waste_boxplot.png` and `output/waste_bar_means.png`.

5. (Optional) Run just the data summaries on their own:

   ```
   python data_processing.py
   ```

6. To run the tests:

   ```
   python test_eda.py
   ```

   All tests should print `All tests passed!` with no assertion
   errors.

## Notes

- All file paths in the code are relative to the repository root, so
  commands should be run from the root of the repository.
- The `output/` folder must exist before running `analysis.py` (it is
  included in this repo already).
