# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01fd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\7\5\u00a8\n\5\f\5\16\5\u00ab\13\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\7\6\u00b4\n\6\f\6\16\6\u00b7\13\6\3\6\5\6\u00ba")
        buf.write("\n\6\3\6\3\6\3\7\6\7\u00bf\n\7\r\7\16\7\u00c0\3\b\6\b")
        buf.write("\u00c4\n\b\r\b\16\b\u00c5\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u00cf\n\t\3\n\3\n\7\n\u00d3\n\n\f\n\16\n\u00d6\13")
        buf.write("\n\3\13\3\13\5\13\u00da\n\13\3\13\6\13\u00dd\n\13\r\13")
        buf.write("\16\13\u00de\3\f\3\f\3\r\3\r\5\r\u00e5\n\r\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00f0\n\20\3\21")
        buf.write("\3\21\7\21\u00f4\n\21\f\21\16\21\u00f7\13\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u0105\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u010e")
        buf.write("\n\23\3\24\3\24\3\24\3\24\5\24\u0114\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$")
        buf.write("\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*")
        buf.write("\3*\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\5-\u019d\n-\3")
        buf.write("-\3-\3-\7-\u01a2\n-\f-\16-\u01a5\13-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\67\3\67\38\38\39\39\39\3:\3:\3")
        buf.write(":\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3")
        buf.write("K\3K\3K\3L\3L\7L\u01ed\nL\fL\16L\u01f0\13L\3L\3L\3M\3")
        buf.write("M\7M\u01f6\nM\fM\16M\u01f9\13M\3M\3M\3M\4\u00a9\u00b5")
        buf.write("\2N\3\2\5\2\7\3\t\4\13\5\r\6\17\7\21\2\23\2\25\2\27\2")
        buf.write("\31\b\33\2\35\2\37\2!\t#\n%\2\'\2)\13+\f-\r/\16\61\17")
        buf.write("\63\20\65\21\67\229\23;\24=\25?\26A\27C\30E\31G\32I\33")
        buf.write("K\34M\35O\36Q\37S U!W\"Y#[\2]$_%a&c\'e(g)i*k+m,o-q.s/")
        buf.write("u\60w\61y\62{\63}\64\177\65\u0081\66\u0083\67\u00858\u0087")
        buf.write("9\u0089:\u008b;\u008d<\u008f=\u0091>\u0093?\u0095@\u0097")
        buf.write("A\u0099B\3\2\13\3\2\62;\4\2C\\c|\5\2\13\f\16\17\"\"\3")
        buf.write("\3\f\f\4\2GGgg\4\2--//\5\2\n\13\16\17^^\b\2$$^^ddhhtt")
        buf.write("vv\4\2\f\f$$\2\u0208\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\31\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\3\u009b\3\2\2\2\5\u009d\3\2\2\2\7\u009f\3\2\2\2\t\u00a3")
        buf.write("\3\2\2\2\13\u00b1\3\2\2\2\r\u00be\3\2\2\2\17\u00c3\3\2")
        buf.write("\2\2\21\u00ce\3\2\2\2\23\u00d0\3\2\2\2\25\u00d7\3\2\2")
        buf.write("\2\27\u00e0\3\2\2\2\31\u00e4\3\2\2\2\33\u00e6\3\2\2\2")
        buf.write("\35\u00e8\3\2\2\2\37\u00ef\3\2\2\2!\u00f1\3\2\2\2#\u0104")
        buf.write("\3\2\2\2%\u010d\3\2\2\2\'\u0113\3\2\2\2)\u0115\3\2\2\2")
        buf.write("+\u011d\3\2\2\2-\u0123\3\2\2\2/\u0129\3\2\2\2\61\u0132")
        buf.write("\3\2\2\2\63\u0135\3\2\2\2\65\u013a\3\2\2\2\67\u0142\3")
        buf.write("\2\2\29\u0148\3\2\2\2;\u014b\3\2\2\2=\u014f\3\2\2\2?\u0153")
        buf.write("\3\2\2\2A\u015a\3\2\2\2C\u015f\3\2\2\2E\u0163\3\2\2\2")
        buf.write("G\u016a\3\2\2\2I\u016f\3\2\2\2K\u0175\3\2\2\2M\u017a\3")
        buf.write("\2\2\2O\u017e\3\2\2\2Q\u0183\3\2\2\2S\u0189\3\2\2\2U\u0190")
        buf.write("\3\2\2\2W\u0193\3\2\2\2Y\u019c\3\2\2\2[\u01a6\3\2\2\2")
        buf.write("]\u01a8\3\2\2\2_\u01aa\3\2\2\2a\u01ac\3\2\2\2c\u01ae\3")
        buf.write("\2\2\2e\u01b0\3\2\2\2g\u01b2\3\2\2\2i\u01b4\3\2\2\2k\u01b7")
        buf.write("\3\2\2\2m\u01ba\3\2\2\2o\u01bc\3\2\2\2q\u01be\3\2\2\2")
        buf.write("s\u01c1\3\2\2\2u\u01c4\3\2\2\2w\u01c7\3\2\2\2y\u01ca\3")
        buf.write("\2\2\2{\u01cc\3\2\2\2}\u01ce\3\2\2\2\177\u01d1\3\2\2\2")
        buf.write("\u0081\u01d3\3\2\2\2\u0083\u01d5\3\2\2\2\u0085\u01d7\3")
        buf.write("\2\2\2\u0087\u01d9\3\2\2\2\u0089\u01db\3\2\2\2\u008b\u01dd")
        buf.write("\3\2\2\2\u008d\u01df\3\2\2\2\u008f\u01e1\3\2\2\2\u0091")
        buf.write("\u01e3\3\2\2\2\u0093\u01e5\3\2\2\2\u0095\u01e7\3\2\2\2")
        buf.write("\u0097\u01ea\3\2\2\2\u0099\u01f3\3\2\2\2\u009b\u009c\t")
        buf.write("\2\2\2\u009c\4\3\2\2\2\u009d\u009e\t\3\2\2\u009e\6\3\2")
        buf.write("\2\2\u009f\u00a0\t\4\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2")
        buf.write("\b\4\2\2\u00a2\b\3\2\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5")
        buf.write("\7,\2\2\u00a5\u00a9\3\2\2\2\u00a6\u00a8\13\2\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3")
        buf.write("\2\2\2\u00ac\u00ad\7,\2\2\u00ad\u00ae\7\61\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b0\b\5\2\2\u00b0\n\3\2\2\2\u00b1\u00b5")
        buf.write("\7%\2\2\u00b2\u00b4\13\2\2\2\u00b3\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b7\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba\t")
        buf.write("\5\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc")
        buf.write("\b\6\2\2\u00bc\f\3\2\2\2\u00bd\u00bf\5\3\2\2\u00be\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\16\3\2\2\2\u00c2\u00c4\5\3\2\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\5")
        buf.write("\21\t\2\u00c8\20\3\2\2\2\u00c9\u00ca\5\23\n\2\u00ca\u00cb")
        buf.write("\5\25\13\2\u00cb\u00cf\3\2\2\2\u00cc\u00cf\5\23\n\2\u00cd")
        buf.write("\u00cf\5\25\13\2\u00ce\u00c9\3\2\2\2\u00ce\u00cc\3\2\2")
        buf.write("\2\u00ce\u00cd\3\2\2\2\u00cf\22\3\2\2\2\u00d0\u00d4\5")
        buf.write("\u0091I\2\u00d1\u00d3\5\3\2\2\u00d2\u00d1\3\2\2\2\u00d3")
        buf.write("\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\24\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d9\t\6")
        buf.write("\2\2\u00d8\u00da\5\27\f\2\u00d9\u00d8\3\2\2\2\u00d9\u00da")
        buf.write("\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00dd\5\3\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00de\u00df\3\2\2\2\u00df\26\3\2\2\2\u00e0\u00e1\t\7")
        buf.write("\2\2\u00e1\30\3\2\2\2\u00e2\u00e5\5G$\2\u00e3\u00e5\5")
        buf.write("I%\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\32")
        buf.write("\3\2\2\2\u00e6\u00e7\t\b\2\2\u00e7\34\3\2\2\2\u00e8\u00e9")
        buf.write("\7^\2\2\u00e9\u00ea\n\t\2\2\u00ea\36\3\2\2\2\u00eb\u00f0")
        buf.write("\n\n\2\2\u00ec\u00f0\5\33\16\2\u00ed\u00ee\7^\2\2\u00ee")
        buf.write("\u00f0\7$\2\2\u00ef\u00eb\3\2\2\2\u00ef\u00ec\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00f0 \3\2\2\2\u00f1\u00f5\7$\2\2")
        buf.write("\u00f2\u00f4\5\37\20\2\u00f3\u00f2\3\2\2\2\u00f4\u00f7")
        buf.write("\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6")
        buf.write("\u00f8\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9\7$\2\2")
        buf.write("\u00f9\u00fa\b\21\3\2\u00fa\"\3\2\2\2\u00fb\u00fc\5\u0081")
        buf.write("A\2\u00fc\u00fd\5\'\24\2\u00fd\u00fe\5%\23\2\u00fe\u00ff")
        buf.write("\5\u0083B\2\u00ff\u0105\3\2\2\2\u0100\u0101\5\u0081A\2")
        buf.write("\u0101\u0102\5\'\24\2\u0102\u0103\5\u0083B\2\u0103\u0105")
        buf.write("\3\2\2\2\u0104\u00fb\3\2\2\2\u0104\u0100\3\2\2\2\u0105")
        buf.write("$\3\2\2\2\u0106\u0107\5\u0093J\2\u0107\u0108\5\'\24\2")
        buf.write("\u0108\u0109\5%\23\2\u0109\u010e\3\2\2\2\u010a\u010b\5")
        buf.write("\u0093J\2\u010b\u010c\5\'\24\2\u010c\u010e\3\2\2\2\u010d")
        buf.write("\u0106\3\2\2\2\u010d\u010a\3\2\2\2\u010e&\3\2\2\2\u010f")
        buf.write("\u0114\5\r\7\2\u0110\u0114\5\17\b\2\u0111\u0114\5\31\r")
        buf.write("\2\u0112\u0114\5!\21\2\u0113\u010f\3\2\2\2\u0113\u0110")
        buf.write("\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114")
        buf.write("(\3\2\2\2\u0115\u0116\7d\2\2\u0116\u0117\7q\2\2\u0117")
        buf.write("\u0118\7q\2\2\u0118\u0119\7n\2\2\u0119\u011a\7g\2\2\u011a")
        buf.write("\u011b\7c\2\2\u011b\u011c\7p\2\2\u011c*\3\2\2\2\u011d")
        buf.write("\u011e\7d\2\2\u011e\u011f\7t\2\2\u011f\u0120\7g\2\2\u0120")
        buf.write("\u0121\7c\2\2\u0121\u0122\7m\2\2\u0122,\3\2\2\2\u0123")
        buf.write("\u0124\7e\2\2\u0124\u0125\7n\2\2\u0125\u0126\7c\2\2\u0126")
        buf.write("\u0127\7u\2\2\u0127\u0128\7u\2\2\u0128.\3\2\2\2\u0129")
        buf.write("\u012a\7e\2\2\u012a\u012b\7q\2\2\u012b\u012c\7p\2\2\u012c")
        buf.write("\u012d\7v\2\2\u012d\u012e\7k\2\2\u012e\u012f\7p\2\2\u012f")
        buf.write("\u0130\7w\2\2\u0130\u0131\7g\2\2\u0131\60\3\2\2\2\u0132")
        buf.write("\u0133\7f\2\2\u0133\u0134\7q\2\2\u0134\62\3\2\2\2\u0135")
        buf.write("\u0136\7g\2\2\u0136\u0137\7n\2\2\u0137\u0138\7u\2\2\u0138")
        buf.write("\u0139\7g\2\2\u0139\64\3\2\2\2\u013a\u013b\7g\2\2\u013b")
        buf.write("\u013c\7z\2\2\u013c\u013d\7v\2\2\u013d\u013e\7g\2\2\u013e")
        buf.write("\u013f\7p\2\2\u013f\u0140\7f\2\2\u0140\u0141\7u\2\2\u0141")
        buf.write("\66\3\2\2\2\u0142\u0143\7h\2\2\u0143\u0144\7n\2\2\u0144")
        buf.write("\u0145\7q\2\2\u0145\u0146\7c\2\2\u0146\u0147\7v\2\2\u0147")
        buf.write("8\3\2\2\2\u0148\u0149\7k\2\2\u0149\u014a\7h\2\2\u014a")
        buf.write(":\3\2\2\2\u014b\u014c\7k\2\2\u014c\u014d\7p\2\2\u014d")
        buf.write("\u014e\7v\2\2\u014e<\3\2\2\2\u014f\u0150\7p\2\2\u0150")
        buf.write("\u0151\7g\2\2\u0151\u0152\7y\2\2\u0152>\3\2\2\2\u0153")
        buf.write("\u0154\7u\2\2\u0154\u0155\7v\2\2\u0155\u0156\7t\2\2\u0156")
        buf.write("\u0157\7k\2\2\u0157\u0158\7p\2\2\u0158\u0159\7i\2\2\u0159")
        buf.write("@\3\2\2\2\u015a\u015b\7v\2\2\u015b\u015c\7j\2\2\u015c")
        buf.write("\u015d\7g\2\2\u015d\u015e\7p\2\2\u015eB\3\2\2\2\u015f")
        buf.write("\u0160\7h\2\2\u0160\u0161\7q\2\2\u0161\u0162\7t\2\2\u0162")
        buf.write("D\3\2\2\2\u0163\u0164\7t\2\2\u0164\u0165\7g\2\2\u0165")
        buf.write("\u0166\7v\2\2\u0166\u0167\7w\2\2\u0167\u0168\7t\2\2\u0168")
        buf.write("\u0169\7p\2\2\u0169F\3\2\2\2\u016a\u016b\7v\2\2\u016b")
        buf.write("\u016c\7t\2\2\u016c\u016d\7w\2\2\u016d\u016e\7g\2\2\u016e")
        buf.write("H\3\2\2\2\u016f\u0170\7h\2\2\u0170\u0171\7c\2\2\u0171")
        buf.write("\u0172\7n\2\2\u0172\u0173\7u\2\2\u0173\u0174\7g\2\2\u0174")
        buf.write("J\3\2\2\2\u0175\u0176\7x\2\2\u0176\u0177\7q\2\2\u0177")
        buf.write("\u0178\7k\2\2\u0178\u0179\7f\2\2\u0179L\3\2\2\2\u017a")
        buf.write("\u017b\7p\2\2\u017b\u017c\7k\2\2\u017c\u017d\7n\2\2\u017d")
        buf.write("N\3\2\2\2\u017e\u017f\7v\2\2\u017f\u0180\7j\2\2\u0180")
        buf.write("\u0181\7k\2\2\u0181\u0182\7u\2\2\u0182P\3\2\2\2\u0183")
        buf.write("\u0184\7h\2\2\u0184\u0185\7k\2\2\u0185\u0186\7p\2\2\u0186")
        buf.write("\u0187\7c\2\2\u0187\u0188\7n\2\2\u0188R\3\2\2\2\u0189")
        buf.write("\u018a\7u\2\2\u018a\u018b\7v\2\2\u018b\u018c\7c\2\2\u018c")
        buf.write("\u018d\7v\2\2\u018d\u018e\7k\2\2\u018e\u018f\7e\2\2\u018f")
        buf.write("T\3\2\2\2\u0190\u0191\7v\2\2\u0191\u0192\7q\2\2\u0192")
        buf.write("V\3\2\2\2\u0193\u0194\7f\2\2\u0194\u0195\7q\2\2\u0195")
        buf.write("\u0196\7y\2\2\u0196\u0197\7p\2\2\u0197\u0198\7v\2\2\u0198")
        buf.write("\u0199\7q\2\2\u0199X\3\2\2\2\u019a\u019d\5\5\3\2\u019b")
        buf.write("\u019d\5[.\2\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("\u01a3\3\2\2\2\u019e\u01a2\5\5\3\2\u019f\u01a2\5\3\2\2")
        buf.write("\u01a0\u01a2\5[.\2\u01a1\u019e\3\2\2\2\u01a1\u019f\3\2")
        buf.write("\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4Z\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a6\u01a7\7a\2\2\u01a7\\\3\2\2\2\u01a8\u01a9")
        buf.write("\7-\2\2\u01a9^\3\2\2\2\u01aa\u01ab\7/\2\2\u01ab`\3\2\2")
        buf.write("\2\u01ac\u01ad\7,\2\2\u01adb\3\2\2\2\u01ae\u01af\7)\2")
        buf.write("\2\u01afd\3\2\2\2\u01b0\u01b1\7\61\2\2\u01b1f\3\2\2\2")
        buf.write("\u01b2\u01b3\7\'\2\2\u01b3h\3\2\2\2\u01b4\u01b5\7#\2\2")
        buf.write("\u01b5\u01b6\7?\2\2\u01b6j\3\2\2\2\u01b7\u01b8\7?\2\2")
        buf.write("\u01b8\u01b9\7?\2\2\u01b9l\3\2\2\2\u01ba\u01bb\7>\2\2")
        buf.write("\u01bbn\3\2\2\2\u01bc\u01bd\7@\2\2\u01bdp\3\2\2\2\u01be")
        buf.write("\u01bf\7>\2\2\u01bf\u01c0\7?\2\2\u01c0r\3\2\2\2\u01c1")
        buf.write("\u01c2\7@\2\2\u01c2\u01c3\7?\2\2\u01c3t\3\2\2\2\u01c4")
        buf.write("\u01c5\7~\2\2\u01c5\u01c6\7~\2\2\u01c6v\3\2\2\2\u01c7")
        buf.write("\u01c8\7(\2\2\u01c8\u01c9\7(\2\2\u01c9x\3\2\2\2\u01ca")
        buf.write("\u01cb\7#\2\2\u01cbz\3\2\2\2\u01cc\u01cd\7`\2\2\u01cd")
        buf.write("|\3\2\2\2\u01ce\u01cf\7<\2\2\u01cf\u01d0\7?\2\2\u01d0")
        buf.write("~\3\2\2\2\u01d1\u01d2\7?\2\2\u01d2\u0080\3\2\2\2\u01d3")
        buf.write("\u01d4\7}\2\2\u01d4\u0082\3\2\2\2\u01d5\u01d6\7\177\2")
        buf.write("\2\u01d6\u0084\3\2\2\2\u01d7\u01d8\7*\2\2\u01d8\u0086")
        buf.write("\3\2\2\2\u01d9\u01da\7+\2\2\u01da\u0088\3\2\2\2\u01db")
        buf.write("\u01dc\7]\2\2\u01dc\u008a\3\2\2\2\u01dd\u01de\7_\2\2\u01de")
        buf.write("\u008c\3\2\2\2\u01df\u01e0\7=\2\2\u01e0\u008e\3\2\2\2")
        buf.write("\u01e1\u01e2\7<\2\2\u01e2\u0090\3\2\2\2\u01e3\u01e4\7")
        buf.write("\60\2\2\u01e4\u0092\3\2\2\2\u01e5\u01e6\7.\2\2\u01e6\u0094")
        buf.write("\3\2\2\2\u01e7\u01e8\13\2\2\2\u01e8\u01e9\bK\4\2\u01e9")
        buf.write("\u0096\3\2\2\2\u01ea\u01ee\7$\2\2\u01eb\u01ed\5\37\20")
        buf.write("\2\u01ec\u01eb\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec")
        buf.write("\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f1\u01f2\bL\5\2\u01f2\u0098\3\2\2\2")
        buf.write("\u01f3\u01f7\7$\2\2\u01f4\u01f6\5\37\20\2\u01f5\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f7\3\2\2\2")
        buf.write("\u01fa\u01fb\5\35\17\2\u01fb\u01fc\bM\6\2\u01fc\u009a")
        buf.write("\3\2\2\2\27\2\u00a9\u00b5\u00b9\u00c0\u00c5\u00ce\u00d4")
        buf.write("\u00d9\u00de\u00e4\u00ef\u00f5\u0104\u010d\u0113\u019c")
        buf.write("\u01a1\u01a3\u01ee\u01f7\7\b\2\2\3\21\2\3K\3\3L\4\3M\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BLOCK_CMT = 2
    LINE_CMT = 3
    INTLIT = 4
    FLOATLIT = 5
    BOOLLIT = 6
    STRINGLIT = 7
    ARRAYLIT = 8
    BOOLEAN = 9
    BREAK = 10
    CLASS = 11
    CONTINUE = 12
    DO = 13
    ELSE = 14
    EXTENDS = 15
    FLOAT = 16
    IF = 17
    INT = 18
    NEW = 19
    STRING = 20
    THEN = 21
    FOR = 22
    RETURN = 23
    TRUE = 24
    FALSE = 25
    VOID = 26
    NIL = 27
    THIS = 28
    FINAL = 29
    STATIC = 30
    TO = 31
    DOWNTO = 32
    ID = 33
    ADD = 34
    SUB = 35
    MUL = 36
    DIV = 37
    DIVF = 38
    MOD = 39
    NEQ = 40
    EQ = 41
    LESS = 42
    GREATER = 43
    LEQ = 44
    GREQ = 45
    OR = 46
    AND = 47
    NOT = 48
    CONCAT = 49
    ASSIGN = 50
    INIT = 51
    LP = 52
    RP = 53
    LB = 54
    RB = 55
    LQ = 56
    RQ = 57
    SEMI = 58
    COLON = 59
    DOT = 60
    COMMA = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'+'", "'-'", "'*'", "'''", "'/'", "'%'", "'!='", "'=='", "'<'", 
            "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", 
            "'='", "'{'", "'}'", "'('", "')'", "'['", "']'", "';'", "':'", 
            "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLOCK_CMT", "LINE_CMT", "INTLIT", "FLOATLIT", "BOOLLIT", 
            "STRINGLIT", "ARRAYLIT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
            "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
            "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
            "FINAL", "STATIC", "TO", "DOWNTO", "ID", "ADD", "SUB", "MUL", 
            "DIV", "DIVF", "MOD", "NEQ", "EQ", "LESS", "GREATER", "LEQ", 
            "GREQ", "OR", "AND", "NOT", "CONCAT", "ASSIGN", "INIT", "LP", 
            "RP", "LB", "RB", "LQ", "RQ", "SEMI", "COLON", "DOT", "COMMA", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "DIGIT", "CHAR", "WS", "BLOCK_CMT", "LINE_CMT", "INTLIT", 
                  "FLOATLIT", "FLOAT_END", "DECPART", "EXPPART", "SIGN", 
                  "BOOLLIT", "ESCAPE", "ILLEGAL_ESC", "CHARS", "STRINGLIT", 
                  "ARRAYLIT", "LITLIST", "LITERAL", "BOOLEAN", "BREAK", 
                  "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", 
                  "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
                  "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                  "TO", "DOWNTO", "ID", "UNDERSCORE", "ADD", "SUB", "MUL", 
                  "DIV", "DIVF", "MOD", "NEQ", "EQ", "LESS", "GREATER", 
                  "LEQ", "GREQ", "OR", "AND", "NOT", "CONCAT", "ASSIGN", 
                  "INIT", "LP", "RP", "LB", "RB", "LQ", "RQ", "SEMI", "COLON", 
                  "DOT", "COMMA", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[15] = self.STRINGLIT_action 
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.UNCLOSE_STRING_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    # self.text = (str(self.text))[1:-1]
                    pass
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:])

     


