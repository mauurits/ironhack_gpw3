import pandas as pd
import numpy as np

def clean_dataframe(df):
    # Step 1: Lowercase column names and replace white spaces with underscores
    df.columns = [col.replace(" ", "_").lower() for col in df.columns]
    # Step 2: Fill NaN values with group means and medians based on city and year
    fill_na_strategies = {
        'premature_deaths': 'mean',
        'years_of_life_lost': 'median',
        'premature_deaths_-_lower_ci': 'median',
        'premature_deaths_-_upper_ci': 'median',
        'years_of_life_lost_-_lower_ci': 'median',
        'years_of_life_lost_-_upper_ci': 'median'
    }
    for column, strategy in fill_na_strategies.items():
        if strategy == 'mean':
            df[column] = df.groupby(['city', 'year'])[column].transform(lambda group: group.fillna(group.mean()))
        elif strategy == 'median':
            df[column] = df.groupby(['city', 'year'])[column].transform(lambda group: group.fillna(group.median()))
    # Step 3: Remove duplicated rows
    df = df.drop_duplicates()
    # Step 4: Drop the 'city_code' column
    if 'city_code' in df.columns:
        df = df.drop('city_code', axis=1)
    # Step 5: Reset the index
    df = df.reset_index(drop=True)
    return df

