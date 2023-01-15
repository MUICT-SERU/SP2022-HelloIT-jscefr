import json
import os

directory = './input/NPM_package_patch'
FILE_LIST = os.listdir(directory)
PROGRESS_BAR = 80


def update_status(now, total):
    os.system('clear')
    print('File count: ' + str(now) + '/' + str(total))
    print('Progress: [' + '#' * int(now * PROGRESS_BAR / total) +
          '·' * (int((total - now) * PROGRESS_BAR / total) + 1) + ']')


def convert(directory, filename):
    f = open(directory + '/' + filename)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    PR_NUM = filename[:-5]
    # print(f'PR = {PR_NUM}')

    # Iterating through the json

    for commit_num, commit in data.items():
        COMMIT_ID = commit['commit_id']
        COMMIT_USER = commit['submitter_name']
        COMMIT_DATETIME = commit['committer_date']
        COMMIT_DATE = COMMIT_DATETIME.split(' ')[0]
        COMMIT_TIME = COMMIT_DATETIME.split(' ')[1]
        COMMIT_PATH = f'./output/{PR_NUM}/{commit_num}'
        isExist = os.path.exists(COMMIT_PATH)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(COMMIT_PATH)

        for file_name, file_data in commit['files'].items():
            # print(f'File = {file_name}')
            FILENAME = file_name.split('/')[-1]
            if file_name[-3:] == '.js':
                index = -1
                pointer = 0
                # print(f'Step = {index}')
                if 'added_lines' in file_data:
                    for line, value in file_data['added_lines'].items():
                        # print(f'prev = {pointer}, now = {line}')
                        # print(line + ' ' + value)
                        if abs(int(line) - pointer) > 1:
                            index += 1
                        # print(index)
                        with open(f'{COMMIT_PATH}/{COMMIT_USER}_{COMMIT_ID}_{COMMIT_DATE}_{COMMIT_TIME}_{FILENAME}_{index}.js', "a") as write_file:
                            write_file.write(value + '\n')
                            write_file.close()
                        # pointer = int(line)
                            # write_file.close()

    # Closing file
    f.close()


for file in FILE_LIST:
    update_status(FILE_LIST.index(file), len(FILE_LIST))
    convert(directory, file)
