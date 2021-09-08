import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_varDecl(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("int a;","int,a,;,<EOF>",101))

    def test_separators(self):
        self.assertTrue(TestLexer.test("""{(]
            }""","{,(,],},<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.test("ab~svn","ab,Error Token ~",103))

    def test_string(self):
        self.assertTrue(TestLexer.test("""string a := "th\ting";""", """string,a,:=,"th\ting",;,<EOF>""", 104))

    def test_class(self):
        self.assertTrue(TestLexer.test("""class""","class,<EOF>", 105))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("Var x;","Var,x,;,<EOF>",104))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.test(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.test(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.test(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

