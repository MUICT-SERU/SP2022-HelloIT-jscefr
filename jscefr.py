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
from alive_progress import alive_bar

report_features = ['Class', 'Level', 'Start Line', 'Start Column', 'Stop Line', 'Stop Column']

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
    absFilePath.replace('//', '/')
    print('Directory: ' + absFilePath)
    path = absFilePath
    try:
        directory = os.listdir(path)
        if 'node_modules' in directory:
            directory.remove('node_modules')
        # print(directory)
        for i in range(0, len(directory)):
            if directory[i].endswith('.js') or directory[i].endswith('.jsx'):
                pos = path + "/" + directory[i]
                pos.replace('//', '/')
                read_File(pos, repo)
            elif '.' not in directory[i]:
                print('\nOpening another directory...\n')
                path2 = absFilePath + '/' + directory[i]
                path2.replace('//', '/')
                try:
                    read_Directory(path2, repo)
                except NotADirectoryError:
                    pass
    except FileNotFoundError:
        pass

def read_File(pos, repo):
    """ Read the file and return the tree. """
    filename = str(pos.split('/')[-1])
    print('JavaScript File: ' + filename)
    input_stream = FileStream(pos, encoding='utf-8', errors='ignore')
    lexer = JavaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JscefrParser(stream)
    tree = parser.program()

    listener = JavaScriptParserListener()
    # length_json_comp_before = len(listener.get_comp())
    walker = JscefrWalker()
    walker.walk(listener, tree, 0, repo, pos)

    # summary = {}
    # summary[pos] = listener.get_comp()[length_json_comp_before : ]
    # save_summary(summary, repo, pos.replace('/', '-'))

# def json_to_csv(data):
#     csv_data = [['Repository', 'File Name', 'Class', 'Level']]
#     repository = list(data.keys())[0]
#     for file in data[repository]:
#         file_name = ''.join(file.split('.')[:-1])
#         for construct in data[repository][file]:
#             csv_data.append(
#                 [repository, file_name, construct['Class'], construct['Level']])
#     return csv_data

# def save_summary(data, repo, filename):
#     print(
#         f"created file = report_generators/analyzed_files/{repo}/{filename.replace('.js', '')}.json".replace('//', '/'))
#     with open(f"created file = report_generators/analyzed_files/{repo}/{filename.replace('.js', '')}.json".replace('//', '/'), 'w') as file:
#         file.write(json.dumps(data, indent=4))

# def show_result_new(data, num_files):
#     """ Returns the result of the analysis. """
#     result = '====================================='
#     result += '\nRESULT OF THE ANALYSIS:'
#     result += ('\nAnalyzed .js files: ' + str(num_files))
#     levels = {}
#     for val in data.values():
#         levels = val
#     levels = sorted(levels.items())
#     for key, value in levels:
#         result += ('\nElements of level ' + key + ': ' + str(value))
#     result += '\n====================================='
#     return result

# def write_to_file(dir_name):
    # # Gather all summary files
    # print(dir_name)
    # path = 'report_generators/analyzed_files/' + dir_name
    # SUMMARY = {
    #     "A1": 0,
    #     "A2": 0,
    #     "B1": 0,
    #     "B2": 0,
    #     "C1": 0,
    #     "C2": 0
    # }
    # directory = os.listdir(path)
    
    # num_files = len(directory)
    # cnt = 0
    # header = "{" + f"\"{dir_name}\":"
    
    # with alive_bar(num_files) as bar:
    #     for file in directory:
    #         # print(f'at {cnt}/{num_files}, reading {file}')
    #         cnt += 1
    #         read_file_content = json.load(open(path + '/' + file))
    #         for pair in read_file_content.values():
    #             for content in pair:
    #                 SUMMARY[content['Level']] += 1
    #         bar()
    #             # print(content)
    #             # sleep(0.5)
    # data = {}
    # data[dir_name] = SUMMARY
    # with open(f'report/result/{dir_name}.json', 'w') as file:
    #     file.write(json.dumps(data, indent=4))

    # print(show_result_new(data, num_files))
    # pass

def write_json_summary(repo):
    summary = {}
    data = {}
    with open('report_generators/data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            # comp_match = {'Class': row[2], 'Level': row[3]}
            comp_match = {}
            for i in range(len(report_features)):
                comp_match[report_features[i]] = row[i + 2]
            # print(comp_match)
            if row[1] in data.keys():
                data[row[1]].append(comp_match)
            else:
                data[row[1]] = [comp_match]
    summary[repo] = data
    
    with open('report_generators/data.json', 'w') as file:
        json.dump(summary, file, indent=4)

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

    if option.endswith('/'):
        option = option[:-1]

    repo_name = option.split('/')[-1]

    with open('report_generators/data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Repository', 'File Name'] + report_features)

    choose_option(repo_name)

    write_json_summary(repo_name)

    # write_to_file(repo_name)
    try:
        summary_Levels()
    except:
        print('Data empty. Cannot find any match.')