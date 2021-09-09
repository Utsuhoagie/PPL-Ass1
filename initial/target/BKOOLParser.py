# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\48\n\4\3\5\3\5\3\5\3\5\5\5>\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6N\n\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7V\n\7\3\b\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\3")
        buf.write("\6\2\7\7\16\16\20\20\22\22\2a\2\26\3\2\2\2\4\35\3\2\2")
        buf.write("\2\6\67\3\2\2\2\b=\3\2\2\2\nM\3\2\2\2\fU\3\2\2\2\16W\3")
        buf.write("\2\2\2\20Z\3\2\2\2\22\\\3\2\2\2\24^\3\2\2\2\26\27\5\4")
        buf.write("\3\2\27\30\7\2\2\3\30\3\3\2\2\2\31\32\5\6\4\2\32\33\5")
        buf.write("\4\3\2\33\36\3\2\2\2\34\36\5\6\4\2\35\31\3\2\2\2\35\34")
        buf.write("\3\2\2\2\36\5\3\2\2\2\37 \7\t\2\2 !\7\6\2\2!\"\7\r\2\2")
        buf.write("\"#\7\6\2\2#$\7\62\2\2$%\5\b\5\2%&\7\63\2\2&8\3\2\2\2")
        buf.write("\'(\7\t\2\2()\7\6\2\2)*\7\62\2\2*+\5\b\5\2+,\7\63\2\2")
        buf.write(",8\3\2\2\2-.\7\t\2\2./\7\6\2\2/\60\7\r\2\2\60\61\7\6\2")
        buf.write("\2\61\62\7\62\2\2\628\7\63\2\2\63\64\7\t\2\2\64\65\7\6")
        buf.write("\2\2\65\66\7\62\2\2\668\7\63\2\2\67\37\3\2\2\2\67\'\3")
        buf.write("\2\2\2\67-\3\2\2\2\67\63\3\2\2\28\7\3\2\2\29:\5\n\6\2")
        buf.write(":;\5\b\5\2;>\3\2\2\2<>\5\n\6\2=9\3\2\2\2=<\3\2\2\2>\t")
        buf.write("\3\2\2\2?@\5\f\7\2@A\5\16\b\2AB\7\66\2\2BN\3\2\2\2CD\5")
        buf.write("\16\b\2DE\7\66\2\2EN\3\2\2\2FG\7\34\2\2GH\5\24\13\2HI")
        buf.write("\7\66\2\2IN\3\2\2\2JK\5\24\13\2KL\7\66\2\2LN\3\2\2\2M")
        buf.write("?\3\2\2\2MC\3\2\2\2MF\3\2\2\2MJ\3\2\2\2N\13\3\2\2\2OP")
        buf.write("\7\34\2\2PV\7\33\2\2QR\7\33\2\2RV\7\34\2\2SV\7\34\2\2")
        buf.write("TV\7\33\2\2UO\3\2\2\2UQ\3\2\2\2US\3\2\2\2UT\3\2\2\2V\r")
        buf.write("\3\2\2\2WX\5\20\t\2XY\5\22\n\2Y\17\3\2\2\2Z[\t\2\2\2[")
        buf.write("\21\3\2\2\2\\]\7\17\2\2]\23\3\2\2\2^_\7%\2\2_\25\3\2\2")
        buf.write("\2\7\35\67=MU")
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
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classDeclList = 1
    RULE_classDecl = 2
    RULE_memberList = 3
    RULE_member = 4
    RULE_keyword = 5
    RULE_attribute = 6
    RULE_attrType = 7
    RULE_attrNameList = 8
    RULE_method = 9

    ruleNames =  [ "program", "classDeclList", "classDecl", "memberList", 
                   "member", "keyword", "attribute", "attrType", "attrNameList", 
                   "method" ]

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

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclListContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.classDeclList()
            self.state = 21
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclContext,0)


        def classDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclList" ):
                return visitor.visitClassDeclList(self)
            else:
                return visitor.visitChildren(self)




    def classDeclList(self):

        localctx = BKOOLParser.ClassDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclList)
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.classDecl()
                self.state = 24
                self.classDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.classDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def memberList(self):
            return self.getTypedRuleContext(BKOOLParser.MemberListContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(BKOOLParser.CLASS)
                self.state = 30
                self.match(BKOOLParser.ID)
                self.state = 31
                self.match(BKOOLParser.EXTENDS)
                self.state = 32
                self.match(BKOOLParser.ID)
                self.state = 33
                self.match(BKOOLParser.LB)
                self.state = 34
                self.memberList()
                self.state = 35
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(BKOOLParser.CLASS)
                self.state = 38
                self.match(BKOOLParser.ID)
                self.state = 39
                self.match(BKOOLParser.LB)
                self.state = 40
                self.memberList()
                self.state = 41
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(BKOOLParser.CLASS)
                self.state = 44
                self.match(BKOOLParser.ID)
                self.state = 45
                self.match(BKOOLParser.EXTENDS)
                self.state = 46
                self.match(BKOOLParser.ID)
                self.state = 47
                self.match(BKOOLParser.LB)
                self.state = 48
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.match(BKOOLParser.CLASS)
                self.state = 50
                self.match(BKOOLParser.ID)
                self.state = 51
                self.match(BKOOLParser.LB)
                self.state = 52
                self.match(BKOOLParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def memberList(self):
            return self.getTypedRuleContext(BKOOLParser.MemberListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memberList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberList" ):
                return visitor.visitMemberList(self)
            else:
                return visitor.visitChildren(self)




    def memberList(self):

        localctx = BKOOLParser.MemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memberList)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.member()
                self.state = 56
                self.memberList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.member()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(BKOOLParser.KeywordContext,0)


        def attribute(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def method(self):
            return self.getTypedRuleContext(BKOOLParser.MethodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.keyword()
                self.state = 62
                self.attribute()
                self.state = 63
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.attribute()
                self.state = 66
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(BKOOLParser.STATIC)
                self.state = 69
                self.method()
                self.state = 70
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.method()
                self.state = 73
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_keyword

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword" ):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)




    def keyword(self):

        localctx = BKOOLParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_keyword)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(BKOOLParser.STATIC)
                self.state = 78
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(BKOOLParser.FINAL)
                self.state = 80
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.match(BKOOLParser.FINAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrType(self):
            return self.getTypedRuleContext(BKOOLParser.AttrTypeContext,0)


        def attrNameList(self):
            return self.getTypedRuleContext(BKOOLParser.AttrNameListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.attrType()
            self.state = 86
            self.attrNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attrType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrType" ):
                return visitor.visitAttrType(self)
            else:
                return visitor.visitChildren(self)




    def attrType(self):

        localctx = BKOOLParser.AttrTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrNameListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attrNameList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrNameList" ):
                return visitor.visitAttrNameList(self)
            else:
                return visitor.visitChildren(self)




    def attrNameList(self):

        localctx = BKOOLParser.AttrNameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attrNameList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(BKOOLParser.IF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = BKOOLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(BKOOLParser.NEQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





