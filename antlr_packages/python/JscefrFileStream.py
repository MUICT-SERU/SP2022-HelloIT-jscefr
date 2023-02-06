from antlr4 import *
from .JscefrReportNoter import JscefrReportNoter

class JscefrFileStream(FileStream):

    def __init__(self, repo, fileName:str, encoding:str='ascii', errors:str='strict'):
        super().__init__(fileName, encoding, errors)
        self.repo = repo

    def detect_comments(self):
        stream_data = self.strdata.split('\n')
        comment_open = False
        first_line_comment = 1
        first_col_comment = 0
        try:
            comp_comment = [match for match in JscefrReportNoter.read_dict() if match['Class'] == 'comment'][0]
        except:
            pass

        for i in range(len(stream_data)):
            if comment_open:
                if stream_data[i].replace(' ', '').endswith('*/'):
                    comment_open = False
                    JscefrReportNoter.note(self.repo, self.fileName, comp_comment, [first_line_comment, first_col_comment, i + 1, len(stream_data[i]) - 1])
                else:
                    continue
            elif stream_data[i].replace(' ', '').startswith('//'):
                JscefrReportNoter.note(self.repo, self.fileName, comp_comment, [i + 1, stream_data[i].index('//'), i + 1, len(stream_data[i]) - 1])
            elif stream_data[i].replace(' ', '').startswith('/*'):
                comment_open = True
                first_line_comment = i + 1
                first_col_comment = stream_data[i].index('/*')