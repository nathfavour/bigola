"""Data loading and processing utilities."""

import pandas as pd


def load_and_clean_data(input_file_path, output_file_path):
    """Load the cars CSV, fix duplicates, missing headers, missing numeric values, and save cleaned data as a text file."""
    # load csv (assuming the CSV doesn't have a header row)
    columns = [
        'name', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear'
    ]
    df = pd.read_csv(input_file_path, names=columns)

    # drop duplicate entries
    df.drop_duplicates(inplace=True)

    # Replace missing numeric values with the mean
    numeric_cols = ['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # save the cleaned dataset to a text file
    df.to_csv(output_file_path, index=False)
    return df


def add_pass_regulations(df):
    """Add column indicating if mpg >= 25."""
    df['meets_regulations'] = [mpg_value >= 25 for mpg_value in df['mpg']]
    return df


def print_regulations_count(df):
    """Print how many cars pass the regulations."""
    passing = df['meets_regulations'].sum()
    print("Number of cars with >=25 mpg:", passing)
