# Generated from e:\Study\Sem7\PPL\Assignment\A1\Third Test A1, changing ANTLR\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0201\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\3\2\3\2\3\2\5\2\u00a1\n\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u00af\n\6\f\6")
        buf.write("\16\6\u00b2\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\7\7\u00bb")
        buf.write("\n\7\f\7\16\7\u00be\13\7\3\7\5\7\u00c1\n\7\3\7\3\7\3\b")
        buf.write("\3\b\5\b\u00c7\n\b\3\b\3\b\3\b\7\b\u00cc\n\b\f\b\16\b")
        buf.write("\u00cf\13\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\6=\u0196")
        buf.write("\n=\r=\16=\u0197\3>\6>\u019b\n>\r>\16>\u019c\3>\3>\3?")
        buf.write("\3?\3?\3?\3?\5?\u01a6\n?\3@\3@\7@\u01aa\n@\f@\16@\u01ad")
        buf.write("\13@\3A\3A\5A\u01b1\nA\3A\6A\u01b4\nA\rA\16A\u01b5\3B")
        buf.write("\3B\3C\3C\5C\u01bc\nC\3D\3D\3E\3E\3E\3F\3F\3F\3F\5F\u01c7")
        buf.write("\nF\3G\3G\7G\u01cb\nG\fG\16G\u01ce\13G\3G\3G\3H\3H\3H")
        buf.write("\3H\3H\3H\3H\3H\3H\5H\u01db\nH\3I\3I\3I\3I\3I\3I\3I\5")
        buf.write("I\u01e4\nI\3J\3J\3J\3J\5J\u01ea\nJ\3K\3K\3K\3L\3L\7L\u01f1")
        buf.write("\nL\fL\16L\u01f4\13L\3L\3L\3M\3M\7M\u01fa\nM\fM\16M\u01fd")
        buf.write("\13M\3M\3M\3M\4\u00b0\u00bc\2N\3\3\5\2\7\2\t\4\13\5\r")
        buf.write("\6\17\7\21\2\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17")
        buf.write("#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\32")
        buf.write("9\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a")
        buf.write("/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}\2\177\2\u0081")
        buf.write("\2\u0083\2\u0085=\u0087\2\u0089\2\u008b\2\u008d>\u008f")
        buf.write("?\u0091@\u0093\2\u0095A\u0097B\u0099C\3\2\13\3\2\62;\4")
        buf.write("\2C\\c|\5\2\13\f\16\17\"\"\3\3\f\f\4\2GGgg\4\2--//\5\2")
        buf.write("\n\13\16\17^^\b\2$$^^ddhhttvv\4\2\f\f$$\2\u020e\2\3\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2\u0085\3\2\2\2\2\u008d\3\2\2\2")
        buf.write("\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\3\u00a0\3\2\2\2\5\u00a2\3\2\2")
        buf.write("\2\7\u00a4\3\2\2\2\t\u00a6\3\2\2\2\13\u00aa\3\2\2\2\r")
        buf.write("\u00b8\3\2\2\2\17\u00c6\3\2\2\2\21\u00d0\3\2\2\2\23\u00d2")
        buf.write("\3\2\2\2\25\u00da\3\2\2\2\27\u00e0\3\2\2\2\31\u00e6\3")
        buf.write("\2\2\2\33\u00ef\3\2\2\2\35\u00f2\3\2\2\2\37\u00f7\3\2")
        buf.write("\2\2!\u00ff\3\2\2\2#\u0105\3\2\2\2%\u0108\3\2\2\2\'\u010c")
        buf.write("\3\2\2\2)\u0110\3\2\2\2+\u0117\3\2\2\2-\u011c\3\2\2\2")
        buf.write("/\u0120\3\2\2\2\61\u0127\3\2\2\2\63\u012c\3\2\2\2\65\u0132")
        buf.write("\3\2\2\2\67\u0137\3\2\2\29\u013b\3\2\2\2;\u0140\3\2\2")
        buf.write("\2=\u0146\3\2\2\2?\u014d\3\2\2\2A\u0150\3\2\2\2C\u0157")
        buf.write("\3\2\2\2E\u0159\3\2\2\2G\u015b\3\2\2\2I\u015d\3\2\2\2")
        buf.write("K\u015f\3\2\2\2M\u0161\3\2\2\2O\u0163\3\2\2\2Q\u0166\3")
        buf.write("\2\2\2S\u0169\3\2\2\2U\u016b\3\2\2\2W\u016d\3\2\2\2Y\u0170")
        buf.write("\3\2\2\2[\u0173\3\2\2\2]\u0176\3\2\2\2_\u0179\3\2\2\2")
        buf.write("a\u017b\3\2\2\2c\u017d\3\2\2\2e\u0180\3\2\2\2g\u0182\3")
        buf.write("\2\2\2i\u0184\3\2\2\2k\u0186\3\2\2\2m\u0188\3\2\2\2o\u018a")
        buf.write("\3\2\2\2q\u018c\3\2\2\2s\u018e\3\2\2\2u\u0190\3\2\2\2")
        buf.write("w\u0192\3\2\2\2y\u0195\3\2\2\2{\u019a\3\2\2\2}\u01a5\3")
        buf.write("\2\2\2\177\u01a7\3\2\2\2\u0081\u01ae\3\2\2\2\u0083\u01b7")
        buf.write("\3\2\2\2\u0085\u01bb\3\2\2\2\u0087\u01bd\3\2\2\2\u0089")
        buf.write("\u01bf\3\2\2\2\u008b\u01c6\3\2\2\2\u008d\u01c8\3\2\2\2")
        buf.write("\u008f\u01da\3\2\2\2\u0091\u01e3\3\2\2\2\u0093\u01e9\3")
        buf.write("\2\2\2\u0095\u01eb\3\2\2\2\u0097\u01ee\3\2\2\2\u0099\u01f7")
        buf.write("\3\2\2\2\u009b\u009c\5\17\b\2\u009c\u009d\5w<\2\u009d")
        buf.write("\u009e\5\3\2\2\u009e\u00a1\3\2\2\2\u009f\u00a1\5\17\b")
        buf.write("\2\u00a0\u009b\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\4\3\2")
        buf.write("\2\2\u00a2\u00a3\t\2\2\2\u00a3\6\3\2\2\2\u00a4\u00a5\t")
        buf.write("\3\2\2\u00a5\b\3\2\2\2\u00a6\u00a7\t\4\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00a9\b\5\2\2\u00a9\n\3\2\2\2\u00aa\u00ab")
        buf.write("\7\61\2\2\u00ab\u00ac\7,\2\2\u00ac\u00b0\3\2\2\2\u00ad")
        buf.write("\u00af\13\2\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2")
        buf.write("\2\u00b0\u00b1\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b3")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\7,\2\2\u00b4")
        buf.write("\u00b5\7\61\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\b\6\2")
        buf.write("\2\u00b7\f\3\2\2\2\u00b8\u00bc\7%\2\2\u00b9\u00bb\13\2")
        buf.write("\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00bd")
        buf.write("\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00bf\u00c1\t\5\2\2\u00c0\u00bf\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\u00c3\b\7\2\2\u00c3\16\3\2")
        buf.write("\2\2\u00c4\u00c7\5\7\4\2\u00c5\u00c7\5\21\t\2\u00c6\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00cd\3\2\2\2\u00c8")
        buf.write("\u00cc\5\7\4\2\u00c9\u00cc\5\5\3\2\u00ca\u00cc\5\21\t")
        buf.write("\2\u00cb\u00c8\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\20\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0")
        buf.write("\u00d1\7a\2\2\u00d1\22\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3")
        buf.write("\u00d4\7q\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7n\2\2\u00d6")
        buf.write("\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7p\2\2\u00d9")
        buf.write("\24\3\2\2\2\u00da\u00db\7d\2\2\u00db\u00dc\7t\2\2\u00dc")
        buf.write("\u00dd\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7m\2\2\u00df")
        buf.write("\26\3\2\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2\7n\2\2\u00e2")
        buf.write("\u00e3\7c\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5\7u\2\2\u00e5")
        buf.write("\30\3\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8\7q\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb")
        buf.write("\u00ec\7p\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee\7g\2\2\u00ee")
        buf.write("\32\3\2\2\2\u00ef\u00f0\7f\2\2\u00f0\u00f1\7q\2\2\u00f1")
        buf.write("\34\3\2\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7n\2\2\u00f4")
        buf.write("\u00f5\7u\2\2\u00f5\u00f6\7g\2\2\u00f6\36\3\2\2\2\u00f7")
        buf.write("\u00f8\7g\2\2\u00f8\u00f9\7z\2\2\u00f9\u00fa\7v\2\2\u00fa")
        buf.write("\u00fb\7g\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7f\2\2\u00fd")
        buf.write("\u00fe\7u\2\2\u00fe \3\2\2\2\u00ff\u0100\7h\2\2\u0100")
        buf.write("\u0101\7n\2\2\u0101\u0102\7q\2\2\u0102\u0103\7c\2\2\u0103")
        buf.write("\u0104\7v\2\2\u0104\"\3\2\2\2\u0105\u0106\7k\2\2\u0106")
        buf.write("\u0107\7h\2\2\u0107$\3\2\2\2\u0108\u0109\7k\2\2\u0109")
        buf.write("\u010a\7p\2\2\u010a\u010b\7v\2\2\u010b&\3\2\2\2\u010c")
        buf.write("\u010d\7p\2\2\u010d\u010e\7g\2\2\u010e\u010f\7y\2\2\u010f")
        buf.write("(\3\2\2\2\u0110\u0111\7u\2\2\u0111\u0112\7v\2\2\u0112")
        buf.write("\u0113\7t\2\2\u0113\u0114\7k\2\2\u0114\u0115\7p\2\2\u0115")
        buf.write("\u0116\7i\2\2\u0116*\3\2\2\2\u0117\u0118\7v\2\2\u0118")
        buf.write("\u0119\7j\2\2\u0119\u011a\7g\2\2\u011a\u011b\7p\2\2\u011b")
        buf.write(",\3\2\2\2\u011c\u011d\7h\2\2\u011d\u011e\7q\2\2\u011e")
        buf.write("\u011f\7t\2\2\u011f.\3\2\2\2\u0120\u0121\7t\2\2\u0121")
        buf.write("\u0122\7g\2\2\u0122\u0123\7v\2\2\u0123\u0124\7w\2\2\u0124")
        buf.write("\u0125\7t\2\2\u0125\u0126\7p\2\2\u0126\60\3\2\2\2\u0127")
        buf.write("\u0128\7v\2\2\u0128\u0129\7t\2\2\u0129\u012a\7w\2\2\u012a")
        buf.write("\u012b\7g\2\2\u012b\62\3\2\2\2\u012c\u012d\7h\2\2\u012d")
        buf.write("\u012e\7c\2\2\u012e\u012f\7n\2\2\u012f\u0130\7u\2\2\u0130")
        buf.write("\u0131\7g\2\2\u0131\64\3\2\2\2\u0132\u0133\7x\2\2\u0133")
        buf.write("\u0134\7q\2\2\u0134\u0135\7k\2\2\u0135\u0136\7f\2\2\u0136")
        buf.write("\66\3\2\2\2\u0137\u0138\7p\2\2\u0138\u0139\7k\2\2\u0139")
        buf.write("\u013a\7n\2\2\u013a8\3\2\2\2\u013b\u013c\7v\2\2\u013c")
        buf.write("\u013d\7j\2\2\u013d\u013e\7k\2\2\u013e\u013f\7u\2\2\u013f")
        buf.write(":\3\2\2\2\u0140\u0141\7h\2\2\u0141\u0142\7k\2\2\u0142")
        buf.write("\u0143\7p\2\2\u0143\u0144\7c\2\2\u0144\u0145\7n\2\2\u0145")
        buf.write("<\3\2\2\2\u0146\u0147\7u\2\2\u0147\u0148\7v\2\2\u0148")
        buf.write("\u0149\7c\2\2\u0149\u014a\7v\2\2\u014a\u014b\7k\2\2\u014b")
        buf.write("\u014c\7e\2\2\u014c>\3\2\2\2\u014d\u014e\7v\2\2\u014e")
        buf.write("\u014f\7q\2\2\u014f@\3\2\2\2\u0150\u0151\7f\2\2\u0151")
        buf.write("\u0152\7q\2\2\u0152\u0153\7y\2\2\u0153\u0154\7p\2\2\u0154")
        buf.write("\u0155\7v\2\2\u0155\u0156\7q\2\2\u0156B\3\2\2\2\u0157")
        buf.write("\u0158\7-\2\2\u0158D\3\2\2\2\u0159\u015a\7/\2\2\u015a")
        buf.write("F\3\2\2\2\u015b\u015c\7,\2\2\u015cH\3\2\2\2\u015d\u015e")
        buf.write("\7)\2\2\u015eJ\3\2\2\2\u015f\u0160\7\61\2\2\u0160L\3\2")
        buf.write("\2\2\u0161\u0162\7\'\2\2\u0162N\3\2\2\2\u0163\u0164\7")
        buf.write("#\2\2\u0164\u0165\7?\2\2\u0165P\3\2\2\2\u0166\u0167\7")
        buf.write("?\2\2\u0167\u0168\7?\2\2\u0168R\3\2\2\2\u0169\u016a\7")
        buf.write(">\2\2\u016aT\3\2\2\2\u016b\u016c\7@\2\2\u016cV\3\2\2\2")
        buf.write("\u016d\u016e\7>\2\2\u016e\u016f\7?\2\2\u016fX\3\2\2\2")
        buf.write("\u0170\u0171\7@\2\2\u0171\u0172\7?\2\2\u0172Z\3\2\2\2")
        buf.write("\u0173\u0174\7~\2\2\u0174\u0175\7~\2\2\u0175\\\3\2\2\2")
        buf.write("\u0176\u0177\7(\2\2\u0177\u0178\7(\2\2\u0178^\3\2\2\2")
        buf.write("\u0179\u017a\7#\2\2\u017a`\3\2\2\2\u017b\u017c\7`\2\2")
        buf.write("\u017cb\3\2\2\2\u017d\u017e\7<\2\2\u017e\u017f\7?\2\2")
        buf.write("\u017fd\3\2\2\2\u0180\u0181\7}\2\2\u0181f\3\2\2\2\u0182")
        buf.write("\u0183\7\177\2\2\u0183h\3\2\2\2\u0184\u0185\7*\2\2\u0185")
        buf.write("j\3\2\2\2\u0186\u0187\7+\2\2\u0187l\3\2\2\2\u0188\u0189")
        buf.write("\7]\2\2\u0189n\3\2\2\2\u018a\u018b\7_\2\2\u018bp\3\2\2")
        buf.write("\2\u018c\u018d\7=\2\2\u018dr\3\2\2\2\u018e\u018f\7<\2")
        buf.write("\2\u018ft\3\2\2\2\u0190\u0191\7\60\2\2\u0191v\3\2\2\2")
        buf.write("\u0192\u0193\7.\2\2\u0193x\3\2\2\2\u0194\u0196\5\5\3\2")
        buf.write("\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195\3")
        buf.write("\2\2\2\u0197\u0198\3\2\2\2\u0198z\3\2\2\2\u0199\u019b")
        buf.write("\5\5\3\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u019f\5}?\2\u019f|\3\2\2\2\u01a0\u01a1\5\177@\2")
        buf.write("\u01a1\u01a2\5\u0081A\2\u01a2\u01a6\3\2\2\2\u01a3\u01a6")
        buf.write("\5\177@\2\u01a4\u01a6\5\u0081A\2\u01a5\u01a0\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6~\3\2\2\2\u01a7")
        buf.write("\u01ab\5u;\2\u01a8\u01aa\5\5\3\2\u01a9\u01a8\3\2\2\2\u01aa")
        buf.write("\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ac\u0080\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01b0\t")
        buf.write("\6\2\2\u01af\u01b1\5\u0083B\2\u01b0\u01af\3\2\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01b4\5\5\3\2")
        buf.write("\u01b3\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b3\3")
        buf.write("\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u0082\3\2\2\2\u01b7\u01b8")
        buf.write("\t\7\2\2\u01b8\u0084\3\2\2\2\u01b9\u01bc\5\61\31\2\u01ba")
        buf.write("\u01bc\5\63\32\2\u01bb\u01b9\3\2\2\2\u01bb\u01ba\3\2\2")
        buf.write("\2\u01bc\u0086\3\2\2\2\u01bd\u01be\t\b\2\2\u01be\u0088")
        buf.write("\3\2\2\2\u01bf\u01c0\7^\2\2\u01c0\u01c1\n\t\2\2\u01c1")
        buf.write("\u008a\3\2\2\2\u01c2\u01c7\n\n\2\2\u01c3\u01c7\5\u0087")
        buf.write("D\2\u01c4\u01c5\7^\2\2\u01c5\u01c7\7$\2\2\u01c6\u01c2")
        buf.write("\3\2\2\2\u01c6\u01c3\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7")
        buf.write("\u008c\3\2\2\2\u01c8\u01cc\7$\2\2\u01c9\u01cb\5\u008b")
        buf.write("F\2\u01ca\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01cf\u01d0\7$\2\2\u01d0\u008e\3\2\2\2")
        buf.write("\u01d1\u01d2\5e\63\2\u01d2\u01d3\5\u0093J\2\u01d3\u01d4")
        buf.write("\5\u0091I\2\u01d4\u01d5\5g\64\2\u01d5\u01db\3\2\2\2\u01d6")
        buf.write("\u01d7\5e\63\2\u01d7\u01d8\5\u0093J\2\u01d8\u01d9\5g\64")
        buf.write("\2\u01d9\u01db\3\2\2\2\u01da\u01d1\3\2\2\2\u01da\u01d6")
        buf.write("\3\2\2\2\u01db\u0090\3\2\2\2\u01dc\u01dd\5w<\2\u01dd\u01de")
        buf.write("\5\u0093J\2\u01de\u01df\5\u0091I\2\u01df\u01e4\3\2\2\2")
        buf.write("\u01e0\u01e1\5w<\2\u01e1\u01e2\5\u0093J\2\u01e2\u01e4")
        buf.write("\3\2\2\2\u01e3\u01dc\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e4")
        buf.write("\u0092\3\2\2\2\u01e5\u01ea\5y=\2\u01e6\u01ea\5{>\2\u01e7")
        buf.write("\u01ea\5\u0085C\2\u01e8\u01ea\5\u008dG\2\u01e9\u01e5\3")
        buf.write("\2\2\2\u01e9\u01e6\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8")
        buf.write("\3\2\2\2\u01ea\u0094\3\2\2\2\u01eb\u01ec\13\2\2\2\u01ec")
        buf.write("\u01ed\bK\3\2\u01ed\u0096\3\2\2\2\u01ee\u01f2\7$\2\2\u01ef")
        buf.write("\u01f1\5\u008bF\2\u01f0\u01ef\3\2\2\2\u01f1\u01f4\3\2")
        buf.write("\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f5")
        buf.write("\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f6\bL\4\2\u01f6")
        buf.write("\u0098\3\2\2\2\u01f7\u01fb\7$\2\2\u01f8\u01fa\5\u008b")
        buf.write("F\2\u01f9\u01f8\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fe\3\2\2\2\u01fd")
        buf.write("\u01fb\3\2\2\2\u01fe\u01ff\5\u0089E\2\u01ff\u0200\bM\5")
        buf.write("\2\u0200\u009a\3\2\2\2\30\2\u00a0\u00b0\u00bc\u00c0\u00c6")
        buf.write("\u00cb\u00cd\u0197\u019c\u01a5\u01ab\u01b0\u01b5\u01bb")
        buf.write("\u01c6\u01cc\u01da\u01e3\u01e9\u01f2\u01fb\6\b\2\2\3K")
        buf.write("\2\3L\3\3M\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDList = 1
    WS = 2
    BLOCK_CMT = 3
    LINE_CMT = 4
    ID = 5
    BOOLEAN = 6
    BREAK = 7
    CLASS = 8
    CONTINUE = 9
    DO = 10
    ELSE = 11
    EXTENDS = 12
    FLOAT = 13
    IF = 14
    INT = 15
    NEW = 16
    STRING = 17
    THEN = 18
    FOR = 19
    RETURN = 20
    TRUE = 21
    FALSE = 22
    VOID = 23
    NIL = 24
    THIS = 25
    FINAL = 26
    STATIC = 27
    TO = 28
    DOWNTO = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    DIVF = 34
    MOD = 35
    NEQ = 36
    EQ = 37
    LESS = 38
    GREATER = 39
    LEQ = 40
    GREQ = 41
    OR = 42
    AND = 43
    NOT = 44
    CONCAT = 45
    ASSIGN = 46
    LP = 47
    RP = 48
    LB = 49
    RB = 50
    LQ = 51
    RQ = 52
    SEMI = 53
    COLON = 54
    DOT = 55
    COMMA = 56
    INTLIT = 57
    FLOATLIT = 58
    BOOLLIT = 59
    STRINGLIT = 60
    ARRAYLIT = 61
    LITLIST = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65

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
            "IDList", "WS", "BLOCK_CMT", "LINE_CMT", "ID", "BOOLEAN", "BREAK", 
            "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", 
            "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
            "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD", 
            "SUB", "MUL", "DIV", "DIVF", "MOD", "NEQ", "EQ", "LESS", "GREATER", 
            "LEQ", "GREQ", "OR", "AND", "NOT", "CONCAT", "ASSIGN", "LP", 
            "RP", "LB", "RB", "LQ", "RQ", "SEMI", "COLON", "DOT", "COMMA", 
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ARRAYLIT", "LITLIST", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IDList", "DIGIT", "CHAR", "WS", "BLOCK_CMT", "LINE_CMT", 
                  "ID", "UNDERSCORE", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                  "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
                  "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
                  "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD", 
                  "SUB", "MUL", "DIV", "DIVF", "MOD", "NEQ", "EQ", "LESS", 
                  "GREATER", "LEQ", "GREQ", "OR", "AND", "NOT", "CONCAT", 
                  "ASSIGN", "LP", "RP", "LB", "RB", "LQ", "RQ", "SEMI", 
                  "COLON", "DOT", "COMMA", "INTLIT", "FLOATLIT", "FLOAT_END", 
                  "DECPART", "EXPPART", "SIGN", "BOOLLIT", "ESCAPE", "ILLEGAL_ESC", 
                  "CHARS", "STRINGLIT", "ARRAYLIT", "LITLIST", "LITERAL", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
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
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.UNCLOSE_STRING_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     


