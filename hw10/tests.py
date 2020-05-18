##make sure to import the modules we need in this file
##refer back to the lesson8 code for how to write unittests
##we want one unittest class for each function in debug.py
##make sure to write extensive test cases for each function inside the class
##also make sure each individual test's name starts with the word 'test'
##i.e we want a test to check the length of a function name it test_length
import unittest
import debug


class PosNumberTest(unittest.TestCase):
    def test_pos(self):
        self.assertEqual(debug.pos_number(3), True)

    def test_zero(self):
        self.assertEqual(debug.pos_number(0),True)

    def test_neg(self):
        self.assertEqual(debug.pos_number(-1), False )

    def test_pos_float(self):
        self.assertEqual(debug.pos_number(2.3), True)

    def test_neg_float_test(self):
        self.assertEqual(debug.pos_number(-2.3), False)


class OnlyPositivesTest(unittest.TestCase):
    def test_all_neg(self):
        self.assertEqual(debug.only_positives([-1,-2,-3]), [])
    def test_list_type(self):
        self.assertEqual(type(debug.only_positives([3,-1,6,-4])), list)


class SecondLetterPTest(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(IndexError):
            debug.second_letter_p("")

    def test_less_length_one(self):
        with self.assertRaises(IndexError):
            debug.second_letter_p("I")

    def test_length_greater_test(self):
        self.assertEqual(debug.second_letter_p("nice"), "npce")

    def test_with_p(self):
        self.assertEqual(debug.second_letter_p("apricot"), "apricot")
        
class RecursiveSumTest(unittest.TestCase):
    def test_list_empty(self):
        self.assertEqual(debug.recursive_sum([]),0)
    def test_one_num(self):
        self.assertEqual(debug.recursive_sum([11]), 11)
    def test_nested_empt(self):
        self.assertEqual(debug.recursive_sum([[],[]]), 0)
    def test_no_nests(self):
        self.assertEqual(debug.recursive_sum ([1,5,2,3]), 11)
    def test_with_nests(self):
         self.assertEqual(debug.recursive_sum([1, 2, [3,4], [6, [0,2]]]), 18)
            
class ListToDictsTest(unittest.TestCase):
    def test_value_words(self):
        self.assertEqual(debug.lists_to_dict(["strawberries", "clementines", "bananas"],["red", "orange", "yellow"]), {"strawberries":"red", "clementines":"orange", "bananas":"yellow"})
    def test_value_number(self):
        self.assertEqual(debug.lists_to_dict(["strawberries", "clementines", "bananas"],[3,7,8]), {"strawberries":3, "clementines": 7, "bananas":8})
    def test_empty_list(self):
        self.assertEqual(debug.lists_to_dict([1,2,3], []), {})
    def test_diff_lengths(self):
        self.assertEqual(debug.lists_to_dict(["strawberries", "clementines", "bananas"],[3,7,8,5,6]),  {"strawberries":3, "clementines": 7, "bananas":8})

                         

##don't have to do anything with this line
## it just ensures that your tests will run when you run this file
if __name__ == '__main__':
    unittest.main(exit=False)
