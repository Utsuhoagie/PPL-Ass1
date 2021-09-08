# Generated from e:\Study\Sem7\PPL\Assignment\A1\Third Test A1, changing ANTLR\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'''", "'/'", "'%'", "'!='", "'=='", "'<'", "'>'", 
                     "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", 
                     "'{'", "'}'", "'('", "')'", "'['", "']'", "';'", "':'", 
                     "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "WS", "BLOCK_CMT", "LINE_CMT", "ID", 
                      "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                      "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
                      "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
                      "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "ADD", "SUB", "MUL", "DIV", "DIVF", "MOD", "NEQ", 
                      "EQ", "LESS", "GREATER", "LEQ", "GREQ", "OR", "AND", 
                      "NOT", "CONCAT", "ASSIGN", "LP", "RP", "LB", "RB", 
                      "LQ", "RQ", "SEMI", "COLON", "DOT", "COMMA", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "STRINGLIT", "ARRAYLIT", "LITLIST", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    WS=1
    BLOCK_CMT=2
    LINE_CMT=3
    ID=4
    BOOLEAN=5
    BREAK=6
    CLASS=7
    CONTINUE=8
    DO=9
    ELSE=10
    EXTENDS=11
    FLOAT=12
    IF=13
    INT=14
    NEW=15
    STRING=16
    THEN=17
    FOR=18
    RETURN=19
    TRUE=20
    FALSE=21
    VOID=22
    NIL=23
    THIS=24
    FINAL=25
    STATIC=26
    TO=27
    DOWNTO=28
    ADD=29
    SUB=30
    MUL=31
    DIV=32
    DIVF=33
    MOD=34
    NEQ=35
    EQ=36
    LESS=37
    GREATER=38
    LEQ=39
    GREQ=40
    OR=41
    AND=42
    NOT=43
    CONCAT=44
    ASSIGN=45
    LP=46
    RP=47
    LB=48
    RB=49
    LQ=50
    RQ=51
    SEMI=52
    COLON=53
    DOT=54
    COMMA=55
    INTLIT=56
    FLOATLIT=57
    BOOLLIT=58
    STRINGLIT=59
    ARRAYLIT=60
    LITLIST=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    UNTERMINATED_COMMENT=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





