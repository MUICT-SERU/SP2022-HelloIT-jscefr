import os
import json
import shutil
import sys
from alive_progress import alive_bar
from time import sleep

PROJECT = 'next.js'

# Skipping A1 and A2
skip = False

PATH = '../report/DATA_JSON/' + PROJECT + '.json'

# "LAYER" | "LENGTH" | "TEST"
CHOICE = "TEST"

print(f'doing {CHOICE} at {PATH}')

try:
    shutil.rmtree(f'processed_data/{PROJECT}/{CHOICE}')
except FileNotFoundError:
    pass

os.makedirs(f'processed_data/{PROJECT}/{CHOICE}')

DATA_COMP = {
    'A1': 1,
    'A2': 2,
    'B1': 3,
    'B2': 4,
    'C1': 5,
    'C2': 6,
}

dim_y = []
dim_x = []

data_dict = {}

IGNORE_LEN = len(PROJECT) + len('input_dataset') + 1

with open(f'{PATH}', 'r') as f:
    json_data = json.load(f)
    for project in json_data.values():
        with alive_bar(len(project)) as bar:
            for file_name, file_data in project.items():
                # print(f"Working on {file_name}")
                # print(file_data)
                for level, amount in file_data['Levels'].items():
                    # print(construct)
                    # for level, amount in construct.items():
                    if skip and (level == 'A1' or level == 'A2'):
                        pass
                    else:
                        if 'test' in file_name[IGNORE_LEN:]:
                            for _ in range(amount):
                                # print(f"Level: {level}")
                                dim_x.append(DATA_COMP[level])
                        else:
                            for _ in range(amount):
                                # print(f"Level: {level}")
                                dim_y.append(DATA_COMP[level])
                bar()

with open(f'processed_data/{PROJECT}/{CHOICE}/test.json', 'w') as file:
    file.write(json.dumps((dim_x), indent=4))

with open(f'processed_data/{PROJECT}/{CHOICE}/non_test.json', 'w') as file:
    file.write(json.dumps((dim_y), indent=4))