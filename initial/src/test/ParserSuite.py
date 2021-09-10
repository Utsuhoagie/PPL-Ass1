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

    def test_classMem_program(self):

        input = """
            class Dog extends Animal {
                static int count = 0;

                void foo() {
                    this.count := 5;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_bigClass_program(self):

        input = """
            class Dog extends Animal {
                static int count = 0;
                int age;
                float height, weight;

                void addNew(int age; float height, weight) {
                    this.count := this.count + 1;
                    this.age := age;
                    this.height := height;
                    this.weight := weight;
                }

                int getCount() {
                    return this.count;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_2classes_program(self):

        input = """
            class Dog extends Animal {
                static int count = 0;

                int getCount() {
                    return this.count;
                }
            }

            class Person {
                int countDogs() {
                    return Dog.getCount();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_more_complex_program(self):
        """More complex program"""
        input = """
        class A {
            void foo() {
                int i, j = 0;
                for i := 0 to 5 do {
                    j := j + 2;
                    if j == 6 then
                        break;
                    else continue;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input,expect,203))