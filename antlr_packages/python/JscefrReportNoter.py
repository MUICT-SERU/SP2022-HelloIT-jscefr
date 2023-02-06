import os, csv, json

class JscefrReportNoter():

    @staticmethod
    def read_dict():
        f = open(os.getcwd() + '/dictionary_converter/dict.json')
        data = json.load(f)
        return data

    @staticmethod
    def note(repo, filename, match, start_stop_line_col):
        with open(os.getcwd() + '/report_generators/data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([repo, filename] + list(match.values()) + start_stop_line_col)