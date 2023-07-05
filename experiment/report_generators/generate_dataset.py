import os
import json
import shutil
import sys
from alive_progress import alive_bar
from time import sleep

# PROJECT = str(sys.argv[1])
PROJECT = 'react'


# Skipping A1 and A2
skip = False

PATH = '../../jscefr_tool/report/DATA_JSON/' + PROJECT + '.json'

# SCORING_SYSTEM = "MAX" | "ALL"

# SCORING_SYSTEM = str(sys.argv[2])
SCORING_SYSTEM = "ALL"

# "LAYER" | "LENGTH" | "TEST"
CHOICE_LIST = ["LAYER", "LENGTH", "TEST"]

CHOICE = "TEST"

for c in CHOICE_LIST:
    print(f'doing {c} at {PATH}')

    try:
        shutil.rmtree(f'processed_data/{SCORING_SYSTEM}/{PROJECT}/{c}')
    except FileNotFoundError:
        pass

    os.makedirs(f'processed_data/{SCORING_SYSTEM}/{PROJECT}/{c}')

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

    if c == 'LAYER' or c == 'LENGTH':
        with open(f'{PATH}', 'r') as f:
            json_data = json.load(f)
            for project in json_data.values():
                with alive_bar(len(project)) as bar:
                    for file_name, file_data in project.items():
                        if SCORING_SYSTEM == 'ALL':
                            for level, amount in file_data['Levels'].items():
                                if skip and (DATA_COMP['Level'] == 'A1' or DATA_COMP['Level'] == 'A2'):
                                    pass
                                else:
                                    file_name = file_name.replace('//', '')
                                    if c == 'LAYER':
                                        dim_x_data = file_name.count('/') - 2
                                        dim_y.append(DATA_COMP[level])
                                        dim_x.append(dim_x_data)
                                    elif c == 'LENGTH':
                                        dim_x_data = len(file_name.split('/')[-1])
                                        dim_y.append(DATA_COMP[level])
                                        dim_x.append(dim_x_data)
                        elif SCORING_SYSTEM == 'MAX':
                            max_level = 'A1'
                            for level, amount in file_data['Levels'].items():
                                if DATA_COMP[level] > DATA_COMP[max_level]:
                                    max_level = level
                            if skip and (max_level == 'A1' or max_level == 'A2'):
                                pass
                            else:
                                file_name = file_name.replace('//', '')
                                if c == 'LAYER':
                                    dim_x_data = file_name.count('/') - 2
                                    dim_y.append(DATA_COMP[max_level])
                                    dim_x.append(dim_x_data)
                                elif c == 'LENGTH':
                                    dim_x_data = len(file_name.split('/')[-1])
                                    dim_y.append(DATA_COMP[max_level])
                                    dim_x.append(dim_x_data)
                        bar()


    elif c == 'TEST':
        with open(f'{PATH}', 'r') as f:
            json_data = json.load(f)
            for project in json_data.values():
                with alive_bar(len(project)) as bar:
                    for file_name, file_data in project.items():
                        # print(f"Working on {file_name}")
                        # print(file_data)
                            # print(construct)
                            # for level, amount in construct.items():
                        if SCORING_SYSTEM == 'ALL':
                            for level, amount in file_data['Levels'].items():
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
                        elif SCORING_SYSTEM == 'MAX':
                            max_level = 'A1'
                            if skip and (level == 'A1' or level == 'A2'):
                                pass
                            else:
                                for level, amount in file_data['Levels'].items():
                                    if DATA_COMP[level] > DATA_COMP[max_level]:
                                        max_level = level
                                if 'test' in file_name[IGNORE_LEN:]:
                                    for _ in range(amount):
                                        # print(f"Level: {level}")
                                        dim_x.append(DATA_COMP[max_level])
                                else:
                                    for _ in range(amount):
                                        # print(f"Level: {level}")
                                        dim_y.append(DATA_COMP[max_level])
                        bar()

    with open(f'processed_data/{SCORING_SYSTEM}/{PROJECT}/{c}/dim_x.json', 'w') as file:
        file.write(json.dumps((dim_x), indent=4))

    with open(f'processed_data/{SCORING_SYSTEM}/{PROJECT}/{c}/dim_y.json', 'w') as file:
        file.write(json.dumps((dim_y), indent=4))