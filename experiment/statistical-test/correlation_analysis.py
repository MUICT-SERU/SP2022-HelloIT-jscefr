import json
import os
from scipy import stats
import pandas as pd
import sys

PROJECT = str(sys.argv[1])
SCORING_SYSTEM = str(sys.argv[2])
TYPE = ["LAYER", "LENGTH"]


for ttype in TYPE:
    df = pd.DataFrame(columns=["project", "type",
                      "corr", "p_val", "is_significant"])
    # data_type_x = []
    # data_type_y = []
    # for project in PROJECT:
    f = open(
        f'processed_data/{SCORING_SYSTEM}/{PROJECT}/{ttype}/dim_x.json')
    dataset_1 = json.loads(f.read())
    # data_type_x.append(dataset_1)
    f.close()
    f = open(
        f'processed_data/{SCORING_SYSTEM}/{PROJECT}/{ttype}/dim_y.json')
    dataset_2 = json.loads(f.read())
    # data_type_y.append(dataset_2)
    f.close()

    corr, p_val = stats.kendalltau(dataset_1, dataset_2)

    new_line = {"project": PROJECT, "type": ttype, "corr": corr,
                "p_val": p_val, "is_significant": p_val < 0.05}
    df = pd.concat([df, pd.DataFrame(new_line, index=[0])])

    # flatten_x = [item for sublist in data_type_x for item in sublist]
    # flatten_y = [item for sublist in data_type_y for item in sublist]
    # corr, p_val = stats.kendalltau(flatten_x, flatten_y)

    # new_line = {"project": "all", "type": ttype, "corr": corr,
    #             "p_val": p_val, "is_significant": p_val < 0.05}
    # df = pd.concat([df, pd.DataFrame(new_line, index=[0])])

    df.to_csv(f"./summary/{PROJECT}/{ttype}.csv", index=False)
