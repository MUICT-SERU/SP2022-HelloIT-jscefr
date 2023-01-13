import os, json
from antlr4 import *
from antlr4.tree.Tree import ParseTree
from .JavaScriptParserListener import JavaScriptParserListener
from .JscefrParser import JscefrParser
# from .JavaScriptParser import JavaScriptParser

class JscefrWalker(ParseTreeWalker):

    compositions = []

    def __init__(self):
        self.data = self.read_dict()

    def read_dict(self):
        f = open(os.getcwd() + '/dictionary_converter/dict.json')
        data = json.load(f)
        return data

    def walk(self, listener:JavaScriptParserListener, t:ParseTree, layer):
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
        self.enterRule(listener, t, layer)
        for child in t.getChildren():
            self.walk(listener, child, layer + 1)
        self.exitRule(listener, t)
    
    def enterRule(self, listener:JavaScriptParserListener, r:RuleNode, layer):
        """
	    Enters a grammar rule by first triggering the generic event {@link ParseTreeListener#enterEveryRule}
	    then by triggering the event specific to the given parse tree node
	    @param listener The listener responding to the trigger events
	    @param r The grammar rule containing the rule context
        """
        ctx = r.getRuleContext()
        listener.enterEveryRule(ctx)
        ctx.enterRule(listener)

        # code_construct = JavaScriptParser.ruleNames[ctx.getRuleIndex()]
        # code_construct = JscefrParser.ruleNames[ctx.getRuleIndex()]

        try:
            code_construct = JscefrParser.ruleNames[ctx.getRuleIndex()]
        except:
            code_construct = None
        
        # listener.add_to_traverse_result([layer, code_construct, ctx.start.line, ctx.start.column, ctx.stop.line, ctx.stop.column, ctx.start.text, ctx.stop.text, [JscefrParser.ruleNames[child.getRuleIndex()] for child in (ctx.children or []) if (child.__class__.__name__ != 'TerminalNodeImpl') and (child.__class__.__name__ != 'ErrorNodeImpl')], ctx.__class__.__name__])

        for match in self.data:
            name = match['Class']
            if JscefrParser.ruleNames[ctx.getRuleIndex()].lower() == name.lower() or JscefrParser.isSpecialRule(ctx, match, match['Class'], listener):
                listener.insert_values(list(match.values()))
    
    def exitRule(self, listener:JavaScriptParserListener, r:RuleNode):
        """
	    Exits a grammar rule by first triggering the event specific to the given parse tree node
	    then by triggering the generic event {@link ParseTreeListener#exitEveryRule}
	    @param listener The listener responding to the trigger events
	    @param r The grammar rule containing the rule context
        """
        ctx = r.getRuleContext()
        ctx.exitRule(listener)
        listener.exitEveryRule(ctx)