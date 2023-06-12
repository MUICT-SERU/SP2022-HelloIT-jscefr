import json
import pandas as pd
from scipy import stats
import numpy as np
from tabulate import tabulate
import sys
import os
import shutil

# PROJECT = ['next', 'react', 'sveltekit']
# SCORING_TYPE = 'MAX'

PROJECT = str(sys.argv[1])
SCORING_SYSTEM = str(sys.argv[2])

try:
    shutil.rmtree(f'summary/{PROJECT}')
except FileNotFoundError:
    pass

os.makedirs(f'summary/{PROJECT}')

# for project in PROJECT:
f = open(f'processed_data/{SCORING_SYSTEM}/{PROJECT}/LAYER/dim_y.json')
raw = json.loads(f.read())
f.close()
# f = open(f'../processed_data/MAX/{project}/LAYER/dim_y.json')
# raw_max = json.loads(f.read())
# f.close()

# NUM_FILES = {
#     'A1': 0,
#     'A2': 0,
#     'B1': 0,
#     'B2': 0,
#     'C1': 0,
#     'C2': 0,
# }
NUM_COMP = {
    'A1': 0,
    'A2': 0,
    'B1': 0,
    'B2': 0,
    'C1': 0,
    'C2': 0,
}

list_all = list(raw)
# list_max = list(raw_max)
COMPETENCY = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
for i in range(6):
    NUM_COMP[COMPETENCY[i]] = list_all.count(i + 1)
    # NUM_FILES[COMPETENCY[i]] = list_max.count(i + 1)

# print(NUM_COMP)
# print(NUM_FILES)

df_num = pd.DataFrame({'Competency': COMPETENCY, 'Number of Code Construct': NUM_COMP.values(
)})

TOTAL_COMP = sum(NUM_COMP.values())
# TOTAL_FILES = sum(NUM_FILES.values())

df_num = pd.concat([df_num, pd.DataFrame({'Competency': ['Total'], 'Number of Code Construct': [
                    TOTAL_COMP]})], ignore_index=True)

# print(project)
print(tabulate(df_num, headers='keys', tablefmt='psql'))
df_num.to_csv(f'summary/{PROJECT}/construct.csv', index=False)
