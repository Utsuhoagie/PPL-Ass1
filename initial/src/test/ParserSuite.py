import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """class A{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_multiline_program(self):
        """Program with multilines"""
        input = """
            class A {

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_multiClass_program(self):
        """Program with many classes"""
        input = """
            class A {

            }

            class B {

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_wrongBracketClass_program(self):
        
        input = """
            class A (

            }
        """
        expect = "Error on line 2 col 20: ("
        self.assertTrue(TestParser.test(input,expect,204))

    def test_classExtend_program(self):

        input = """
            class Dog extends Animal {

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_fullClass_program(self):

        input = """
            class Dog extends Animal {
                static int count = 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input,expect,203))