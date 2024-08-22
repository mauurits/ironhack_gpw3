import pandas as pd


def fill_na_with_group_mean(group):
    return group.fillna(group.median())




