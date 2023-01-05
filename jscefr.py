import sys, os, json, csv
from antlr4 import *
from antlr_packages.python.JavaScriptLexer import JavaScriptLexer
from antlr_packages.python.JavaScriptParser import JavaScriptParser
from antlr_packages.python.JavaScriptParserListener import JavaScriptParserListener
from antlr_packages.python.JscefrWalker import JscefrWalker
from report_generators.getjson import read_Json
from report_generators.getcsv import read_FileCsv

def choose_option():
    """ Choose option. """
    if type_option == 'directory':
        repo = option.split('/')[-1]
        directory_dict = {}
        directory_dict[repo] = read_Directory(option, repo)
        return directory_dict
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
        print(directory)
        for i in range(0, len(directory)):
            if directory[i].endswith('.js'):
                print('JavaScript File: ' + str(directory[i]))
                pos = path + "/" + directory[i]
                directory_dict[directory[i]] = read_File(pos)
            elif '.' not in directory[i]:
                # If the directory contains JS files that aren't coded by the project owner (such as libraries), it will skip that directory.
                print('\nOpening another directory...\n')
                path2 = absFilePath + '/' + directory[i]
                try:
                    directory_dict = read_Directory(path2, directory[i])
                except NotADirectoryError:
                    pass
    except FileNotFoundError:
        pass
    return directory_dict

def read_File(pos):
    """ Read the file and return the tree. """
    input_stream = FileStream(pos)
    lexer = JavaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaScriptParser(stream)
    tree = parser.program()
    # print(len([line for line in parser._input.tokenSource._input.data if line == 10]))

    listener = JavaScriptParserListener()
    length_comp_before = len(listener.get_comp())
    walker = JscefrWalker()
    walker.walk(listener, tree, 1)
    summary = listener.get_comp()[length_comp_before : ]
    return summary

def json_to_csv(data):
    csv_data = [['Repository', 'File Name', 'Class', 'Level']]
    repository = list(data.keys())[0]
    for file in data[repository]:
        file_name = ''.join(file.split('.')[:-1])
        for construct in data[repository][file]:
            csv_data.append([repository, file_name, construct['Class'], construct['Level']])
    return csv_data

def write_to_file(data):
    # Write to JSON file
    with open('report_generators/data.json', 'w') as file:
        file.write(json.dumps(data, indent=4))
    
    # Convert to CSV-type data
    csv_data = json_to_csv(data)

    # Write to CSV file
    with open('report_generators/data.csv', 'w') as file:
        writer = csv.writer(file)
        for row in csv_data:
            writer.writerow(row)

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
    data = choose_option()
    # write_to_file(data)
    # summary_Levels()