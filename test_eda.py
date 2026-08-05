"""
test_eda.py

Tests for the functions in eda.py. Uses a small, hand-built DataFrame
with known values so that the correct output of each function can be
computed by hand and checked with assert statements. Also runs the
summary functions on the real dataset as a sanity check (e.g. correct
shape, no unexpected missing values).
"""

import pandas as pd
from eda import (
    load_data,
    check_missing_data,
    seven_number_summary,
    categorical_summary,
    run_ttest,
)


def get_small_test_data():
    """
    Return a small, hand-built DataFrame that mimics the structure of
    the real dataset. Values are chosen so that summary statistics
    can be verified by hand.
    """
    return pd.DataFrame({
        'Eco_Friendly_Manufacturing': ['Yes', 'Yes', 'No', 'No', 'Yes'],
        'Waste_Production_KG': [10.0, 20.0, 30.0, 40.0, 50.0],
    })


def test_check_missing_data_no_missing():
    df = get_small_test_data()
    missing = check_missing_data(df)
    assert missing['Eco_Friendly_Manufacturing'] == 0
    assert missing['Waste_Production_KG'] == 0


def test_check_missing_data_with_missing():
    df = get_small_test_data()
    df.loc[0, 'Waste_Production_KG'] = None
    missing = check_missing_data(df)
    assert missing['Waste_Production_KG'] == 1


def test_seven_number_summary():
    df = get_small_test_data()
    summary = seven_number_summary(df, 'Waste_Production_KG')
    # Values [10, 20, 30, 40, 50]
    assert summary['mean'] == 30.0
    assert summary['min'] == 10.0
    assert summary['max'] == 50.0
    assert summary['median'] == 30.0
    # std computed with pandas default (ddof=1)
    assert round(summary['std'], 2) == 15.81


def test_categorical_summary():
    df = get_small_test_data()
    counts = categorical_summary(df, 'Eco_Friendly_Manufacturing')
    assert counts['Yes'] == 3
    assert counts['No'] == 2
    assert counts.sum() == 5


def test_run_ttest_identical_groups_gives_high_p_value():
    # If both groups have the exact same values, the t-test should
    # find no significant difference (p-value close to 1).
    df = pd.DataFrame({
        'Eco_Friendly_Manufacturing': ['Yes', 'Yes', 'No', 'No'],
        'Waste_Production_KG': [100.0, 200.0, 100.0, 200.0],
    })
    t_stat, p_value = run_ttest(
        df, 'Eco_Friendly_Manufacturing', 'Waste_Production_KG')
    assert round(t_stat, 4) == 0.0
    assert p_value > 0.9


def test_run_ttest_clearly_different_groups_gives_low_p_value():
    # If one group is much larger than the other, the t-test should
    # find a significant difference (small p-value).
    df = pd.DataFrame({
        'Eco_Friendly_Manufacturing': ['Yes'] * 10 + ['No'] * 10,
        'Waste_Production_KG': [1000.0] * 10 + [1.0] * 10,
    })
    t_stat, p_value = run_ttest(
        df, 'Eco_Friendly_Manufacturing', 'Waste_Production_KG')
    assert p_value < 0.01


def test_real_dataset_loads_and_has_expected_shape():
    df = load_data('data/sustainable_fashion_trends.csv')
    assert df.shape[0] == 5000
    assert 'Eco_Friendly_Manufacturing' in df.columns
    assert 'Waste_Production_KG' in df.columns


def test_real_dataset_has_no_missing_values():
    df = load_data('data/sustainable_fashion_trends.csv')
    missing = check_missing_data(df)
    assert missing.sum() == 0


def main():
    test_check_missing_data_no_missing()
    test_check_missing_data_with_missing()
    test_seven_number_summary()
    test_categorical_summary()
    test_run_ttest_identical_groups_gives_high_p_value()
    test_run_ttest_clearly_different_groups_gives_low_p_value()
    test_real_dataset_loads_and_has_expected_shape()
    test_real_dataset_has_no_missing_values()
    print('All tests passed!')


if __name__ == '__main__':
    main()
