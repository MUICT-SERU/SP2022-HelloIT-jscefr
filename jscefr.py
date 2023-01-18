import sys
import os
import json
import csv
import shutil
from antlr4 import *
from antlr_packages.python.JavaScriptLexer import JavaScriptLexer
from antlr_packages.python.JscefrParser import JscefrParser
from antlr_packages.python.JavaScriptParserListener import JavaScriptParserListener
from antlr_packages.python.JscefrWalker import JscefrWalker
from report_generators.getjson import read_Json
from report_generators.getcsv import read_FileCsv
from time import sleep

def choose_option(repo):
    """ Choose option. """
    if type_option == 'directory':
        # repo = option.split('/')[-1]
        # directory_dict = {}
        # directory_dict[repo] = read_Directory(option, repo)
        read_Directory(option, repo)
        # return directory_dict
    # elif type_option == 'repo-url':
    #     request_url()
    # elif type_option == 'user':
    #     run_user()
    else:
        sys.exit('Incorrect Option')

def read_Directory(absFilePath, repo):
    """ Extract the .js files from the directory. """
    pos = ''
    directory_dict = {}
    print('Directory: ')
    path = absFilePath
    try:
        directory = os.listdir(path)
        if 'node_modules' in directory:
            directory.remove('node_modules')
        print(directory)
        for i in range(0, len(directory)):
            if directory[i].endswith('.js') or directory[i].endswith('.jsx'):
                print('JavaScript File: ' + str(directory[i]))
                pos = path + "/" + directory[i]
                directory_dict[pos] = read_File(pos)
                save_summary(directory_dict, repo, pos.replace('/', '-'))
            elif '.' not in directory[i]:
                print('\nOpening another directory...\n')
                path2 = absFilePath + '/' + directory[i]
                try:
                    read_Directory(path2, repo)
                except NotADirectoryError:
                    pass
    except FileNotFoundError:
        pass

def read_File(pos):
    """ Read the file and return the tree. """
    input_stream = FileStream(pos, encoding='utf-8', errors='ignore')
    lexer = JavaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JscefrParser(stream)
    tree = parser.program()

    listener = JavaScriptParserListener()
    walker = JscefrWalker()
    walker.walk(listener, tree, 1)
    return listener.get_comp()


def json_to_csv(data):
    csv_data = [['Repository', 'File Name', 'Class', 'Level']]
    repository = list(data.keys())[0]
    for file in data[repository]:
        file_name = ''.join(file.split('.')[:-1])
        for construct in data[repository][file]:
            csv_data.append(
                [repository, file_name, construct['Class'], construct['Level']])
    return csv_data

def save_summary(data, repo, filename):
    print(
        f"created file = report_generators/analyzed_files/{repo}/{filename.replace('.js', '')}.json")
    with open(f"report_generators/analyzed_files/{repo}/{filename.replace('.js', '')}.json", 'w') as file:
        file.write(json.dumps(data, indent=4))

def show_result_new(data, num_files):
    """ Returns the result of the analysis. """
    result = '====================================='
    result += '\nRESULT OF THE ANALYSIS:'
    result += ('\nAnalyzed .js files: ' + str(num_files))
    levels = {}
    for val in data.values():
        levels = val
    levels = sorted(levels.items())
    for key, value in levels:
        result += ('\nElements of level ' + key + ': ' + str(value))
    result += '\n====================================='
    return result

def write_to_file(dir_name):
    # Gather all summary files
    print(dir_name)
    path = 'report_generators/analyzed_files/' + dir_name
    SUMMARY = {
        "A1": 0,
        "A2": 0,
        "B1": 0,
        "B2": 0,
        "C1": 0,
        "C2": 0
    }
    directory = os.listdir(path)
    # all_summaries = {}
    # print(directory)
    # sleep(5)
    num_files = len(directory)
    cnt = 0
    header = "{" + f"\"{dir_name}\":"
    # with open('report_generators/data.json', 'w') as file:
    #     file.write(header)
    for file in directory:
        print(f'at {cnt}/{num_files}, reading {file}')
        cnt += 1
        read_file_content = json.load(open(path + '/' + file))
        file_content = {}
        for pair in read_file_content.values():
            for content in pair:
                SUMMARY[content['Level']] += 1
                # print(content)
                # sleep(0.5)
            # file_content[pair] = read_file_content[pair]

            # print(f"{pair}: {read_file_content[pair]}")
            # all_summaries[pair] = read_file_content[pair]
    #     with open('report_generators/data.json', 'a') as file:
    #         file.write(json.dumps(file_content, indent=4))
    #         file.write(',')
    # footer = "}"
    # with open('report_generators/data.json', 'a') as file:
    #         file.write(footer)
    # data = {}
    # data[dir_name] = all_summaries
    # print('done dict creation')
    # Write to JSON file

    # print(SUMMARY)
    data = {}
    data[dir_name] = SUMMARY
    with open(f'report/result/{dir_name}.json', 'w') as file:
        file.write(json.dumps(data, indent=4))

    print(show_result_new(data, num_files))
    # Convert to CSV-type data
    # csv_data = json_to_csv(data)

    # Write to CSV file
    # with open('report_generators/data.csv', 'w') as file:
    #     writer = csv.writer(file)
    #     for row in csv_data:
    #         writer.writerow(row)

def summary_Levels():
    """ Summary of directory levels """
    result = read_Json()
    read_FileCsv()
    print(result)

if __name__ == '__main__':
    try:
        type_option = sys.argv[1]
        option = sys.argv[2]
    except:
        sys.exit("Usage: python3 file.js type-option('directory', " +
                 "'repo-url', 'user') option(directory, url, user)")

    repo_name = option.split(
        '/')[-1] if option.split('/')[-1] != '' else option.split('/')[-2]

    summary_dir_path = 'report_generators/analyzed_files/' + repo_name
    try:
        shutil.rmtree(summary_dir_path)
    except FileNotFoundError:
        pass
    os.makedirs(summary_dir_path)

    # print(repo_name)
    # sleep(5)
    choose_option(repo_name)

    try:
        os.mkdir('report/result')
    except FileExistsError:
        pass

    write_to_file(repo_name)
    try:
        # summary_Levels()
        pass
    except:
        print('Data empty. Cannot find any match.')