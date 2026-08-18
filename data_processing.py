"""
data_processing.py

Data loading and summary statistics for the Sustainable Fashion:
Eco-Friendly Trends dataset (Kaggle, waqi786/sustainable-fashion-
eco-friendly-trends).

This module is responsible for loading the raw CSV data and computing
the summary statistics used throughout the project: missing-value
counts, the seven-number summary of a quantitative column, and the
value counts of a categorical column.

Run this file directly to print the summary statistics for the
dataset:
    python data_processing.py
"""

import pandas as pd

DATA_PATH = 'data/sustainable_fashion_trends.csv'


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


if __name__ == '__main__':
    main()
