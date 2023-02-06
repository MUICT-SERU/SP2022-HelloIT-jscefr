import sys
import os
import json
import csv
import shutil
from antlr4 import *
from antlr_packages.python.JscefrFileStream import JscefrFileStream
from antlr_packages.python.JavaScriptLexer import JavaScriptLexer
from antlr_packages.python.JscefrParser import JscefrParser
from antlr_packages.python.JscefrWalker import JscefrWalker
from report_generators.getjson import read_Json
from report_generators.getcsv import read_FileCsv
from time import sleep
from alive_progress import alive_bar

report_features = ['Class', 'Level', 'Start Line', 'Start Column', 'Stop Line', 'Stop Column']

def choose_option(repo):
    """ Choose option. """
    if type_option == 'directory':
        read_Directory(option, repo)
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
    input_stream = JscefrFileStream(repo, pos, encoding='utf-8', errors='ignore')
    input_stream.detect_comments()
    lexer = JavaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JscefrParser(stream)
    tree = parser.program()

    listener = ParseTreeListener()
    walker = JscefrWalker()
    walker.walk(listener, tree, 0, repo, pos)

def write_json_summary(repo):
    summary = {}
    data = {}
    with open('report_generators/data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            comp_match = {}
            for i in range(len(report_features)):
                comp_match[report_features[i]] = row[i + 2]
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

    # write_json_summary(repo_name)

    # try:
    #     summary_Levels()
    # except:
    #     print('Data empty. Cannot find any match.')