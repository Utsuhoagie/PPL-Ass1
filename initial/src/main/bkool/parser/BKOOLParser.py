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
        buf.write("\u0197\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3L\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4U\n\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4]\n\4\3\4\5\4`\n\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5f\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6o\n\6\3\6")
        buf.write("\3\6\3\6\5\6t\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7}\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0085\n\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u0091\n\n\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u0097\n\13\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u009f")
        buf.write("\n\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u00a9\n")
        buf.write("\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00b2\n\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c7\n")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00d1")
        buf.write("\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00eb\n\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\7\21\u00f6\n\21\f\21\16\21\u00f9")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\5\22\u0100\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u0107\n\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u010f\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u0119\n\25\3\26\3\26\3\26\5\26\u011e")
        buf.write("\n\26\3\26\3\26\3\27\3\27\5\27\u0124\n\27\3\27\3\27\5")
        buf.write("\27\u0128\n\27\3\30\3\30\3\30\3\30\5\30\u012e\n\30\3\31")
        buf.write("\3\31\5\31\u0132\n\31\3\31\3\31\3\31\3\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u014a\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0158\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0170\n\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3!\3!\5!\u017e\n!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\5\"\u0186\n\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u0191\n\"\3\"\3\"\5\"\u0195\n\"\3\"\2\3 #\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@B\2\n\7\2\13\13\22\22\24\24\26\26##\7\2\13\13\22\22")
        buf.write("\24\24\26\26\34\34\3\2$%\3\2&)\3\2\60\61\3\2*+\3\2,/\3")
        buf.write("\2!\"\2\u01bb\2D\3\2\2\2\4K\3\2\2\2\6_\3\2\2\2\be\3\2")
        buf.write("\2\2\ns\3\2\2\2\f|\3\2\2\2\16\u0084\3\2\2\2\20\u0086\3")
        buf.write("\2\2\2\22\u0090\3\2\2\2\24\u0096\3\2\2\2\26\u0098\3\2")
        buf.write("\2\2\30\u009a\3\2\2\2\32\u00a8\3\2\2\2\34\u00aa\3\2\2")
        buf.write("\2\36\u00b1\3\2\2\2 \u00d0\3\2\2\2\"\u00ff\3\2\2\2$\u0101")
        buf.write("\3\2\2\2&\u010e\3\2\2\2(\u0118\3\2\2\2*\u011a\3\2\2\2")
        buf.write(",\u0123\3\2\2\2.\u012d\3\2\2\2\60\u0131\3\2\2\2\62\u0137")
        buf.write("\3\2\2\2\64\u0149\3\2\2\2\66\u0157\3\2\2\28\u0159\3\2")
        buf.write("\2\2:\u016f\3\2\2\2<\u0171\3\2\2\2>\u0174\3\2\2\2@\u017d")
        buf.write("\3\2\2\2B\u0194\3\2\2\2DE\5\4\3\2EF\7\2\2\3F\3\3\2\2\2")
        buf.write("GH\5\6\4\2HI\5\4\3\2IL\3\2\2\2JL\5\6\4\2KG\3\2\2\2KJ\3")
        buf.write("\2\2\2L\5\3\2\2\2MN\7\r\2\2NO\7#\2\2OP\7\21\2\2PQ\7#\2")
        buf.write("\2QT\7\66\2\2RU\5\b\5\2SU\3\2\2\2TR\3\2\2\2TS\3\2\2\2")
        buf.write("UV\3\2\2\2V`\7\67\2\2WX\7\r\2\2XY\7#\2\2Y\\\7\66\2\2Z")
        buf.write("]\5\b\5\2[]\3\2\2\2\\Z\3\2\2\2\\[\3\2\2\2]^\3\2\2\2^`")
        buf.write("\7\67\2\2_M\3\2\2\2_W\3\2\2\2`\7\3\2\2\2ab\5\n\6\2bc\5")
        buf.write("\b\5\2cf\3\2\2\2df\5\n\6\2ea\3\2\2\2ed\3\2\2\2f\t\3\2")
        buf.write("\2\2gh\5\f\7\2hi\5\16\b\2ij\5\22\n\2jk\7<\2\2kt\3\2\2")
        buf.write("\2lo\7 \2\2mo\3\2\2\2nl\3\2\2\2nm\3\2\2\2op\3\2\2\2pq")
        buf.write("\5\26\f\2qr\5\30\r\2rt\3\2\2\2sg\3\2\2\2sn\3\2\2\2t\13")
        buf.write("\3\2\2\2uv\7 \2\2v}\7\37\2\2wx\7\37\2\2x}\7 \2\2y}\7 ")
        buf.write("\2\2z}\7\37\2\2{}\3\2\2\2|u\3\2\2\2|w\3\2\2\2|y\3\2\2")
        buf.write("\2|z\3\2\2\2|{\3\2\2\2}\r\3\2\2\2~\u0085\7\24\2\2\177")
        buf.write("\u0085\7\22\2\2\u0080\u0085\7\13\2\2\u0081\u0085\7\26")
        buf.write("\2\2\u0082\u0085\7#\2\2\u0083\u0085\5\20\t\2\u0084~\3")
        buf.write("\2\2\2\u0084\177\3\2\2\2\u0084\u0080\3\2\2\2\u0084\u0081")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085")
        buf.write("\17\3\2\2\2\u0086\u0087\t\2\2\2\u0087\u0088\7:\2\2\u0088")
        buf.write("\u0089\7\6\2\2\u0089\u008a\7;\2\2\u008a\21\3\2\2\2\u008b")
        buf.write("\u008c\5\24\13\2\u008c\u008d\7?\2\2\u008d\u008e\5\22\n")
        buf.write("\2\u008e\u0091\3\2\2\2\u008f\u0091\5\24\13\2\u0090\u008b")
        buf.write("\3\2\2\2\u0090\u008f\3\2\2\2\u0091\23\3\2\2\2\u0092\u0093")
        buf.write("\7#\2\2\u0093\u0094\7\65\2\2\u0094\u0097\5 \21\2\u0095")
        buf.write("\u0097\7#\2\2\u0096\u0092\3\2\2\2\u0096\u0095\3\2\2\2")
        buf.write("\u0097\25\3\2\2\2\u0098\u0099\t\3\2\2\u0099\27\3\2\2\2")
        buf.write("\u009a\u009b\7#\2\2\u009b\u009e\78\2\2\u009c\u009f\5\32")
        buf.write("\16\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\79\2\2\u00a1")
        buf.write("\u00a2\5*\26\2\u00a2\31\3\2\2\2\u00a3\u00a4\5\34\17\2")
        buf.write("\u00a4\u00a5\7<\2\2\u00a5\u00a6\5\32\16\2\u00a6\u00a9")
        buf.write("\3\2\2\2\u00a7\u00a9\5\34\17\2\u00a8\u00a3\3\2\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a9\33\3\2\2\2\u00aa\u00ab\5\16\b\2\u00ab")
        buf.write("\u00ac\5\36\20\2\u00ac\35\3\2\2\2\u00ad\u00ae\7#\2\2\u00ae")
        buf.write("\u00af\7?\2\2\u00af\u00b2\5\36\20\2\u00b0\u00b2\7#\2\2")
        buf.write("\u00b1\u00ad\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\37\3\2")
        buf.write("\2\2\u00b3\u00b4\b\21\1\2\u00b4\u00b5\78\2\2\u00b5\u00b6")
        buf.write("\5 \21\2\u00b6\u00b7\79\2\2\u00b7\u00d1\3\2\2\2\u00b8")
        buf.write("\u00d1\7\6\2\2\u00b9\u00d1\7\7\2\2\u00ba\u00d1\7\b\2\2")
        buf.write("\u00bb\u00d1\7\t\2\2\u00bc\u00d1\7\n\2\2\u00bd\u00d1\7")
        buf.write("\36\2\2\u00be\u00d1\7#\2\2\u00bf\u00d1\5$\23\2\u00c0\u00c1")
        buf.write("\7#\2\2\u00c1\u00c2\7>\2\2\u00c2\u00c3\7#\2\2\u00c3\u00c6")
        buf.write("\78\2\2\u00c4\u00c7\5\"\22\2\u00c5\u00c7\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00d1\79\2\2\u00c9\u00ca\7#\2\2\u00ca\u00cb\7>")
        buf.write("\2\2\u00cb\u00d1\7#\2\2\u00cc\u00cd\t\4\2\2\u00cd\u00d1")
        buf.write("\5 \21\n\u00ce\u00cf\7\62\2\2\u00cf\u00d1\5 \21\t\u00d0")
        buf.write("\u00b3\3\2\2\2\u00d0\u00b8\3\2\2\2\u00d0\u00b9\3\2\2\2")
        buf.write("\u00d0\u00ba\3\2\2\2\u00d0\u00bb\3\2\2\2\u00d0\u00bc\3")
        buf.write("\2\2\2\u00d0\u00bd\3\2\2\2\u00d0\u00be\3\2\2\2\u00d0\u00bf")
        buf.write("\3\2\2\2\u00d0\u00c0\3\2\2\2\u00d0\u00c9\3\2\2\2\u00d0")
        buf.write("\u00cc\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00f7\3\2\2\2")
        buf.write("\u00d2\u00d3\f\b\2\2\u00d3\u00d4\7\63\2\2\u00d4\u00f6")
        buf.write("\5 \21\t\u00d5\u00d6\f\7\2\2\u00d6\u00d7\t\5\2\2\u00d7")
        buf.write("\u00f6\5 \21\b\u00d8\u00d9\f\6\2\2\u00d9\u00da\t\4\2\2")
        buf.write("\u00da\u00f6\5 \21\7\u00db\u00dc\f\5\2\2\u00dc\u00dd\t")
        buf.write("\6\2\2\u00dd\u00f6\5 \21\6\u00de\u00df\f\4\2\2\u00df\u00e0")
        buf.write("\t\7\2\2\u00e0\u00f6\5 \21\5\u00e1\u00e2\f\3\2\2\u00e2")
        buf.write("\u00e3\t\b\2\2\u00e3\u00f6\5 \21\4\u00e4\u00e5\f\17\2")
        buf.write("\2\u00e5\u00e6\7>\2\2\u00e6\u00e7\7#\2\2\u00e7\u00ea\7")
        buf.write("8\2\2\u00e8\u00eb\5\"\22\2\u00e9\u00eb\3\2\2\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00f6\79\2\2\u00ed\u00ee\f\r\2\2\u00ee\u00ef\7>\2\2\u00ef")
        buf.write("\u00f6\7#\2\2\u00f0\u00f1\f\13\2\2\u00f1\u00f2\7:\2\2")
        buf.write("\u00f2\u00f3\5 \21\2\u00f3\u00f4\7;\2\2\u00f4\u00f6\3")
        buf.write("\2\2\2\u00f5\u00d2\3\2\2\2\u00f5\u00d5\3\2\2\2\u00f5\u00d8")
        buf.write("\3\2\2\2\u00f5\u00db\3\2\2\2\u00f5\u00de\3\2\2\2\u00f5")
        buf.write("\u00e1\3\2\2\2\u00f5\u00e4\3\2\2\2\u00f5\u00ed\3\2\2\2")
        buf.write("\u00f5\u00f0\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3")
        buf.write("\2\2\2\u00f7\u00f8\3\2\2\2\u00f8!\3\2\2\2\u00f9\u00f7")
        buf.write("\3\2\2\2\u00fa\u00fb\5 \21\2\u00fb\u00fc\7?\2\2\u00fc")
        buf.write("\u00fd\5\"\22\2\u00fd\u0100\3\2\2\2\u00fe\u0100\5 \21")
        buf.write("\2\u00ff\u00fa\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100#\3\2")
        buf.write("\2\2\u0101\u0102\7\25\2\2\u0102\u0103\7#\2\2\u0103\u0106")
        buf.write("\78\2\2\u0104\u0107\5\"\22\2\u0105\u0107\3\2\2\2\u0106")
        buf.write("\u0104\3\2\2\2\u0106\u0105\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u0109\79\2\2\u0109%\3\2\2\2\u010a\u010b\5(\25\2")
        buf.write("\u010b\u010c\5&\24\2\u010c\u010f\3\2\2\2\u010d\u010f\5")
        buf.write("(\25\2\u010e\u010a\3\2\2\2\u010e\u010d\3\2\2\2\u010f\'")
        buf.write("\3\2\2\2\u0110\u0119\5*\26\2\u0111\u0119\5\62\32\2\u0112")
        buf.write("\u0119\5\66\34\2\u0113\u0119\58\35\2\u0114\u0119\5<\37")
        buf.write("\2\u0115\u0119\5> \2\u0116\u0119\5@!\2\u0117\u0119\5B")
        buf.write("\"\2\u0118\u0110\3\2\2\2\u0118\u0111\3\2\2\2\u0118\u0112")
        buf.write("\3\2\2\2\u0118\u0113\3\2\2\2\u0118\u0114\3\2\2\2\u0118")
        buf.write("\u0115\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2")
        buf.write("\u0119)\3\2\2\2\u011a\u011d\7\66\2\2\u011b\u011e\5,\27")
        buf.write("\2\u011c\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011c")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\7\67\2\2\u0120")
        buf.write("+\3\2\2\2\u0121\u0124\5.\30\2\u0122\u0124\3\2\2\2\u0123")
        buf.write("\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2\2")
        buf.write("\u0125\u0128\5&\24\2\u0126\u0128\3\2\2\2\u0127\u0125\3")
        buf.write("\2\2\2\u0127\u0126\3\2\2\2\u0128-\3\2\2\2\u0129\u012a")
        buf.write("\5\60\31\2\u012a\u012b\5.\30\2\u012b\u012e\3\2\2\2\u012c")
        buf.write("\u012e\5\60\31\2\u012d\u0129\3\2\2\2\u012d\u012c\3\2\2")
        buf.write("\2\u012e/\3\2\2\2\u012f\u0132\7\37\2\2\u0130\u0132\3\2")
        buf.write("\2\2\u0131\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133\u0134\5\16\b\2\u0134\u0135\5\22\n\2\u0135")
        buf.write("\u0136\7<\2\2\u0136\61\3\2\2\2\u0137\u0138\5\64\33\2\u0138")
        buf.write("\u0139\7\64\2\2\u0139\u013a\5 \21\2\u013a\u013b\7<\2\2")
        buf.write("\u013b\63\3\2\2\2\u013c\u014a\7#\2\2\u013d\u013e\5 \21")
        buf.write("\2\u013e\u013f\7>\2\2\u013f\u0140\7#\2\2\u0140\u014a\3")
        buf.write("\2\2\2\u0141\u0142\7#\2\2\u0142\u0143\7>\2\2\u0143\u014a")
        buf.write("\7#\2\2\u0144\u0145\5 \21\2\u0145\u0146\7:\2\2\u0146\u0147")
        buf.write("\5 \21\2\u0147\u0148\7;\2\2\u0148\u014a\3\2\2\2\u0149")
        buf.write("\u013c\3\2\2\2\u0149\u013d\3\2\2\2\u0149\u0141\3\2\2\2")
        buf.write("\u0149\u0144\3\2\2\2\u014a\65\3\2\2\2\u014b\u014c\7\23")
        buf.write("\2\2\u014c\u014d\5 \21\2\u014d\u014e\7\27\2\2\u014e\u014f")
        buf.write("\5(\25\2\u014f\u0150\7\20\2\2\u0150\u0151\5(\25\2\u0151")
        buf.write("\u0158\3\2\2\2\u0152\u0153\7\23\2\2\u0153\u0154\5 \21")
        buf.write("\2\u0154\u0155\7\27\2\2\u0155\u0156\5(\25\2\u0156\u0158")
        buf.write("\3\2\2\2\u0157\u014b\3\2\2\2\u0157\u0152\3\2\2\2\u0158")
        buf.write("\67\3\2\2\2\u0159\u015a\7\30\2\2\u015a\u015b\5:\36\2\u015b")
        buf.write("\u015c\7\64\2\2\u015c\u015d\5 \21\2\u015d\u015e\t\t\2")
        buf.write("\2\u015e\u015f\5 \21\2\u015f\u0160\7\17\2\2\u0160\u0161")
        buf.write("\5(\25\2\u01619\3\2\2\2\u0162\u0170\7#\2\2\u0163\u0164")
        buf.write("\5 \21\2\u0164\u0165\7>\2\2\u0165\u0166\7#\2\2\u0166\u0170")
        buf.write("\3\2\2\2\u0167\u0168\7#\2\2\u0168\u0169\7>\2\2\u0169\u0170")
        buf.write("\7#\2\2\u016a\u016b\5 \21\2\u016b\u016c\7:\2\2\u016c\u016d")
        buf.write("\5 \21\2\u016d\u016e\7;\2\2\u016e\u0170\3\2\2\2\u016f")
        buf.write("\u0162\3\2\2\2\u016f\u0163\3\2\2\2\u016f\u0167\3\2\2\2")
        buf.write("\u016f\u016a\3\2\2\2\u0170;\3\2\2\2\u0171\u0172\7\f\2")
        buf.write("\2\u0172\u0173\7<\2\2\u0173=\3\2\2\2\u0174\u0175\7\16")
        buf.write("\2\2\u0175\u0176\7<\2\2\u0176?\3\2\2\2\u0177\u0178\7\31")
        buf.write("\2\2\u0178\u0179\5 \21\2\u0179\u017a\7<\2\2\u017a\u017e")
        buf.write("\3\2\2\2\u017b\u017c\7\31\2\2\u017c\u017e\7<\2\2\u017d")
        buf.write("\u0177\3\2\2\2\u017d\u017b\3\2\2\2\u017eA\3\2\2\2\u017f")
        buf.write("\u0180\5 \21\2\u0180\u0181\7>\2\2\u0181\u0182\7#\2\2\u0182")
        buf.write("\u0185\78\2\2\u0183\u0186\5\"\22\2\u0184\u0186\3\2\2\2")
        buf.write("\u0185\u0183\3\2\2\2\u0185\u0184\3\2\2\2\u0186\u0187\3")
        buf.write("\2\2\2\u0187\u0188\79\2\2\u0188\u0189\7<\2\2\u0189\u0195")
        buf.write("\3\2\2\2\u018a\u018b\7#\2\2\u018b\u018c\7>\2\2\u018c\u018d")
        buf.write("\7#\2\2\u018d\u0190\78\2\2\u018e\u0191\5\"\22\2\u018f")
        buf.write("\u0191\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192\u0193\79\2\2\u0193\u0195\7")
        buf.write("<\2\2\u0194\u017f\3\2\2\2\u0194\u018a\3\2\2\2\u0195C\3")
        buf.write("\2\2\2%KT\\_ens|\u0084\u0090\u0096\u009e\u00a8\u00b1\u00c6")
        buf.write("\u00d0\u00ea\u00f5\u00f7\u00ff\u0106\u010e\u0118\u011d")
        buf.write("\u0123\u0127\u012d\u0131\u0149\u0157\u016f\u017d\u0185")
        buf.write("\u0190\u0194")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'''", "'/'", "'%'", "'!='", "'=='", 
                     "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
                     "'^'", "':='", "'='", "'{'", "'}'", "'('", "')'", "'['", 
                     "']'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "WS", "BLOCK_CMT", "LINE_CMT", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "STRINGLIT", "ARRAYLIT", "BOOLEAN", 
                      "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
                      "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", 
                      "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                      "FINAL", "STATIC", "TO", "DOWNTO", "ID", "ADD", "SUB", 
                      "MUL", "DIV", "DIVF", "MOD", "NEQ", "EQ", "LESS", 
                      "GREATER", "LEQ", "GREQ", "OR", "AND", "NOT", "CONCAT", 
                      "ASSIGN", "INIT", "LP", "RP", "LB", "RB", "LQ", "RQ", 
                      "SEMI", "COLON", "DOT", "COMMA", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classDeclList = 1
    RULE_classDecl = 2
    RULE_memberList = 3
    RULE_member = 4
    RULE_attrKeyword = 5
    RULE_attrType = 6
    RULE_arrayType = 7
    RULE_attrList = 8
    RULE_attribute = 9
    RULE_returnType = 10
    RULE_method = 11
    RULE_paramList = 12
    RULE_param = 13
    RULE_idList = 14
    RULE_exp = 15
    RULE_argList = 16
    RULE_obj_create = 17
    RULE_stmtList = 18
    RULE_stmt = 19
    RULE_blockStmt = 20
    RULE_blockBody = 21
    RULE_declList = 22
    RULE_decl = 23
    RULE_assignStmt = 24
    RULE_lhs = 25
    RULE_ifStmt = 26
    RULE_forStmt = 27
    RULE_scalarVar = 28
    RULE_breakStmt = 29
    RULE_continueStmt = 30
    RULE_returnStmt = 31
    RULE_methodInvokeStmt = 32

    ruleNames =  [ "program", "classDeclList", "classDecl", "memberList", 
                   "member", "attrKeyword", "attrType", "arrayType", "attrList", 
                   "attribute", "returnType", "method", "paramList", "param", 
                   "idList", "exp", "argList", "obj_create", "stmtList", 
                   "stmt", "blockStmt", "blockBody", "declList", "decl", 
                   "assignStmt", "lhs", "ifStmt", "forStmt", "scalarVar", 
                   "breakStmt", "continueStmt", "returnStmt", "methodInvokeStmt" ]

    EOF = Token.EOF
    WS=1
    BLOCK_CMT=2
    LINE_CMT=3
    INTLIT=4
    FLOATLIT=5
    BOOLLIT=6
    STRINGLIT=7
    ARRAYLIT=8
    BOOLEAN=9
    BREAK=10
    CLASS=11
    CONTINUE=12
    DO=13
    ELSE=14
    EXTENDS=15
    FLOAT=16
    IF=17
    INT=18
    NEW=19
    STRING=20
    THEN=21
    FOR=22
    RETURN=23
    TRUE=24
    FALSE=25
    VOID=26
    NIL=27
    THIS=28
    FINAL=29
    STATIC=30
    TO=31
    DOWNTO=32
    ID=33
    ADD=34
    SUB=35
    MUL=36
    DIV=37
    DIVF=38
    MOD=39
    NEQ=40
    EQ=41
    LESS=42
    GREATER=43
    LEQ=44
    GREQ=45
    OR=46
    AND=47
    NOT=48
    CONCAT=49
    ASSIGN=50
    INIT=51
    LP=52
    RP=53
    LB=54
    RB=55
    LQ=56
    RQ=57
    SEMI=58
    COLON=59
    DOT=60
    COMMA=61
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
            self.state = 66
            self.classDeclList()
            self.state = 67
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
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.classDecl()
                self.state = 70
                self.classDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
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

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def memberList(self):
            return self.getTypedRuleContext(BKOOLParser.MemberListContext,0)


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
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(BKOOLParser.CLASS)
                self.state = 76
                self.match(BKOOLParser.ID)
                self.state = 77
                self.match(BKOOLParser.EXTENDS)
                self.state = 78
                self.match(BKOOLParser.ID)
                self.state = 79
                self.match(BKOOLParser.LP)
                self.state = 82
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                    self.state = 80
                    self.memberList()
                    pass
                elif token in [BKOOLParser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 84
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(BKOOLParser.CLASS)
                self.state = 86
                self.match(BKOOLParser.ID)
                self.state = 87
                self.match(BKOOLParser.LP)
                self.state = 90
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                    self.state = 88
                    self.memberList()
                    pass
                elif token in [BKOOLParser.RP]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 92
                self.match(BKOOLParser.RP)
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.member()
                self.state = 96
                self.memberList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
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

        def attrKeyword(self):
            return self.getTypedRuleContext(BKOOLParser.AttrKeywordContext,0)


        def attrType(self):
            return self.getTypedRuleContext(BKOOLParser.AttrTypeContext,0)


        def attrList(self):
            return self.getTypedRuleContext(BKOOLParser.AttrListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def returnType(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnTypeContext,0)


        def method(self):
            return self.getTypedRuleContext(BKOOLParser.MethodContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.attrKeyword()
                self.state = 102
                self.attrType()
                self.state = 103
                self.attrList()
                self.state = 104
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 106
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 110
                self.returnType()
                self.state = 111
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attrKeyword

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrKeyword" ):
                return visitor.visitAttrKeyword(self)
            else:
                return visitor.visitChildren(self)




    def attrKeyword(self):

        localctx = BKOOLParser.AttrKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrKeyword)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(BKOOLParser.STATIC)
                self.state = 116
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(BKOOLParser.FINAL)
                self.state = 118
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def arrayType(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrType" ):
                return visitor.visitAttrType(self)
            else:
                return visitor.visitChildren(self)




    def attrType(self):

        localctx = BKOOLParser.AttrTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrType)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.arrayType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LQ(self):
            return self.getToken(BKOOLParser.LQ, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RQ(self):
            return self.getToken(BKOOLParser.RQ, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = BKOOLParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 133
            self.match(BKOOLParser.LQ)
            self.state = 134
            self.match(BKOOLParser.INTLIT)
            self.state = 135
            self.match(BKOOLParser.RQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attrList(self):
            return self.getTypedRuleContext(BKOOLParser.AttrListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrList" ):
                return visitor.visitAttrList(self)
            else:
                return visitor.visitChildren(self)




    def attrList(self):

        localctx = BKOOLParser.AttrListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attrList)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.attribute()
                self.state = 138
                self.match(BKOOLParser.COMMA)
                self.state = 139
                self.attrList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.attribute()
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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INIT(self):
            return self.getToken(BKOOLParser.INIT, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attribute)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(BKOOLParser.ID)
                self.state = 145
                self.match(BKOOLParser.INIT)
                self.state = 146
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
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

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = BKOOLParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
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


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = BKOOLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(BKOOLParser.ID)
            self.state = 153
            self.match(BKOOLParser.LB)
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.state = 154
                self.paramList()
                pass
            elif token in [BKOOLParser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 158
            self.match(BKOOLParser.RB)
            self.state = 159
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = BKOOLParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramList)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.param()
                self.state = 162
                self.match(BKOOLParser.SEMI)
                self.state = 163
                self.paramList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrType(self):
            return self.getTypedRuleContext(BKOOLParser.AttrTypeContext,0)


        def idList(self):
            return self.getTypedRuleContext(BKOOLParser.IdListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.attrType()
            self.state = 169
            self.idList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idList(self):
            return self.getTypedRuleContext(BKOOLParser.IdListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = BKOOLParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_idList)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(BKOOLParser.ID)
                self.state = 172
                self.match(BKOOLParser.COMMA)
                self.state = 173
                self.idList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKOOLParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def ARRAYLIT(self):
            return self.getToken(BKOOLParser.ARRAYLIT, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def obj_create(self):
            return self.getTypedRuleContext(BKOOLParser.Obj_createContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def argList(self):
            return self.getTypedRuleContext(BKOOLParser.ArgListContext,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def DIVF(self):
            return self.getToken(BKOOLParser.DIVF, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LEQ(self):
            return self.getToken(BKOOLParser.LEQ, 0)

        def GREQ(self):
            return self.getToken(BKOOLParser.GREQ, 0)

        def LQ(self):
            return self.getToken(BKOOLParser.LQ, 0)

        def RQ(self):
            return self.getToken(BKOOLParser.RQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 178
                self.match(BKOOLParser.LB)
                self.state = 179
                self.exp(0)
                self.state = 180
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.state = 182
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 3:
                self.state = 183
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.state = 184
                self.match(BKOOLParser.BOOLLIT)
                pass

            elif la_ == 5:
                self.state = 185
                self.match(BKOOLParser.STRINGLIT)
                pass

            elif la_ == 6:
                self.state = 186
                self.match(BKOOLParser.ARRAYLIT)
                pass

            elif la_ == 7:
                self.state = 187
                self.match(BKOOLParser.THIS)
                pass

            elif la_ == 8:
                self.state = 188
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 9:
                self.state = 189
                self.obj_create()
                pass

            elif la_ == 10:
                self.state = 190
                self.match(BKOOLParser.ID)
                self.state = 191
                self.match(BKOOLParser.DOT)
                self.state = 192
                self.match(BKOOLParser.ID)
                self.state = 193
                self.match(BKOOLParser.LB)
                self.state = 196
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                    self.state = 194
                    self.argList()
                    pass
                elif token in [BKOOLParser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 198
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 11:
                self.state = 199
                self.match(BKOOLParser.ID)
                self.state = 200
                self.match(BKOOLParser.DOT)
                self.state = 201
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 12:
                self.state = 202
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 203
                self.exp(8)
                pass

            elif la_ == 13:
                self.state = 204
                self.match(BKOOLParser.NOT)
                self.state = 205
                self.exp(7)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 243
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 208
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 209
                        self.match(BKOOLParser.CONCAT)
                        self.state = 210
                        self.exp(7)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 211
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 212
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.DIV) | (1 << BKOOLParser.DIVF) | (1 << BKOOLParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 213
                        self.exp(6)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 214
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 215
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 216
                        self.exp(5)
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 217
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 218
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 219
                        self.exp(4)
                        pass

                    elif la_ == 5:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 220
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 221
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 222
                        self.exp(3)
                        pass

                    elif la_ == 6:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 223
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 224
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LEQ) | (1 << BKOOLParser.GREQ))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        self.exp(2)
                        pass

                    elif la_ == 7:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 226
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 227
                        self.match(BKOOLParser.DOT)
                        self.state = 228
                        self.match(BKOOLParser.ID)
                        self.state = 229
                        self.match(BKOOLParser.LB)
                        self.state = 232
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                            self.state = 230
                            self.argList()
                            pass
                        elif token in [BKOOLParser.RB]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 234
                        self.match(BKOOLParser.RB)
                        pass

                    elif la_ == 8:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 235
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 236
                        self.match(BKOOLParser.DOT)
                        self.state = 237
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 9:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 238
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 239
                        self.match(BKOOLParser.LQ)
                        self.state = 240
                        self.exp(0)
                        self.state = 241
                        self.match(BKOOLParser.RQ)
                        pass

             
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def argList(self):
            return self.getTypedRuleContext(BKOOLParser.ArgListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = BKOOLParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_argList)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.exp(0)
                self.state = 249
                self.match(BKOOLParser.COMMA)
                self.state = 250
                self.argList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def argList(self):
            return self.getTypedRuleContext(BKOOLParser.ArgListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_obj_create

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_create" ):
                return visitor.visitObj_create(self)
            else:
                return visitor.visitChildren(self)




    def obj_create(self):

        localctx = BKOOLParser.Obj_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_obj_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(BKOOLParser.NEW)
            self.state = 256
            self.match(BKOOLParser.ID)
            self.state = 257
            self.match(BKOOLParser.LB)
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                self.state = 258
                self.argList()
                pass
            elif token in [BKOOLParser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 262
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def stmtList(self):
            return self.getTypedRuleContext(BKOOLParser.StmtListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtList" ):
                return visitor.visitStmtList(self)
            else:
                return visitor.visitChildren(self)




    def stmtList(self):

        localctx = BKOOLParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmtList)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.stmt()
                self.state = 265
                self.stmtList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnStmtContext,0)


        def methodInvokeStmt(self):
            return self.getTypedRuleContext(BKOOLParser.MethodInvokeStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.blockStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 273
                self.forStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 274
                self.breakStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 275
                self.continueStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 276
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 277
                self.methodInvokeStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def blockBody(self):
            return self.getTypedRuleContext(BKOOLParser.BlockBodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = BKOOLParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_blockStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(BKOOLParser.LP)
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 281
                self.blockBody()
                pass

            elif la_ == 2:
                pass


            self.state = 285
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declList(self):
            return self.getTypedRuleContext(BKOOLParser.DeclListContext,0)


        def stmtList(self):
            return self.getTypedRuleContext(BKOOLParser.StmtListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockBody" ):
                return visitor.visitBlockBody(self)
            else:
                return visitor.visitChildren(self)




    def blockBody(self):

        localctx = BKOOLParser.BlockBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_blockBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 287
                self.declList()
                pass

            elif la_ == 2:
                pass


            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LP, BKOOLParser.LB]:
                self.state = 291
                self.stmtList()
                pass
            elif token in [BKOOLParser.RP]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def declList(self):
            return self.getTypedRuleContext(BKOOLParser.DeclListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_declList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclList" ):
                return visitor.visitDeclList(self)
            else:
                return visitor.visitChildren(self)




    def declList(self):

        localctx = BKOOLParser.DeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_declList)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.decl()
                self.state = 296
                self.declList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrType(self):
            return self.getTypedRuleContext(BKOOLParser.AttrTypeContext,0)


        def attrList(self):
            return self.getTypedRuleContext(BKOOLParser.AttrListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FINAL]:
                self.state = 301
                self.match(BKOOLParser.FINAL)
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 305
            self.attrType()
            self.state = 306
            self.attrList()
            self.state = 307
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = BKOOLParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.lhs()
            self.state = 310
            self.match(BKOOLParser.ASSIGN)
            self.state = 311
            self.exp(0)
            self.state = 312
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LQ(self):
            return self.getToken(BKOOLParser.LQ, 0)

        def RQ(self):
            return self.getToken(BKOOLParser.RQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lhs)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.exp(0)
                self.state = 316
                self.match(BKOOLParser.DOT)
                self.state = 317
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.match(BKOOLParser.ID)
                self.state = 320
                self.match(BKOOLParser.DOT)
                self.state = 321
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.exp(0)
                self.state = 323
                self.match(BKOOLParser.LQ)
                self.state = 324
                self.exp(0)
                self.state = 325
                self.match(BKOOLParser.RQ)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BKOOLParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifStmt)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(BKOOLParser.IF)
                self.state = 330
                self.exp(0)
                self.state = 331
                self.match(BKOOLParser.THEN)
                self.state = 332
                self.stmt()
                self.state = 333
                self.match(BKOOLParser.ELSE)
                self.state = 334
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(BKOOLParser.IF)
                self.state = 337
                self.exp(0)
                self.state = 338
                self.match(BKOOLParser.THEN)
                self.state = 339
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def scalarVar(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarVarContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BKOOLParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(BKOOLParser.FOR)
            self.state = 344
            self.scalarVar()
            self.state = 345
            self.match(BKOOLParser.ASSIGN)
            self.state = 346
            self.exp(0)
            self.state = 347
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 348
            self.exp(0)
            self.state = 349
            self.match(BKOOLParser.DO)
            self.state = 350
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LQ(self):
            return self.getToken(BKOOLParser.LQ, 0)

        def RQ(self):
            return self.getToken(BKOOLParser.RQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalarVar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarVar" ):
                return visitor.visitScalarVar(self)
            else:
                return visitor.visitChildren(self)




    def scalarVar(self):

        localctx = BKOOLParser.ScalarVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_scalarVar)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.exp(0)
                self.state = 354
                self.match(BKOOLParser.DOT)
                self.state = 355
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 357
                self.match(BKOOLParser.ID)
                self.state = 358
                self.match(BKOOLParser.DOT)
                self.state = 359
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 360
                self.exp(0)
                self.state = 361
                self.match(BKOOLParser.LQ)
                self.state = 362
                self.exp(0)
                self.state = 363
                self.match(BKOOLParser.RQ)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = BKOOLParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(BKOOLParser.BREAK)
            self.state = 368
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = BKOOLParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(BKOOLParser.CONTINUE)
            self.state = 371
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_returnStmt)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(BKOOLParser.RETURN)
                self.state = 374
                self.exp(0)
                self.state = 375
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.match(BKOOLParser.RETURN)
                self.state = 378
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvokeStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def argList(self):
            return self.getTypedRuleContext(BKOOLParser.ArgListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodInvokeStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvokeStmt" ):
                return visitor.visitMethodInvokeStmt(self)
            else:
                return visitor.visitChildren(self)




    def methodInvokeStmt(self):

        localctx = BKOOLParser.MethodInvokeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_methodInvokeStmt)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.exp(0)
                self.state = 382
                self.match(BKOOLParser.DOT)
                self.state = 383
                self.match(BKOOLParser.ID)
                self.state = 384
                self.match(BKOOLParser.LB)
                self.state = 387
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                    self.state = 385
                    self.argList()
                    pass
                elif token in [BKOOLParser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 389
                self.match(BKOOLParser.RB)
                self.state = 390
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.match(BKOOLParser.ID)
                self.state = 393
                self.match(BKOOLParser.DOT)
                self.state = 394
                self.match(BKOOLParser.ID)
                self.state = 395
                self.match(BKOOLParser.LB)
                self.state = 398
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAYLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ID, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB]:
                    self.state = 396
                    self.argList()
                    pass
                elif token in [BKOOLParser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 400
                self.match(BKOOLParser.RB)
                self.state = 401
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 9)
         




