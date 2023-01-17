import sys, os, json, csv, shutil
from antlr4 import *
from antlr_packages.python.JavaScriptLexer import JavaScriptLexer
from antlr_packages.python.JscefrParser import JscefrParser
from antlr_packages.python.JavaScriptParserListener import JavaScriptParserListener
from antlr_packages.python.JscefrWalker import JscefrWalker
from report_generators.getjson import read_Json
from report_generators.getcsv import read_FileCsv

def choose_option():
    """ Choose option. """
    if type_option == 'directory':
        # repo = option.split('/')[-1]
        # directory_dict = {}
        # directory_dict[repo] = read_Directory(option, repo)
        read_Directory(option, option.split('/')[-1])
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
                save_summary(directory_dict, pos.replace('/', '-'))
            elif '.' not in directory[i]:
                print('\nOpening another directory...\n')
                path2 = absFilePath + '/' + directory[i]
                try:
                    read_Directory(path2, directory[i])
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
            csv_data.append([repository, file_name, construct['Class'], construct['Level']])
    return csv_data

def save_summary(data, filename):
    with open(f"report_generators/analyzed_files/{filename.replace('.js', '')}.json", 'w') as file:
        file.write(json.dumps(data, indent=4))

def write_to_file(dir_name):
    # Gather all summary files
    path = 'report_generators/analyzed_files'
    directory = os.listdir(path)
    all_summaries = {}
    for file in directory:
        read_file_content = json.load(open(path + '/' + file))
        for pair in read_file_content:
            # print(f"{pair}: {read_file_content[pair]}")
            all_summaries[pair] = read_file_content[pair]
    data = {}
    data[dir_name] = all_summaries

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

    summary_dir_path = 'report_generators/analyzed_files'
    try:
        shutil.rmtree(summary_dir_path)
    except FileExistsError:
        pass
    os.mkdir(summary_dir_path)
    
    choose_option()
    write_to_file(option.split('/')[-1])
    try:
        summary_Levels()
    except:
        print('Data empty. Cannot find any match.')