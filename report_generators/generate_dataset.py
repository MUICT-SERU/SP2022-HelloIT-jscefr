import os
import json
import shutil
from alive_progress import alive_bar

SUB_FOLDER = 'packages'

# Skipping A1 and A2
skip = False

PATH = 'analyzed_files/' + SUB_FOLDER

# "LAYER" | "LENGTH" | "TEST"
CHOICE = "LENGTH"

print(f'doing {CHOICE} at {PATH}')

try:
    shutil.rmtree(f'processed_data/{SUB_FOLDER}/{CHOICE}')
except FileNotFoundError:
    pass

os.makedirs(f'processed_data/{SUB_FOLDER}/{CHOICE}')

DATA_COMP = {
    'A1': 1,
    'A2': 2,
    'B1': 3,
    'B2': 4,
    'C1': 5,
    'C2': 6,
}

list_dir = os.listdir(PATH)

dim_y = []
dim_x = []

data_dict = {}

if CHOICE == 'LAYER' or CHOICE == 'LENGTH':
    with alive_bar(len(list_dir)) as bar:
        for file_dir in list_dir:
            with open(f'{PATH}/{file_dir}', 'r') as file:
                json_data = json.load(file)
                for file_name, file_data in json_data.items():
                    for construct in file_data:
                        mock = 'test/react/fixtures/art/VectorWidget.js'
                        if skip and (construct['Level'] == 'A1' or construct['Level'] == 'A2'):
                            pass
                        else:
                            file_name = file_name.replace('//', '')
                            if CHOICE == 'LAYER':
                                dim_x_data = file_name.count('/') - 2
                                dim_y.append(DATA_COMP[construct['Level']])
                                dim_x.append(dim_x_data)
                                # if dim_x_data not in data_dict.keys():
                                #     data_dict[dim_x_data] = []
                                # else:
                                #     data_dict[dim_x_data].append(DATA_COMP[construct['Level']])
                            elif CHOICE == 'LENGTH':
                                dim_x_data = len(file_name.split('/')[-1])
                                dim_y.append(DATA_COMP[construct['Level']])
                                dim_x.append(dim_x_data)
            bar()

    with open(f'processed_data/{SUB_FOLDER}/{CHOICE}/dim_x.json', 'w') as file:
        file.write(json.dumps((dim_x), indent=4))

    with open(f'processed_data/{SUB_FOLDER}/{CHOICE}/dim_y.json', 'w') as file:
        file.write(json.dumps((dim_y), indent=4))
    # print(max(dim_x))
    # print(data_dict)

elif CHOICE == 'TEST':
    with alive_bar(len(list_dir)) as bar:
        for file_dir in list_dir:
            with open(f'{PATH}/{file_dir}', 'r') as file:
                json_data = json.load(file)
                for file_name, file_data in json_data.items():
                        for construct in file_data:
                            if skip and (construct['Level'] == 'A1' or construct['Level'] == 'A2'):
                                pass
                            else:
                                if 'test' in file_name[4:]:
                                    dim_x.append(DATA_COMP[construct['Level']])
                                else:
                                    dim_y.append(DATA_COMP[construct['Level']])
            bar()

    with open(f'processed_data/{SUB_FOLDER}/{CHOICE}/test.json', 'w') as file:
        file.write(json.dumps((dim_x), indent=4))

    with open(f'processed_data/{SUB_FOLDER}/{CHOICE}/non_test.json', 'w') as file:
        file.write(json.dumps((dim_y), indent=4))
