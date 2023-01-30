import os, json, csv
from antlr4 import *
from antlr4.tree.Tree import ParseTree
from .JscefrParser import JscefrParser

class JscefrWalker(ParseTreeWalker):

    compositions = []

    def __init__(self):
        self.data = self.read_dict()

    def read_dict(self):
        f = open(os.getcwd() + '/dictionary_converter/dict.json')
        data = json.load(f)
        return data

    def walk(self, listener:ParseTreeListener, t:ParseTree, layer, repo, filename):
        """
	    Performs a walk on the given parse tree starting at the root and going down recursively
	    with depth-first search. On each node, {@link ParseTreeWalker#enterRule} is called before
	    recursively walking down into child nodes, then
	    {@link ParseTreeWalker#exitRule} is called after the recursive call to wind up.
	    @param listener The listener used by the walker to process grammar rules
	    @param t The parse tree to be walked on
        """
        if isinstance(t, ErrorNode):
            listener.visitErrorNode(t)
            return
        elif isinstance(t, TerminalNode):
            listener.visitTerminal(t)
            return
        self.enterRule(listener, t, layer, repo, filename)
        for child in t.getChildren():
            self.walk(listener, child, layer + 1, repo, filename)
        self.exitRule(listener, t)
    
    def enterRule(self, listener:ParseTreeListener, r:RuleNode, layer, repo, filename):
        """
	    Enters a grammar rule by first triggering the generic event {@link ParseTreeListener#enterEveryRule}
	    then by triggering the event specific to the given parse tree node
	    @param listener The listener responding to the trigger events
	    @param r The grammar rule containing the rule context
        """
        ctx = r.getRuleContext()
        listener.enterEveryRule(ctx)
        ctx.enterRule(listener)

        # self.display_construct(layer, ctx)

        for match in self.data:
            name = match['Class']
            if JscefrParser.ruleNames[ctx.getRuleIndex()].lower() == name.lower() or JscefrParser.isSpecialRule(ctx, match, name):
                with open(os.getcwd() + '/report_generators/data.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow([repo, filename] + list(match.values()) + [ctx.start.line, ctx.start.column, ctx.stop.line, ctx.stop.column])
    
    def exitRule(self, listener:ParseTreeListener, r:RuleNode):
        """
	    Exits a grammar rule by first triggering the event specific to the given parse tree node
	    then by triggering the generic event {@link ParseTreeListener#exitEveryRule}
	    @param listener The listener responding to the trigger events
	    @param r The grammar rule containing the rule context
        """
        ctx = r.getRuleContext()
        ctx.exitRule(listener)
        listener.exitEveryRule(ctx)
    
    def display_construct(self, layer, ctx):
        print(f'Layer {layer}: {JscefrParser.ruleNames[ctx.getRuleIndex()]}')
        # print(f'Layer {layer}: {ctx.__class__.__name__.replace("Context", "")}')
        print(f'\t starts at line {ctx.start.line}, column {ctx.start.column}')
        print(f'\t stops at line {ctx.stop.line}, column {ctx.stop.column}')
        print(f'\t start text: {ctx.start.text}, stop text: {ctx.stop.text}')
        print(f'\t children: {[child.__class__.__name__.replace("Context", "") for child in ctx.children]}')