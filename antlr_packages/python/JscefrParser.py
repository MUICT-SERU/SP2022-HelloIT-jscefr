from antlr4 import *
import sys
from .JavaScriptParser import JavaScriptParser
from .JavaScriptParserListener import JavaScriptParserListener
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

class JscefrParser( JavaScriptParser ):
    
    @staticmethod
    def isSpecialRule(ctx, match, name, listener):
        code_construct = JscefrParser.ruleNames[ctx.getRuleIndex()]
        class_name = ctx.__class__.__name__
        # check if the code construct falls into the basic rule
        if class_name.replace('Context', '').lower() == name.lower():
            return match
        # check if the code construct is searched keyword(s)
        elif (code_construct == 'identifier' and ctx.start.text.lower() == name.lower()) or (code_construct == 'singleExpression' and len(name.split('.')) > 1 and (ctx.start.text.lower() == name.split('.')[0].lower() and ctx.stop.text.lower() == name.split('.')[-1].lower())):
            return match
        
        elif code_construct == 'numericLiteral':
            # check if the code construct is a float literal
            if '.' in ctx.start.text and name.lower() == 'floatLiteral'.lower():
                return match
            # check if the code construct is an exponential literal
            elif 'e' in ctx.start.text and name.lower() == 'exponentialLiteral'.lower():
                return match
        
        elif code_construct == 'literal':
            # check if the code construct is a string literal
            if ((ctx.start.text[0] == '\'' and ctx.start.text[-1] == '\'') or (ctx.start.text[0] == '\"' and ctx.start.text[-1] == '\"')) and name.lower() == 'stringLiteral'.lower():
                return match
            # check if the code construct is a regular expression literal
            elif (ctx.start.text[0] != '\'' and ctx.start.text[-1] != '\'') and '/' in ctx.start.text and name.lower() == 'RegExp'.lower():
                return match
        # check if the code construct is an aggregating module expression
        elif code_construct == 'importFromBlock' and ctx.start.text == '*' and name.lower() == 'aggregatingModuleExpression'.lower():
            return match
        # check if the code construct is an async expression
        elif code_construct == 'functionDeclaration' and ctx.start.text.lower() == 'async' and name.lower() == 'asyncExpression'.lower():
            return match
        else:
            return None