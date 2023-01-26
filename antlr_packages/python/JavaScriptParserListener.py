# Generated from JavaScriptParser.g4 by ANTLR 4.11.1
import json
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JavaScriptParser import JavaScriptParser
else:
    from JavaScriptParser import JavaScriptParser

# This class defines a complete listener for a parse tree produced by JavaScriptParser.
class JavaScriptParserListener(ParseTreeListener):

    # array of dictionaty matching btw construct / lv
    # handle if comp is empty
    comp = []
    comp_dict_key = ['Class', 'Level', 'Start Line', 'Start Column', 'Stop Line', 'Stop Column']
    traverse_result = []
    traverse_result_dict_key = ['Layer', 'Class', 'Start Line', 'Start Column', 'Stop Line', 'Stop Column', 'Start Text', 'Stop Text', 'Children Classes', 'Belongs to']

    def insert_values(self, values):
        self.comp.append({self.comp_dict_key[i]: values[i] for i in range(len(self.comp_dict_key))})
    
    def add_to_traverse_result(self, values):
        self.traverse_result.append({self.traverse_result_dict_key[i]: values[i] for i in range(len(self.traverse_result_dict_key))})
    
    def get_comp(self):
        return self.comp
    
    # def reset_comp(self):
    #     self.comp = []
    
    def get_traverse_result(self):
        return self.traverse_result
    
    # Enter a parse tree produced by JavaScriptParser#program.
    def enterProgram(self, ctx:JavaScriptParser.ProgramContext):
        # print(f'E nter Program: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#program.
    def exitProgram(self, ctx:JavaScriptParser.ProgramContext):
        # print(f'Exit Program: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#sourceElement.
    def enterSourceElement(self, ctx:JavaScriptParser.SourceElementContext):
        # print(f'E nter Source Element: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#sourceElement.
    def exitSourceElement(self, ctx:JavaScriptParser.SourceElementContext):
        # print(f'Exit Source Element: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#statement.
    def enterStatement(self, ctx:JavaScriptParser.StatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Statement', 0, 0, 0, self.level_dict['Code Construct'][0]['statement']])
        # print(f'E nter Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#statement.
    def exitStatement(self, ctx:JavaScriptParser.StatementContext):
        # print(f'Exit Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#block.
    def enterBlock(self, ctx:JavaScriptParser.BlockContext):
        # self.insert_values(self.json_comp_dict_key, ['Block', 0, 0, 0, 'A1'])
        # print(f'E nter Block: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#block.
    def exitBlock(self, ctx:JavaScriptParser.BlockContext):
        # print(f'Exit Block: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#statementList.
    def enterStatementList(self, ctx:JavaScriptParser.StatementListContext):
        # self.insert_values(self.json_comp_dict_key, ['Statement List', 0, 0, 0, 'A1'])
        # print(f'E nter Statement List: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#statementList.
    def exitStatementList(self, ctx:JavaScriptParser.StatementListContext):
        # print(f'Exit Statement List: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#importStatement.
    def enterImportStatement(self, ctx:JavaScriptParser.ImportStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Import Statement', 'B1'])
        # print(f'E nter Import Element: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#importStatement.
    def exitImportStatement(self, ctx:JavaScriptParser.ImportStatementContext):
        # print(f'Exit Import Element: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#importFromBlock.
    def enterImportFromBlock(self, ctx:JavaScriptParser.ImportFromBlockContext):
        # self.insert_values(self.json_comp_dict_key, ['Import from Block', 'B1'])
        # print(f'E nter Import from Block: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#importFromBlock.
    def exitImportFromBlock(self, ctx:JavaScriptParser.ImportFromBlockContext):
        # print(f'Exit Import from Block: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#moduleItems.
    def enterModuleItems(self, ctx:JavaScriptParser.ModuleItemsContext):
        # self.insert_values(self.json_comp_dict_key, ['Module Items', 'B1'])
        # print(f'E nter Module Items: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#moduleItems.
    def exitModuleItems(self, ctx:JavaScriptParser.ModuleItemsContext):
        # print(f'Exit Module Items: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#importDefault.
    def enterImportDefault(self, ctx:JavaScriptParser.ImportDefaultContext):
        # self.insert_values(self.json_comp_dict_key, ['Import Default', 'B1'])
        # print(f'E nter Import Default: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#importDefault.
    def exitImportDefault(self, ctx:JavaScriptParser.ImportDefaultContext):
        # print(f'Exit Import Default: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#importNamespace.
    def enterImportNamespace(self, ctx:JavaScriptParser.ImportNamespaceContext):
        # self.insert_values(self.json_comp_dict_key, ['Import Namespace', 'B1'])
        # print(f'E nter Import Namespace: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#importNamespace.
    def exitImportNamespace(self, ctx:JavaScriptParser.ImportNamespaceContext):
        # print(f'Exit Import Namespace: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#importFrom.
    def enterImportFrom(self, ctx:JavaScriptParser.ImportFromContext):
        # self.insert_values(self.json_comp_dict_key, ['Import From', 'B1'])
        # print(f'E nter Import From: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#importFrom.
    def exitImportFrom(self, ctx:JavaScriptParser.ImportFromContext):
        # print(f'Exit Import From: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#aliasName.
    def enterAliasName(self, ctx:JavaScriptParser.AliasNameContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        # print(f'E nter Alias Name: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#aliasName.
    def exitAliasName(self, ctx:JavaScriptParser.AliasNameContext):
        # print(f'Exit Alias Name: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#ExportDeclaration.
    def enterExportDeclaration(self, ctx:JavaScriptParser.ExportDeclarationContext):
        # self.insert_values(self.json_comp_dict_key, ['Export Declaration', 'B1'])
        # print(f'E nter Export Declaration: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#ExportDeclaration.
    def exitExportDeclaration(self, ctx:JavaScriptParser.ExportDeclarationContext):
        # print(f'Exit Export Declaration: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#ExportDefaultDeclaration.
    def enterExportDefaultDeclaration(self, ctx:JavaScriptParser.ExportDefaultDeclarationContext):
        # self.insert_values(self.json_comp_dict_key, ['Export Default Declaration', 'B1'])
        # print(f'E nter Default Declaration: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#ExportDefaultDeclaration.
    def exitExportDefaultDeclaration(self, ctx:JavaScriptParser.ExportDefaultDeclarationContext):
        # print(f'Exit Default Declaration: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#exportFromBlock.
    def enterExportFromBlock(self, ctx:JavaScriptParser.ExportFromBlockContext):
        # self.insert_values(self.json_comp_dict_key, ['Export From Block', 'B1'])
        # print(f'E nter Export from Block: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#exportFromBlock.
    def exitExportFromBlock(self, ctx:JavaScriptParser.ExportFromBlockContext):
        # print(f'Exit Export from Block: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#declaration.
    def enterDeclaration(self, ctx:JavaScriptParser.DeclarationContext):
        # self.insert_values(self.json_comp_dict_key, ['Declaration', 'A1'])
        # print(f'E nter Declaration: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#declaration.
    def exitDeclaration(self, ctx:JavaScriptParser.DeclarationContext):
        # print(f'Exit Declaration: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#variableStatement.
    def enterVariableStatement(self, ctx:JavaScriptParser.VariableStatementContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        # print(f'E nter Variable Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#variableStatement.
    def exitVariableStatement(self, ctx:JavaScriptParser.VariableStatementContext):
        # print(f'Exit Variable Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx:JavaScriptParser.VariableDeclarationListContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        # print(f'Enter Variable Declaration List: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx:JavaScriptParser.VariableDeclarationListContext):
        # print(f'Exit Variable Declaration List: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:JavaScriptParser.VariableDeclarationContext):
        # self.insert_values(self.json_comp_dict_key, ['Variable Declaration', 'A1'])
        # print(f'Enter Variable Declaration: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:JavaScriptParser.VariableDeclarationContext):
        # print(f'Exit Variable Declaration: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#emptyStatement_.
    def enterEmptyStatement_(self, ctx:JavaScriptParser.EmptyStatement_Context):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        # print(f'Enter Empty Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#emptyStatement_.
    def exitEmptyStatement_(self, ctx:JavaScriptParser.EmptyStatement_Context):
        # print(f'Exit Empty Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#expressionStatement.
    def enterExpressionStatement(self, ctx:JavaScriptParser.ExpressionStatementContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        # print(f'Enter Expression Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#expressionStatement.
    def exitExpressionStatement(self, ctx:JavaScriptParser.ExpressionStatementContext):
        # print(f'Exit Expression Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#ifStatement.
    def enterIfStatement(self, ctx:JavaScriptParser.IfStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['If Statement', 'A1'])
        # print(f'Exit If Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#ifStatement.
    def exitIfStatement(self, ctx:JavaScriptParser.IfStatementContext):
        # print(f'Exit If Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#DoStatement.
    def enterDoStatement(self, ctx:JavaScriptParser.DoStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Do Statement', 'A1'])
        # print(f'Enter Do Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#DoStatement.
    def exitDoStatement(self, ctx:JavaScriptParser.DoStatementContext):
        # print(f'Exit Do Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#WhileStatement.
    def enterWhileStatement(self, ctx:JavaScriptParser.WhileStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['While Statement', 'A1'])
        # print(f'Enter While Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#WhileStatement.
    def exitWhileStatement(self, ctx:JavaScriptParser.WhileStatementContext):
        # print(f'Exit While Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#ForStatement.
    def enterForStatement(self, ctx:JavaScriptParser.ForStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['For Statement', 'A1'])
        # print(f'Enter For Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#ForStatement.
    def exitForStatement(self, ctx:JavaScriptParser.ForStatementContext):
        # print(f'Exit For Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#ForInStatement.
    def enterForInStatement(self, ctx:JavaScriptParser.ForInStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['For in Statement', 'A2'])
        # print(f'Enter For in Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#ForInStatement.
    def exitForInStatement(self, ctx:JavaScriptParser.ForInStatementContext):
        # print(f'Exit For in Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#ForOfStatement.
    def enterForOfStatement(self, ctx:JavaScriptParser.ForOfStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['For of Statement', 'A2'])
        # print(f'Enter For of Element: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#ForOfStatement.
    def exitForOfStatement(self, ctx:JavaScriptParser.ForOfStatementContext):
        # print(f'Exit For of Element: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#varModifier.
    def enterVarModifier(self, ctx:JavaScriptParser.VarModifierContext):
        # self.insert_values(self.json_comp_dict_key, ['Var Modifier', 'A1'])
        # print(f'Enter Var Modifier: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#varModifier.
    def exitVarModifier(self, ctx:JavaScriptParser.VarModifierContext):
        # print(f'Exit Var Modifier: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#continueStatement.
    def enterContinueStatement(self, ctx:JavaScriptParser.ContinueStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Continue Statement', 'A1'])
        # print(f'Enter Continue Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#continueStatement.
    def exitContinueStatement(self, ctx:JavaScriptParser.ContinueStatementContext):
        # print(f'Exit Continue Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#breakStatement.
    def enterBreakStatement(self, ctx:JavaScriptParser.BreakStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Break Statement', 'A1'])
        # print(f'Enter Break Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#breakStatement.
    def exitBreakStatement(self, ctx:JavaScriptParser.BreakStatementContext):
        # print(f'Exit Break Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#returnStatement.
    def enterReturnStatement(self, ctx:JavaScriptParser.ReturnStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Return Statement', 'A1'])
        # print(f'Enter Return Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#returnStatement.
    def exitReturnStatement(self, ctx:JavaScriptParser.ReturnStatementContext):
        # print(f'Exit Return Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#yieldStatement.
    def enterYieldStatement(self, ctx:JavaScriptParser.YieldStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Yield Statement', 'B1'])
        # print(f'Enter Yield Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#yieldStatement.
    def exitYieldStatement(self, ctx:JavaScriptParser.YieldStatementContext):
        # print(f'Exit Yield Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#withStatement.
    def enterWithStatement(self, ctx:JavaScriptParser.WithStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['With Statement', 'A1'])
        # print(f'Enter With Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#withStatement.
    def exitWithStatement(self, ctx:JavaScriptParser.WithStatementContext):
        # print(f'Exit With Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#switchStatement.
    def enterSwitchStatement(self, ctx:JavaScriptParser.SwitchStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Switch Statement', 'A1'])
        # print(f'Enter Switch Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#switchStatement.
    def exitSwitchStatement(self, ctx:JavaScriptParser.SwitchStatementContext):
        # print(f'Exit Switch Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#caseBlock.
    def enterCaseBlock(self, ctx:JavaScriptParser.CaseBlockContext):
        # self.insert_values(self.json_comp_dict_key, ['Case Block', 'A1'])
        # print(f'Enter Case Block: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#caseBlock.
    def exitCaseBlock(self, ctx:JavaScriptParser.CaseBlockContext):
        # print(f'Exit Case Block: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#caseClauses.
    def enterCaseClauses(self, ctx:JavaScriptParser.CaseClausesContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        # print(f'Enter Case Clauses: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#caseClauses.
    def exitCaseClauses(self, ctx:JavaScriptParser.CaseClausesContext):
        # print(f'Exit Case Clauses: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#caseClause.
    def enterCaseClause(self, ctx:JavaScriptParser.CaseClauseContext):
        # self.insert_values(self.json_comp_dict_key, ['Case Clause', 0, 0, 0, 'A1'])
        # print(f'Enter Case Clause: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#caseClause.
    def exitCaseClause(self, ctx:JavaScriptParser.CaseClauseContext):
        # print(f'Exit Case Clause: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#defaultClause.
    def enterDefaultClause(self, ctx:JavaScriptParser.DefaultClauseContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        # print(f'Enter Default Clause: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#defaultClause.
    def exitDefaultClause(self, ctx:JavaScriptParser.DefaultClauseContext):
        # print(f'Exit Default Clause: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#labelledStatement.
    def enterLabelledStatement(self, ctx:JavaScriptParser.LabelledStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Labelled Statement', 'A2'])
        # print(f'Enter Labelled Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#labelledStatement.
    def exitLabelledStatement(self, ctx:JavaScriptParser.LabelledStatementContext):
        # print(f'Exit Labelled Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#throwStatement.
    def enterThrowStatement(self, ctx:JavaScriptParser.ThrowStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Throw Statement', 'A2'])
        # print(f'Enter Throw Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#throwStatement.
    def exitThrowStatement(self, ctx:JavaScriptParser.ThrowStatementContext):
        # print(f'Exit Throw Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#tryStatement.
    def enterTryStatement(self, ctx:JavaScriptParser.TryStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Try Statement', 'A2'])
        # print(f'Enter Try Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#tryStatement.
    def exitTryStatement(self, ctx:JavaScriptParser.TryStatementContext):
        # print(f'Exit Try Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#catchProduction.
    def enterCatchProduction(self, ctx:JavaScriptParser.CatchProductionContext):
        # self.insert_values(self.json_comp_dict_key, ['Catch Production', 'A2'])
        # print(f'Enter Catch Production: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#catchProduction.
    def exitCatchProduction(self, ctx:JavaScriptParser.CatchProductionContext):
        # print(f'Exit Catch Production: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#finallyProduction.
    def enterFinallyProduction(self, ctx:JavaScriptParser.FinallyProductionContext):
        # self.insert_values(self.json_comp_dict_key, ['Finally', 'A2'])
        # print(f'Enter Finally Production: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#finallyProduction.
    def exitFinallyProduction(self, ctx:JavaScriptParser.FinallyProductionContext):
        # print(f'Exit Finally Production: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#debuggerStatement.
    def enterDebuggerStatement(self, ctx:JavaScriptParser.DebuggerStatementContext):
        # self.insert_values(self.json_comp_dict_key, ['Debugger Statement', 'A1'])
        # print(f'Enter Debugger Statement: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#debuggerStatement.
    def exitDebuggerStatement(self, ctx:JavaScriptParser.DebuggerStatementContext):
        # print(f'Exit Debugger Statement: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:JavaScriptParser.FunctionDeclarationContext):
        # self.insert_values(self.json_comp_dict_key, ['Function Declaration', 'A1'])
        # print(f'Enter Function Declaration: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:JavaScriptParser.FunctionDeclarationContext):
        # print(f'Exit Function Declaration: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaScriptParser.ClassDeclarationContext):
        # self.insert_values(self.json_comp_dict_key, ['Class Declaration', 'A2'])
        # print(f'Enter Class Declaration: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#classDeclaration.
    def exitClassDeclaration(self, ctx:JavaScriptParser.ClassDeclarationContext):
        # print(f'Exit Class Declaration: {ctx}')
        pass

    # Enter a parse tree produced by JavaScriptParser#classTail.
    def enterClassTail(self, ctx:JavaScriptParser.ClassTailContext):
        # self.insert_values(self.json_comp_dict_key, ['Class Tail', 0, 0, 0, 'A1'])
        # print(f'Enter Class Tail: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#classTail.
    def exitClassTail(self, ctx:JavaScriptParser.ClassTailContext):
        # print(f'Exit Class Tail: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#classElement.
    def enterClassElement(self, ctx:JavaScriptParser.ClassElementContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        # print(f'Enter Class Element: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#classElement.
    def exitClassElement(self, ctx:JavaScriptParser.ClassElementContext):
        # print(f'Exit Class Element: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#methodDefinition.
    def enterMethodDefinition(self, ctx:JavaScriptParser.MethodDefinitionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        # print(f'Enter Method Definition: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#methodDefinition.
    def exitMethodDefinition(self, ctx:JavaScriptParser.MethodDefinitionContext):
        # print(f'Exit Method Definition: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#formalParameterList.
    def enterFormalParameterList(self, ctx:JavaScriptParser.FormalParameterListContext):
        # self.insert_values(self.json_comp_dict_key, ['Formal Parameter List', 'A1'])
        # print(f'Enter Formal Parameter List: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#formalParameterList.
    def exitFormalParameterList(self, ctx:JavaScriptParser.FormalParameterListContext):
        # print(f'Exit Formal Parameter List: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#formalParameterArg.
    def enterFormalParameterArg(self, ctx:JavaScriptParser.FormalParameterArgContext):
        # self.insert_values(self.json_comp_dict_key, ['Formal Parameter Arg', 'A1'])
        # print(f'Enter Formal Parameter Arg: {ctx}')
        pass

    # Exit a parse tree produced by JavaScriptParser#formalParameterArg.
    def exitFormalParameterArg(self, ctx:JavaScriptParser.FormalParameterArgContext):
        # print(f'Exit Formal Parameter Arg: {ctx}')
        pass


    # Enter a parse tree produced by JavaScriptParser#lastFormalParameterArg.
    def enterLastFormalParameterArg(self, ctx:JavaScriptParser.LastFormalParameterArgContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#lastFormalParameterArg.
    def exitLastFormalParameterArg(self, ctx:JavaScriptParser.LastFormalParameterArgContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#functionBody.
    def enterFunctionBody(self, ctx:JavaScriptParser.FunctionBodyContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#functionBody.
    def exitFunctionBody(self, ctx:JavaScriptParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#sourceElements.
    def enterSourceElements(self, ctx:JavaScriptParser.SourceElementsContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#sourceElements.
    def exitSourceElements(self, ctx:JavaScriptParser.SourceElementsContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:JavaScriptParser.ArrayLiteralContext):
        # self.insert_values(self.json_comp_dict_key, ['Array', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:JavaScriptParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#elementList.
    def enterElementList(self, ctx:JavaScriptParser.ElementListContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#elementList.
    def exitElementList(self, ctx:JavaScriptParser.ElementListContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#arrayElement.
    def enterArrayElement(self, ctx:JavaScriptParser.ArrayElementContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#arrayElement.
    def exitArrayElement(self, ctx:JavaScriptParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PropertyExpressionAssignment.
    def enterPropertyExpressionAssignment(self, ctx:JavaScriptParser.PropertyExpressionAssignmentContext):
        # self.insert_values(self.json_comp_dict_key, ['Property Expression Assignment', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#PropertyExpressionAssignment.
    def exitPropertyExpressionAssignment(self, ctx:JavaScriptParser.PropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ComputedPropertyExpressionAssignment.
    def enterComputedPropertyExpressionAssignment(self, ctx:JavaScriptParser.ComputedPropertyExpressionAssignmentContext):
        # self.insert_values(self.json_comp_dict_key, ['Computed Property Expression Assignment', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#ComputedPropertyExpressionAssignment.
    def exitComputedPropertyExpressionAssignment(self, ctx:JavaScriptParser.ComputedPropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#FunctionProperty.
    def enterFunctionProperty(self, ctx:JavaScriptParser.FunctionPropertyContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#FunctionProperty.
    def exitFunctionProperty(self, ctx:JavaScriptParser.FunctionPropertyContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PropertyGetter.
    def enterPropertyGetter(self, ctx:JavaScriptParser.PropertyGetterContext):
        # self.insert_values(self.json_comp_dict_key, ['Property Getter', 'A2'])
        pass

    # Exit a parse tree produced by JavaScriptParser#PropertyGetter.
    def exitPropertyGetter(self, ctx:JavaScriptParser.PropertyGetterContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PropertySetter.
    def enterPropertySetter(self, ctx:JavaScriptParser.PropertySetterContext):
        # self.insert_values(self.json_comp_dict_key, ['Property Setter', 'A2'])
        pass

    # Exit a parse tree produced by JavaScriptParser#PropertySetter.
    def exitPropertySetter(self, ctx:JavaScriptParser.PropertySetterContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PropertyShorthand.
    def enterPropertyShorthand(self, ctx:JavaScriptParser.PropertyShorthandContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#PropertyShorthand.
    def exitPropertyShorthand(self, ctx:JavaScriptParser.PropertyShorthandContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#propertyName.
    def enterPropertyName(self, ctx:JavaScriptParser.PropertyNameContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#propertyName.
    def exitPropertyName(self, ctx:JavaScriptParser.PropertyNameContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#arguments.
    def enterArguments(self, ctx:JavaScriptParser.ArgumentsContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#arguments.
    def exitArguments(self, ctx:JavaScriptParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#argument.
    def enterArgument(self, ctx:JavaScriptParser.ArgumentContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#argument.
    def exitArgument(self, ctx:JavaScriptParser.ArgumentContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#expressionSequence.
    def enterExpressionSequence(self, ctx:JavaScriptParser.ExpressionSequenceContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#expressionSequence.
    def exitExpressionSequence(self, ctx:JavaScriptParser.ExpressionSequenceContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#TemplateStringExpression.
    def enterTemplateStringExpression(self, ctx:JavaScriptParser.TemplateStringExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Template String Expression Context', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#TemplateStringExpression.
    def exitTemplateStringExpression(self, ctx:JavaScriptParser.TemplateStringExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#TernaryExpression.
    def enterTernaryExpression(self, ctx:JavaScriptParser.TernaryExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Ternary Expression', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#TernaryExpression.
    def exitTernaryExpression(self, ctx:JavaScriptParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#LogicalAndExpression.
    def enterLogicalAndExpression(self, ctx:JavaScriptParser.LogicalAndExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Logical AND Expression', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#LogicalAndExpression.
    def exitLogicalAndExpression(self, ctx:JavaScriptParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PowerExpression.
    def enterPowerExpression(self, ctx:JavaScriptParser.PowerExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Power Expression', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#PowerExpression.
    def exitPowerExpression(self, ctx:JavaScriptParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PreIncrementExpression.
    def enterPreIncrementExpression(self, ctx:JavaScriptParser.PreIncrementExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Pre-Increment Expression', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#PreIncrementExpression.
    def exitPreIncrementExpression(self, ctx:JavaScriptParser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ObjectLiteralExpression.
    def enterObjectLiteralExpression(self, ctx:JavaScriptParser.ObjectLiteralExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Object Literal Expression', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#ObjectLiteralExpression.
    def exitObjectLiteralExpression(self, ctx:JavaScriptParser.ObjectLiteralExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#MetaExpression.
    def enterMetaExpression(self, ctx:JavaScriptParser.MetaExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Meta Expression', 'B1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#MetaExpression.
    def exitMetaExpression(self, ctx:JavaScriptParser.MetaExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#InExpression.
    def enterInExpression(self, ctx:JavaScriptParser.InExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['In Expression', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#InExpression.
    def exitInExpression(self, ctx:JavaScriptParser.InExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#LogicalOrExpression.
    def enterLogicalOrExpression(self, ctx:JavaScriptParser.LogicalOrExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Logical OR Expression', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#LogicalOrExpression.
    def exitLogicalOrExpression(self, ctx:JavaScriptParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#OptionalChainExpression.
    def enterOptionalChainExpression(self, ctx:JavaScriptParser.OptionalChainExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#OptionalChainExpression.
    def exitOptionalChainExpression(self, ctx:JavaScriptParser.OptionalChainExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#NotExpression.
    def enterNotExpression(self, ctx:JavaScriptParser.NotExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#NotExpression.
    def exitNotExpression(self, ctx:JavaScriptParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PreDecreaseExpression.
    def enterPreDecreaseExpression(self, ctx:JavaScriptParser.PreDecreaseExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#PreDecreaseExpression.
    def exitPreDecreaseExpression(self, ctx:JavaScriptParser.PreDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ArgumentsExpression.
    def enterArgumentsExpression(self, ctx:JavaScriptParser.ArgumentsExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#ArgumentsExpression.
    def exitArgumentsExpression(self, ctx:JavaScriptParser.ArgumentsExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#AwaitExpression.
    def enterAwaitExpression(self, ctx:JavaScriptParser.AwaitExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#AwaitExpression.
    def exitAwaitExpression(self, ctx:JavaScriptParser.AwaitExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ThisExpression.
    def enterThisExpression(self, ctx:JavaScriptParser.ThisExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#ThisExpression.
    def exitThisExpression(self, ctx:JavaScriptParser.ThisExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#FunctionExpression.
    def enterFunctionExpression(self, ctx:JavaScriptParser.FunctionExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#FunctionExpression.
    def exitFunctionExpression(self, ctx:JavaScriptParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:JavaScriptParser.UnaryMinusExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:JavaScriptParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:JavaScriptParser.AssignmentExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:JavaScriptParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PostDecreaseExpression.
    def enterPostDecreaseExpression(self, ctx:JavaScriptParser.PostDecreaseExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#PostDecreaseExpression.
    def exitPostDecreaseExpression(self, ctx:JavaScriptParser.PostDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#TypeofExpression.
    def enterTypeofExpression(self, ctx:JavaScriptParser.TypeofExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Typeof Expression', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#TypeofExpression.
    def exitTypeofExpression(self, ctx:JavaScriptParser.TypeofExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#InstanceofExpression.
    def enterInstanceofExpression(self, ctx:JavaScriptParser.InstanceofExpressionContext):
        # # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#InstanceofExpression.
    def exitInstanceofExpression(self, ctx:JavaScriptParser.InstanceofExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx:JavaScriptParser.UnaryPlusExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx:JavaScriptParser.UnaryPlusExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#DeleteExpression.
    def enterDeleteExpression(self, ctx:JavaScriptParser.DeleteExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#DeleteExpression.
    def exitDeleteExpression(self, ctx:JavaScriptParser.DeleteExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ImportExpression.
    def enterImportExpression(self, ctx:JavaScriptParser.ImportExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#ImportExpression.
    def exitImportExpression(self, ctx:JavaScriptParser.ImportExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#EqualityExpression.
    def enterEqualityExpression(self, ctx:JavaScriptParser.EqualityExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#EqualityExpression.
    def exitEqualityExpression(self, ctx:JavaScriptParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitXOrExpression.
    def enterBitXOrExpression(self, ctx:JavaScriptParser.BitXOrExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#BitXOrExpression.
    def exitBitXOrExpression(self, ctx:JavaScriptParser.BitXOrExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#SuperExpression.
    def enterSuperExpression(self, ctx:JavaScriptParser.SuperExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#SuperExpression.
    def exitSuperExpression(self, ctx:JavaScriptParser.SuperExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:JavaScriptParser.MultiplicativeExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:JavaScriptParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitShiftExpression.
    def enterBitShiftExpression(self, ctx:JavaScriptParser.BitShiftExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#BitShiftExpression.
    def exitBitShiftExpression(self, ctx:JavaScriptParser.BitShiftExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:JavaScriptParser.ParenthesizedExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:JavaScriptParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx:JavaScriptParser.AdditiveExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx:JavaScriptParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#RelationalExpression.
    def enterRelationalExpression(self, ctx:JavaScriptParser.RelationalExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#RelationalExpression.
    def exitRelationalExpression(self, ctx:JavaScriptParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#PostIncrementExpression.
    def enterPostIncrementExpression(self, ctx:JavaScriptParser.PostIncrementExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#PostIncrementExpression.
    def exitPostIncrementExpression(self, ctx:JavaScriptParser.PostIncrementExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#YieldExpression.
    def enterYieldExpression(self, ctx:JavaScriptParser.YieldExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#YieldExpression.
    def exitYieldExpression(self, ctx:JavaScriptParser.YieldExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitNotExpression.
    def enterBitNotExpression(self, ctx:JavaScriptParser.BitNotExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#BitNotExpression.
    def exitBitNotExpression(self, ctx:JavaScriptParser.BitNotExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#NewExpression.
    def enterNewExpression(self, ctx:JavaScriptParser.NewExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#NewExpression.
    def exitNewExpression(self, ctx:JavaScriptParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#LiteralExpression.
    def enterLiteralExpression(self, ctx:JavaScriptParser.LiteralExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#LiteralExpression.
    def exitLiteralExpression(self, ctx:JavaScriptParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ArrayLiteralExpression.
    def enterArrayLiteralExpression(self, ctx:JavaScriptParser.ArrayLiteralExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#ArrayLiteralExpression.
    def exitArrayLiteralExpression(self, ctx:JavaScriptParser.ArrayLiteralExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#MemberDotExpression.
    def enterMemberDotExpression(self, ctx:JavaScriptParser.MemberDotExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#MemberDotExpression.
    def exitMemberDotExpression(self, ctx:JavaScriptParser.MemberDotExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ClassExpression.
    def enterClassExpression(self, ctx:JavaScriptParser.ClassExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#ClassExpression.
    def exitClassExpression(self, ctx:JavaScriptParser.ClassExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#MemberIndexExpression.
    def enterMemberIndexExpression(self, ctx:JavaScriptParser.MemberIndexExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#MemberIndexExpression.
    def exitMemberIndexExpression(self, ctx:JavaScriptParser.MemberIndexExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx:JavaScriptParser.IdentifierExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx:JavaScriptParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitAndExpression.
    def enterBitAndExpression(self, ctx:JavaScriptParser.BitAndExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#BitAndExpression.
    def exitBitAndExpression(self, ctx:JavaScriptParser.BitAndExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#BitOrExpression.
    def enterBitOrExpression(self, ctx:JavaScriptParser.BitOrExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#BitOrExpression.
    def exitBitOrExpression(self, ctx:JavaScriptParser.BitOrExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#AssignmentOperatorExpression.
    def enterAssignmentOperatorExpression(self, ctx:JavaScriptParser.AssignmentOperatorExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['Assignment Operator Expression', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#AssignmentOperatorExpression.
    def exitAssignmentOperatorExpression(self, ctx:JavaScriptParser.AssignmentOperatorExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#VoidExpression.
    def enterVoidExpression(self, ctx:JavaScriptParser.VoidExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#VoidExpression.
    def exitVoidExpression(self, ctx:JavaScriptParser.VoidExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#CoalesceExpression.
    def enterCoalesceExpression(self, ctx:JavaScriptParser.CoalesceExpressionContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#CoalesceExpression.
    def exitCoalesceExpression(self, ctx:JavaScriptParser.CoalesceExpressionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#assignable.
    def enterAssignable(self, ctx:JavaScriptParser.AssignableContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#assignable.
    def exitAssignable(self, ctx:JavaScriptParser.AssignableContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#objectLiteral.
    def enterObjectLiteral(self, ctx:JavaScriptParser.ObjectLiteralContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#objectLiteral.
    def exitObjectLiteral(self, ctx:JavaScriptParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#FunctionDecl.
    def enterFunctionDecl(self, ctx:JavaScriptParser.FunctionDeclContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#FunctionDecl.
    def exitFunctionDecl(self, ctx:JavaScriptParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#AnonymousFunctionDecl.
    def enterAnonymousFunctionDecl(self, ctx:JavaScriptParser.AnonymousFunctionDeclContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#AnonymousFunctionDecl.
    def exitAnonymousFunctionDecl(self, ctx:JavaScriptParser.AnonymousFunctionDeclContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#ArrowFunction.
    def enterArrowFunction(self, ctx:JavaScriptParser.ArrowFunctionContext):
        # self.insert_values(self.json_comp_dict_key, ['Arrow Function', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#ArrowFunction.
    def exitArrowFunction(self, ctx:JavaScriptParser.ArrowFunctionContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#arrowFunctionParameters.
    def enterArrowFunctionParameters(self, ctx:JavaScriptParser.ArrowFunctionParametersContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#arrowFunctionParameters.
    def exitArrowFunctionParameters(self, ctx:JavaScriptParser.ArrowFunctionParametersContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#arrowFunctionBody.
    def enterArrowFunctionBody(self, ctx:JavaScriptParser.ArrowFunctionBodyContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#arrowFunctionBody.
    def exitArrowFunctionBody(self, ctx:JavaScriptParser.ArrowFunctionBodyContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:JavaScriptParser.AssignmentOperatorContext):
        # self.insert_values(self.json_comp_dict_key, ['Assignment Operator', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:JavaScriptParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#literal.
    def enterLiteral(self, ctx:JavaScriptParser.LiteralContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#literal.
    def exitLiteral(self, ctx:JavaScriptParser.LiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#templateStringLiteral.
    def enterTemplateStringLiteral(self, ctx:JavaScriptParser.TemplateStringLiteralContext):
        # self.insert_values(self.json_comp_dict_key, ['', 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#templateStringLiteral.
    def exitTemplateStringLiteral(self, ctx:JavaScriptParser.TemplateStringLiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#templateStringAtom.
    def enterTemplateStringAtom(self, ctx:JavaScriptParser.TemplateStringAtomContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#templateStringAtom.
    def exitTemplateStringAtom(self, ctx:JavaScriptParser.TemplateStringAtomContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#numericLiteral.
    def enterNumericLiteral(self, ctx:JavaScriptParser.NumericLiteralContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#numericLiteral.
    def exitNumericLiteral(self, ctx:JavaScriptParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#bigintLiteral.
    def enterBigintLiteral(self, ctx:JavaScriptParser.BigintLiteralContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#bigintLiteral.
    def exitBigintLiteral(self, ctx:JavaScriptParser.BigintLiteralContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#getter.
    def enterGetter(self, ctx:JavaScriptParser.GetterContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#getter.
    def exitGetter(self, ctx:JavaScriptParser.GetterContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#setter.
    def enterSetter(self, ctx:JavaScriptParser.SetterContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#setter.
    def exitSetter(self, ctx:JavaScriptParser.SetterContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#identifierName.
    def enterIdentifierName(self, ctx:JavaScriptParser.IdentifierNameContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#identifierName.
    def exitIdentifierName(self, ctx:JavaScriptParser.IdentifierNameContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#identifier.
    def enterIdentifier(self, ctx:JavaScriptParser.IdentifierContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#identifier.
    def exitIdentifier(self, ctx:JavaScriptParser.IdentifierContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#reservedWord.
    def enterReservedWord(self, ctx:JavaScriptParser.ReservedWordContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#reservedWord.
    def exitReservedWord(self, ctx:JavaScriptParser.ReservedWordContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#keyword.
    def enterKeyword(self, ctx:JavaScriptParser.KeywordContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#keyword.
    def exitKeyword(self, ctx:JavaScriptParser.KeywordContext):
        pass


    # Enter a parse tree produced by JavaScriptParser#let_.
    def enterLet_(self, ctx:JavaScriptParser.Let_Context):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#let_.
    def exitLet_(self, ctx:JavaScriptParser.Let_Context):
        pass


    # Enter a parse tree produced by JavaScriptParser#eos.
    def enterEos(self, ctx:JavaScriptParser.EosContext):
        # self.insert_values(self.json_comp_dict_key, ['wait', 0, 0, 0, 'A1'])
        pass

    # Exit a parse tree produced by JavaScriptParser#eos.
    def exitEos(self, ctx:JavaScriptParser.EosContext):
        pass



del JavaScriptParser