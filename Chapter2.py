# -*- coding: utf-8 -*-
import pandas as pd

housing = pd.DataFrame(0)

from sklearn.model_selection import  StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

housing["income_cat"].value_counts() / len(housing)

def income_cat_poportion(data):
    return data["income_cat"].value_counts() / len(data)

