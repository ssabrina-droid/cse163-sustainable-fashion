"""
eda.py

Exploratory Data Analysis for the Sustainable Fashion: Eco-Friendly
Trends dataset (Kaggle, waqi786/sustainable-fashion-eco-friendly-trends).

This module loads the dataset, summarizes the two variables of
interest (Eco_Friendly_Manufacturing and Waste_Production_KG),
produces two visualizations, and runs an independent-samples t-test
to check whether brands with eco-friendly manufacturing produce a
significantly different amount of waste than brands without it.

Run this file directly to regenerate all summaries and plots:
    python eda.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

DATA_PATH = 'data/sustainable_fashion_trends.csv'
OUTPUT_DIR = 'output'


def load_data(filepath):
    """
    Load the sustainable fashion dataset from the given CSV filepath
    and return it as a pandas DataFrame.
    """
    return pd.read_csv(filepath)


def check_missing_data(df):
    """
    Given a DataFrame, return a Series with the count of missing
    (NaN) values in each column. Used to verify whether the dataset
    has any missing data.
    """
    return df.isna().sum()


def seven_number_summary(df, column):
    """
    Given a DataFrame and the name of a quantitative column, return a
    dictionary containing the seven-number summary of that column:
    mean, standard deviation, minimum, first quartile, median, third
    quartile, and maximum.
    """
    series = df[column]
    return {
        'mean': series.mean(),
        'std': series.std(),
        'min': series.min(),
        'q1': series.quantile(0.25),
        'median': series.median(),
        'q3': series.quantile(0.75),
        'max': series.max(),
    }


def categorical_summary(df, column):
    """
    Given a DataFrame and the name of a categorical column, return a
    pandas Series with the count of each unique value in that column.
    """
    return df[column].value_counts()


def run_ttest(df, group_column, value_column):
    """
    Given a DataFrame, the name of a binary categorical column
    (group_column, expected values 'Yes'/'No'), and the name of a
    quantitative column (value_column), run an independent-samples
    (Welch's) t-test comparing the mean of value_column between the
    two groups. Returns a tuple (t_statistic, p_value).
    """
    yes_group = df[df[group_column] == 'Yes'][value_column]
    no_group = df[df[group_column] == 'No'][value_column]
    t_stat, p_value = stats.ttest_ind(yes_group, no_group, equal_var=False)
    return t_stat, p_value


def plot_waste_boxplot(df, output_path):
    """
    Create and save a boxplot comparing Waste_Production_KG between
    brands with and without eco-friendly manufacturing.
    """
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x='Eco_Friendly_Manufacturing',
                y='Waste_Production_KG')
    plt.title('Waste Production by Eco-Friendly Manufacturing Status')
    plt.xlabel('Eco-Friendly Manufacturing')
    plt.ylabel('Waste Production (KG)')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_waste_bar_means(df, output_path):
    """
    Create and save a bar chart of the mean Waste_Production_KG for
    each Eco_Friendly_Manufacturing group, with error bars showing
    the standard deviation.
    """
    summary = df.groupby('Eco_Friendly_Manufacturing')[
        'Waste_Production_KG'].agg(['mean', 'std']).reset_index()

    plt.figure(figsize=(7, 5))
    plt.bar(summary['Eco_Friendly_Manufacturing'], summary['mean'],
            yerr=summary['std'], capsize=8,
            color=['#4C72B0', '#55A868'])
    plt.title('Mean Waste Production by Eco-Friendly Manufacturing Status')
    plt.xlabel('Eco-Friendly Manufacturing')
    plt.ylabel('Mean Waste Production (KG)')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def main():
    df = load_data(DATA_PATH)

    print('Dataset shape (rows, columns):', df.shape)
    print()

    print('Missing values per column:')
    print(check_missing_data(df))
    print()

    print('Eco_Friendly_Manufacturing value counts:')
    print(categorical_summary(df, 'Eco_Friendly_Manufacturing'))
    print()

    print('Waste_Production_KG seven-number summary:')
    summary = seven_number_summary(df, 'Waste_Production_KG')
    for key, value in summary.items():
        print(f'  {key}: {value:.2f}')
    print()

    t_stat, p_value = run_ttest(
        df, 'Eco_Friendly_Manufacturing', 'Waste_Production_KG')
    print('Independent samples t-test:')
    print(f'  t-statistic: {t_stat:.4f}')
    print(f'  p-value: {p_value:.4f}')
    print()

    plot_waste_boxplot(df, f'{OUTPUT_DIR}/waste_boxplot.png')
    plot_waste_bar_means(df, f'{OUTPUT_DIR}/waste_bar_means.png')
    print('Saved visualizations to the output/ directory.')


if __name__ == '__main__':
    main()
