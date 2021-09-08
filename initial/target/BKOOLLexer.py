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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n\6\3\6\3\6\3\7\3\7\5\7\u00c0\n\7\3\7\3\7\3\7\7\7\u00c5")
        buf.write("\n\7\f\7\16\7\u00c8\13\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\6<\u018f\n<\r<\16<\u0190\3=\6=\u0194\n=")
        buf.write("\r=\16=\u0195\3=\3=\3>\3>\3>\3>\3>\5>\u019f\n>\3?\3?\7")
        buf.write("?\u01a3\n?\f?\16?\u01a6\13?\3@\3@\5@\u01aa\n@\3@\6@\u01ad")
        buf.write("\n@\r@\16@\u01ae\3A\3A\3B\3B\5B\u01b5\nB\3C\3C\3D\3E\3")
        buf.write("E\5E\u01bc\nE\3F\3F\7F\u01c0\nF\fF\16F\u01c3\13F\3F\3")
        buf.write("F\3G\3G\3G\5G\u01ca\nG\3G\3G\3H\3H\3H\3H\3I\3I\3I\3I\5")
        buf.write("I\u01d6\nI\3J\3J\3K\3K\3L\3L\3M\3M\4\u00a9\u00b5\2N\3")
        buf.write("\2\5\2\7\3\t\4\13\5\r\6\17\2\21\7\23\b\25\t\27\n\31\13")
        buf.write("\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27")
        buf.write("\63\30\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&")
        buf.write("Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8")
        buf.write("u9w:y;{\2}\2\177\2\u0081\2\u0083<\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b=\u008d>\u008f?\u0091\2\u0093@\u0095A\u0097B\u0099")
        buf.write("C\3\2\n\3\2\62;\4\2C\\c|\5\2\13\f\16\17\"\"\3\3\f\f\4")
        buf.write("\2GGgg\4\2--//\5\2\n\13\16\17^^\4\2\f\f$$\2\u01e7\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2\u0083\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3")
        buf.write("\2\2\2\2\u008f\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2")
        buf.write("\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u009b\3\2\2\2\5\u009d")
        buf.write("\3\2\2\2\7\u009f\3\2\2\2\t\u00a3\3\2\2\2\13\u00b1\3\2")
        buf.write("\2\2\r\u00bf\3\2\2\2\17\u00c9\3\2\2\2\21\u00cb\3\2\2\2")
        buf.write("\23\u00d3\3\2\2\2\25\u00d9\3\2\2\2\27\u00df\3\2\2\2\31")
        buf.write("\u00e8\3\2\2\2\33\u00eb\3\2\2\2\35\u00f0\3\2\2\2\37\u00f8")
        buf.write("\3\2\2\2!\u00fe\3\2\2\2#\u0101\3\2\2\2%\u0105\3\2\2\2")
        buf.write("\'\u0109\3\2\2\2)\u0110\3\2\2\2+\u0115\3\2\2\2-\u0119")
        buf.write("\3\2\2\2/\u0120\3\2\2\2\61\u0125\3\2\2\2\63\u012b\3\2")
        buf.write("\2\2\65\u0130\3\2\2\2\67\u0134\3\2\2\29\u0139\3\2\2\2")
        buf.write(";\u013f\3\2\2\2=\u0146\3\2\2\2?\u0149\3\2\2\2A\u0150\3")
        buf.write("\2\2\2C\u0152\3\2\2\2E\u0154\3\2\2\2G\u0156\3\2\2\2I\u0158")
        buf.write("\3\2\2\2K\u015a\3\2\2\2M\u015c\3\2\2\2O\u015f\3\2\2\2")
        buf.write("Q\u0162\3\2\2\2S\u0164\3\2\2\2U\u0166\3\2\2\2W\u0169\3")
        buf.write("\2\2\2Y\u016c\3\2\2\2[\u016f\3\2\2\2]\u0172\3\2\2\2_\u0174")
        buf.write("\3\2\2\2a\u0176\3\2\2\2c\u0179\3\2\2\2e\u017b\3\2\2\2")
        buf.write("g\u017d\3\2\2\2i\u017f\3\2\2\2k\u0181\3\2\2\2m\u0183\3")
        buf.write("\2\2\2o\u0185\3\2\2\2q\u0187\3\2\2\2s\u0189\3\2\2\2u\u018b")
        buf.write("\3\2\2\2w\u018e\3\2\2\2y\u0193\3\2\2\2{\u019e\3\2\2\2")
        buf.write("}\u01a0\3\2\2\2\177\u01a7\3\2\2\2\u0081\u01b0\3\2\2\2")
        buf.write("\u0083\u01b4\3\2\2\2\u0085\u01b6\3\2\2\2\u0087\u01b8\3")
        buf.write("\2\2\2\u0089\u01bb\3\2\2\2\u008b\u01bd\3\2\2\2\u008d\u01c6")
        buf.write("\3\2\2\2\u008f\u01cd\3\2\2\2\u0091\u01d5\3\2\2\2\u0093")
        buf.write("\u01d7\3\2\2\2\u0095\u01d9\3\2\2\2\u0097\u01db\3\2\2\2")
        buf.write("\u0099\u01dd\3\2\2\2\u009b\u009c\t\2\2\2\u009c\4\3\2\2")
        buf.write("\2\u009d\u009e\t\3\2\2\u009e\6\3\2\2\2\u009f\u00a0\t\4")
        buf.write("\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\b\4\2\2\u00a2\b\3")
        buf.write("\2\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5\7,\2\2\u00a5\u00a9")
        buf.write("\3\2\2\2\u00a6\u00a8\13\2\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00ab\3\2\2\2\u00a9\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\7")
        buf.write(",\2\2\u00ad\u00ae\7\61\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0")
        buf.write("\b\5\2\2\u00b0\n\3\2\2\2\u00b1\u00b5\7%\2\2\u00b2\u00b4")
        buf.write("\13\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b9\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b8\u00ba\t\5\2\2\u00b9\u00b8\3")
        buf.write("\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\b\6\2\2\u00bc\f")
        buf.write("\3\2\2\2\u00bd\u00c0\5\5\3\2\u00be\u00c0\5\17\b\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\u00c6\3\2\2\2")
        buf.write("\u00c1\u00c5\5\5\3\2\u00c2\u00c5\5\3\2\2\u00c3\u00c5\5")
        buf.write("\17\b\2\u00c4\u00c1\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\16\3\2\2\2\u00c8\u00c6\3\2")
        buf.write("\2\2\u00c9\u00ca\7a\2\2\u00ca\20\3\2\2\2\u00cb\u00cc\7")
        buf.write("d\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\22\3\2\2\2\u00d3\u00d4\7d\2\2\u00d4\u00d5")
        buf.write("\7t\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8")
        buf.write("\7m\2\2\u00d8\24\3\2\2\2\u00d9\u00da\7e\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de")
        buf.write("\7u\2\2\u00de\26\3\2\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\30\3\2\2\2\u00e8\u00e9\7f\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\32\3\2\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7n\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef\7g\2\2\u00ef\34")
        buf.write("\3\2\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7z\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6")
        buf.write("\7f\2\2\u00f6\u00f7\7u\2\2\u00f7\36\3\2\2\2\u00f8\u00f9")
        buf.write("\7h\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc")
        buf.write("\7c\2\2\u00fc\u00fd\7v\2\2\u00fd \3\2\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7h\2\2\u0100\"\3\2\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104\7v\2\2\u0104$\3")
        buf.write("\2\2\2\u0105\u0106\7p\2\2\u0106\u0107\7g\2\2\u0107\u0108")
        buf.write("\7y\2\2\u0108&\3\2\2\2\u0109\u010a\7u\2\2\u010a\u010b")
        buf.write("\7v\2\2\u010b\u010c\7t\2\2\u010c\u010d\7k\2\2\u010d\u010e")
        buf.write("\7p\2\2\u010e\u010f\7i\2\2\u010f(\3\2\2\2\u0110\u0111")
        buf.write("\7v\2\2\u0111\u0112\7j\2\2\u0112\u0113\7g\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114*\3\2\2\2\u0115\u0116\7h\2\2\u0116\u0117")
        buf.write("\7q\2\2\u0117\u0118\7t\2\2\u0118,\3\2\2\2\u0119\u011a")
        buf.write("\7t\2\2\u011a\u011b\7g\2\2\u011b\u011c\7v\2\2\u011c\u011d")
        buf.write("\7w\2\2\u011d\u011e\7t\2\2\u011e\u011f\7p\2\2\u011f.\3")
        buf.write("\2\2\2\u0120\u0121\7v\2\2\u0121\u0122\7t\2\2\u0122\u0123")
        buf.write("\7w\2\2\u0123\u0124\7g\2\2\u0124\60\3\2\2\2\u0125\u0126")
        buf.write("\7h\2\2\u0126\u0127\7c\2\2\u0127\u0128\7n\2\2\u0128\u0129")
        buf.write("\7u\2\2\u0129\u012a\7g\2\2\u012a\62\3\2\2\2\u012b\u012c")
        buf.write("\7x\2\2\u012c\u012d\7q\2\2\u012d\u012e\7k\2\2\u012e\u012f")
        buf.write("\7f\2\2\u012f\64\3\2\2\2\u0130\u0131\7p\2\2\u0131\u0132")
        buf.write("\7k\2\2\u0132\u0133\7n\2\2\u0133\66\3\2\2\2\u0134\u0135")
        buf.write("\7v\2\2\u0135\u0136\7j\2\2\u0136\u0137\7k\2\2\u0137\u0138")
        buf.write("\7u\2\2\u01388\3\2\2\2\u0139\u013a\7h\2\2\u013a\u013b")
        buf.write("\7k\2\2\u013b\u013c\7p\2\2\u013c\u013d\7c\2\2\u013d\u013e")
        buf.write("\7n\2\2\u013e:\3\2\2\2\u013f\u0140\7u\2\2\u0140\u0141")
        buf.write("\7v\2\2\u0141\u0142\7c\2\2\u0142\u0143\7v\2\2\u0143\u0144")
        buf.write("\7k\2\2\u0144\u0145\7e\2\2\u0145<\3\2\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147\u0148\7q\2\2\u0148>\3\2\2\2\u0149\u014a")
        buf.write("\7f\2\2\u014a\u014b\7q\2\2\u014b\u014c\7y\2\2\u014c\u014d")
        buf.write("\7p\2\2\u014d\u014e\7v\2\2\u014e\u014f\7q\2\2\u014f@\3")
        buf.write("\2\2\2\u0150\u0151\7-\2\2\u0151B\3\2\2\2\u0152\u0153\7")
        buf.write("/\2\2\u0153D\3\2\2\2\u0154\u0155\7,\2\2\u0155F\3\2\2\2")
        buf.write("\u0156\u0157\7)\2\2\u0157H\3\2\2\2\u0158\u0159\7\61\2")
        buf.write("\2\u0159J\3\2\2\2\u015a\u015b\7\'\2\2\u015bL\3\2\2\2\u015c")
        buf.write("\u015d\7#\2\2\u015d\u015e\7?\2\2\u015eN\3\2\2\2\u015f")
        buf.write("\u0160\7?\2\2\u0160\u0161\7?\2\2\u0161P\3\2\2\2\u0162")
        buf.write("\u0163\7>\2\2\u0163R\3\2\2\2\u0164\u0165\7@\2\2\u0165")
        buf.write("T\3\2\2\2\u0166\u0167\7>\2\2\u0167\u0168\7?\2\2\u0168")
        buf.write("V\3\2\2\2\u0169\u016a\7@\2\2\u016a\u016b\7?\2\2\u016b")
        buf.write("X\3\2\2\2\u016c\u016d\7~\2\2\u016d\u016e\7~\2\2\u016e")
        buf.write("Z\3\2\2\2\u016f\u0170\7(\2\2\u0170\u0171\7(\2\2\u0171")
        buf.write("\\\3\2\2\2\u0172\u0173\7#\2\2\u0173^\3\2\2\2\u0174\u0175")
        buf.write("\7`\2\2\u0175`\3\2\2\2\u0176\u0177\7<\2\2\u0177\u0178")
        buf.write("\7?\2\2\u0178b\3\2\2\2\u0179\u017a\7}\2\2\u017ad\3\2\2")
        buf.write("\2\u017b\u017c\7\177\2\2\u017cf\3\2\2\2\u017d\u017e\7")
        buf.write("*\2\2\u017eh\3\2\2\2\u017f\u0180\7+\2\2\u0180j\3\2\2\2")
        buf.write("\u0181\u0182\7]\2\2\u0182l\3\2\2\2\u0183\u0184\7_\2\2")
        buf.write("\u0184n\3\2\2\2\u0185\u0186\7=\2\2\u0186p\3\2\2\2\u0187")
        buf.write("\u0188\7<\2\2\u0188r\3\2\2\2\u0189\u018a\7\60\2\2\u018a")
        buf.write("t\3\2\2\2\u018b\u018c\7.\2\2\u018cv\3\2\2\2\u018d\u018f")
        buf.write("\5\3\2\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191x\3\2\2\2\u0192")
        buf.write("\u0194\5\3\2\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197\u0198\5{>\2\u0198z\3\2\2\2\u0199\u019a\5")
        buf.write("}?\2\u019a\u019b\5\177@\2\u019b\u019f\3\2\2\2\u019c\u019f")
        buf.write("\5}?\2\u019d\u019f\5\177@\2\u019e\u0199\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019f|\3\2\2\2\u01a0")
        buf.write("\u01a4\5s:\2\u01a1\u01a3\5\3\2\2\u01a2\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5~\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a9\t\6\2")
        buf.write("\2\u01a8\u01aa\5\u0081A\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01ad\5\3\2\2\u01ac")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u0080\3\2\2\2\u01b0\u01b1\t")
        buf.write("\7\2\2\u01b1\u0082\3\2\2\2\u01b2\u01b5\5/\30\2\u01b3\u01b5")
        buf.write("\5\61\31\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("\u0084\3\2\2\2\u01b6\u01b7\t\b\2\2\u01b7\u0086\3\2\2\2")
        buf.write("\u01b8\u0088\3\2\2\2\u01b9\u01bc\n\t\2\2\u01ba\u01bc\5")
        buf.write("\u0085C\2\u01bb\u01b9\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bc")
        buf.write("\u008a\3\2\2\2\u01bd\u01c1\7$\2\2\u01be\u01c0\5\u0089")
        buf.write("E\2\u01bf\u01be\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c4\u01c5\7$\2\2\u01c5\u008c\3\2\2\2")
        buf.write("\u01c6\u01c7\5c\62\2\u01c7\u01c9\5\u0091I\2\u01c8\u01ca")
        buf.write("\5\u008fH\2\u01c9\u01c8\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01cc\5e\63\2\u01cc\u008e\3\2\2\2")
        buf.write("\u01cd\u01ce\5u;\2\u01ce\u01cf\5\u0091I\2\u01cf\u01d0")
        buf.write("\5\u008fH\2\u01d0\u0090\3\2\2\2\u01d1\u01d6\5w<\2\u01d2")
        buf.write("\u01d6\5y=\2\u01d3\u01d6\5\u0083B\2\u01d4\u01d6\5\u008b")
        buf.write("F\2\u01d5\u01d1\3\2\2\2\u01d5\u01d2\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6\u0092\3\2\2\2\u01d7")
        buf.write("\u01d8\13\2\2\2\u01d8\u0094\3\2\2\2\u01d9\u01da\13\2\2")
        buf.write("\2\u01da\u0096\3\2\2\2\u01db\u01dc\13\2\2\2\u01dc\u0098")
        buf.write("\3\2\2\2\u01dd\u01de\13\2\2\2\u01de\u009a\3\2\2\2\24\2")
        buf.write("\u00a9\u00b5\u00b9\u00bf\u00c4\u00c6\u0190\u0195\u019e")
        buf.write("\u01a4\u01a9\u01ae\u01b4\u01bb\u01c1\u01c9\u01d5\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BLOCK_CMT = 2
    LINE_CMT = 3
    ID = 4
    BOOLEAN = 5
    BREAK = 6
    CLASS = 7
    CONTINUE = 8
    DO = 9
    ELSE = 10
    EXTENDS = 11
    FLOAT = 12
    IF = 13
    INT = 14
    NEW = 15
    STRING = 16
    THEN = 17
    FOR = 18
    RETURN = 19
    TRUE = 20
    FALSE = 21
    VOID = 22
    NIL = 23
    THIS = 24
    FINAL = 25
    STATIC = 26
    TO = 27
    DOWNTO = 28
    ADD = 29
    SUB = 30
    MUL = 31
    DIV = 32
    DIVF = 33
    MOD = 34
    NEQ = 35
    EQ = 36
    LESS = 37
    GREATER = 38
    LEQ = 39
    GREQ = 40
    OR = 41
    AND = 42
    NOT = 43
    CONCAT = 44
    ASSIGN = 45
    LP = 46
    RP = 47
    LB = 48
    RB = 49
    LQ = 50
    RQ = 51
    SEMI = 52
    COLON = 53
    DOT = 54
    COMMA = 55
    INTLIT = 56
    FLOATLIT = 57
    BOOLLIT = 58
    STRINGLIT = 59
    ARRAYLIT = 60
    LITLIST = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    UNTERMINATED_COMMENT = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'+'", "'-'", "'*'", "'''", "'/'", "'%'", "'!='", "'=='", "'<'", 
            "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", 
            "'{'", "'}'", "'('", "')'", "'['", "']'", "';'", "':'", "'.'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLOCK_CMT", "LINE_CMT", "ID", "BOOLEAN", "BREAK", "CLASS", 
            "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
            "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
            "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", 
            "MUL", "DIV", "DIVF", "MOD", "NEQ", "EQ", "LESS", "GREATER", 
            "LEQ", "GREQ", "OR", "AND", "NOT", "CONCAT", "ASSIGN", "LP", 
            "RP", "LB", "RB", "LQ", "RQ", "SEMI", "COLON", "DOT", "COMMA", 
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ARRAYLIT", "LITLIST", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "DIGIT", "CHAR", "WS", "BLOCK_CMT", "LINE_CMT", "ID", 
                  "UNDERSCORE", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                  "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
                  "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
                  "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD", 
                  "SUB", "MUL", "DIV", "DIVF", "MOD", "NEQ", "EQ", "LESS", 
                  "GREATER", "LEQ", "GREQ", "OR", "AND", "NOT", "CONCAT", 
                  "ASSIGN", "LP", "RP", "LB", "RB", "LQ", "RQ", "SEMI", 
                  "COLON", "DOT", "COMMA", "INTLIT", "FLOATLIT", "FLOAT_END", 
                  "DECPART", "EXPPART", "SIGN", "BOOLLIT", "ESCAPE", "DOUBLEQUOTES", 
                  "CHARS", "STRINGLIT", "ARRAYLIT", "LITLIST", "LITERAL", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


