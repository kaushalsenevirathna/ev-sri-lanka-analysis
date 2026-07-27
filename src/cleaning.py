"""
Cleaning functions for the EV Sri Lanka vehicle import dataset.
These functions take the raw DataFrame and apply the documented cleaning
decisions made in notebooks/01_data_cleaning.ipynb.
"""

import numpy as np


def fix_district_names(df):
    """Fix known typo: 'invalid vavuniaya' -> 'VAVUNIYA'."""
    df['district'] = df['district'].replace('invalid vavuniaya', 'VAVUNIYA')
    return df


def clean_manufacture_year(df, valid_min=1900, valid_max=2025):
    """Set implausible manufacture_year values (outside valid_min-valid_max) to NaN."""
    df.loc[
        (df['manufacture_year'] < valid_min) | (df['manufacture_year'] > valid_max),
        'manufacture_year'
    ] = np.nan
    return df


def standardize_make(df):
    """Strip whitespace, uppercase, and merge known typo/duplicate make values."""
    df['make'] = df['make'].str.strip().str.upper()

    make_corrections = {
        'CITROAN': 'CITROEN',
        'DONG FENG': 'DONGFENG',
        'VOLKSWAGON': 'VOLKSWAGEN',
        'YADIA': 'YADEA',
        'MG4': 'MG',
        'NISSAN MT': 'NISSAN',
        '-': 'UNKNOWN',
    }
    df['make'] = df['make'].replace(make_corrections)
    return df


def clean_ev_data(df):
    """Run the full cleaning pipeline on the raw EV dataset."""
    df = df.iloc[:, :6].copy()
    df.columns = ['vehicle_category', 'make', 'model', 'manufacture_year', 'district', 'count']

    df = fix_district_names(df)
    df = clean_manufacture_year(df)
    df = standardize_make(df)

    df['manufacture_year'] = df['manufacture_year'].astype('Int64')
    return df