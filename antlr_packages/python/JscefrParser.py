from antlr4 import *
import sys
from .JavaScriptParser import JavaScriptParser
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

class JscefrParser( JavaScriptParser ):

    def program(self):

        localctx = JavaScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self.enterOuterAlt(localctx, 1)
        self.state = 155
        self._errHandler.sync(self)
        la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
        if la_ == 1:
            self.state = 154
            self.match(JavaScriptParser.HashBangLine)


        self.state = 158
        self._errHandler.sync(self)
        la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
        if la_ == 1:
            self.state = 157
            self.sourceElements()


        self.state = 160
        try:
            self.match(JavaScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
    
    @staticmethod
    def isSpecialRule(ctx, match, name):
        code_construct = JscefrParser.get_rule_name(ctx)
        # check if the code construct falls into the class name rule
        class_name = JscefrParser.get_class_name(ctx).replace('Context', '')
        if class_name.replace(class_name[0], class_name[0].lower()) == name:
            return True
        # check if the code construct is searched keyword(s)
        elif (code_construct == 'identifier' and ctx.start.text == name) or (code_construct == 'singleExpression' and len(name.split('.')) > 1 and (ctx.start.text == name.split('.')[0] and ctx.stop.text == name.split('.')[-1])):
            return True
        # check if the code construct is a static statement
        elif code_construct == 'statement' and ctx.start.text == 'static' and name == 'staticStatement':
            return True
        
        elif code_construct == 'numericLiteral':
            # check if the code construct is a float literal
            if '.' in ctx.start.text and name == 'floatLiteral':
                return True
            # check if the code construct is an exponential literal
            elif 'e' in ctx.start.text and all([alp.isnumeric() for alp in ctx.start.text if alp != 'e']) and name == 'exponentialLiteral':
                return True
        
        elif code_construct == 'literal':
            # check if the code construct is a string literal
            if ((ctx.start.text[0] == '\'' and ctx.start.text[-1] == '\'') or (ctx.start.text[0] == '\"' and ctx.start.text[-1] == '\"')) and name == 'stringLiteral':
                return True
            # check if the code construct is a regular expression
            elif (ctx.start.text[0] == '/' and ctx.start.text[-1] == '/') and name == 'RegExp':
                return True
        
        # check if the code construct is an async expression
        elif code_construct == 'functionDeclaration' and ctx.start.text == 'async' and name == 'asyncExpression':
            return True
        # check if the code construct is a function with args parameter
        elif code_construct == 'functionBody' and JscefrParser.has_args(ctx) and name == 'argsParameter':
            return True
        
        # check if the code construct is an aggregating module expression
        elif code_construct == 'importFromBlock' and ctx.start.text == '*' and name == 'aggregatingModuleExpression':
            return True
        # check if the code construct is a module creation
        elif code_construct == 'importNamespace' and ctx.start.text != ctx.stop.text and name == 'createModule':
            return True
        
        children_nodes = JscefrParser.get_valid_children(ctx)

        # check if the code construct has a bracket notation
        if class_name == 'MemberIndexExpression' and any([not child.start.text.isnumeric() for child in children_nodes if JscefrParser.get_rule_name(child) == 'expressionSequence']) and name == 'bracketNotation':
            return True
        # check if the code construct is a method keyword
        method_keywords = ['includes', 'startWith', 'endWith', 'indexOf', 'slice', 'toUpperCase', 'toLowerCase', 'replace', 'replaceAll', 'push', 'unshift', 'pop', 'splice', 'split', 'join', 'map', 'shift', 'toString', 'stopPropagation', 'filter', 'focus']
        for m_keyword in method_keywords:
            if code_construct == 'singleExpression' and {'singleExpression', 'arguments'}.issubset(set(map(JscefrParser.get_rule_name, children_nodes))):
                for child in children_nodes:
                    if JscefrParser.get_rule_name(child) == 'singleExpression' and JscefrParser.get_class_name(child).replace("Context", "") == 'MemberDotExpression' and child.stop.text == m_keyword and name == f'{m_keyword}Method':
                        return True
        # check if the code construct is a default parameter
        if code_construct == 'formalParameterArg' and 'singleExpression' in [JscefrParser.get_rule_name(child) for child in children_nodes] and name == 'defaultParameter':
            return True
        
        props = ['value', 'writable', 'enumerable', 'configurable', 'get', 'set']
        # check if the code construct is a data or accessor property
        if code_construct == 'singleExpression':
            for data_prop in props:
                if len(children_nodes) > 0 and ctx.stop.text == data_prop:
                    for child in children_nodes:
                        if child.stop.text == data_prop and name == (data_prop + 'Property'):
                            return True
        # check if the code construct is a function expression
        elif code_construct == 'variableDeclaration' and any([child.start.text == 'function' and JscefrParser.get_rule_name(child) == 'singleExpression' for child in children_nodes]) and name == 'functionExpression':
            return True
        else:
            return None
    
    @staticmethod
    def get_valid_children(ctx):
        return [child for child in (ctx.children or []) if (JscefrParser.get_class_name(child) != 'TerminalNodeImpl') and (JscefrParser.get_class_name(child) != 'ErrorNodeImpl')]
    
    @staticmethod
    def get_rule_name(ctx):
        try:
            return JscefrParser.ruleNames[ctx.getRuleIndex()]
        except:
            return None
    
    @staticmethod
    def get_class_name(ctx):
        return ctx.__class__.__name__
    
    @staticmethod
    def has_args(ctx):
        children_nodes = JscefrParser.get_valid_children(ctx)
        
        if len(children_nodes) > 0:
            for child_node in children_nodes:
                return False or JscefrParser.has_args(child_node)
        try:
            if JscefrParser.get_rule_name(ctx) == 'identifier' and ctx.start.text == 'args':
                return True
            else:
                return False
        except:
            return False