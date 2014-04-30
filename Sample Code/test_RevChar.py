'''
Created on Apr 28, 2014

@author: Piyush Mittal
'''
import unittest
from RevChar import RevChar


class test_RevChar(unittest.TestCase):
    '''Runs tests for RevChar'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ValidInput(self):
        '''
        A valid input returns a valid output
        '''
        test_input = ['a', 'b', 'c', 'd', 'e']
        expected_output = ['E', 'd', 'c', 'b', 'A']
        output = RevChar(test_input).computeOutput()
        msg = 'Input %s \n Expected Output: %s \n Output: = %s' % (test_input, expected_output, output)
        self.assertEqual(expected_output, output, msg)

    def test_allvowels(self):
        '''
        all vowels (upper or lower) are converted to capital case
        '''
        test_input = ['A', 'e', 'I', 'o', 'u']
        expected_output = ['U', 'O', 'I', 'E', 'A']
        output = RevChar(test_input).computeOutput()
        msg = 'Input %s \n Expected Output: %s \n Output: = %s' % (test_input, expected_output, output)
        self.assertEqual(expected_output, output, msg)

    def test_allconsonants(self):
        '''
        all consonants (upper or lower) are returned lower
        '''
        test_input = ['B', 'F', 'G', 'h', 'j']
        expected_output = ['j', 'h', 'g', 'f', 'b']
        output = RevChar(test_input).computeOutput()
        msg = 'Input %s \n Expected Output: %s \n Output: = %s' % (test_input, expected_output, output)
        self.assertEqual(expected_output, output, msg)

    def test_InvalidInput_Integer(self):
        '''
        An invalid input (integer) returns None
        '''
        test_input = ['1', ]  # 1 is not a char
        expected_output = None
        output = RevChar(test_input).computeOutput()
        msg = 'Input %s \n Expected Output: %s \n Output: = %s' % (test_input, expected_output, output)
        self.assertEqual(expected_output, output, msg)

    def test_InvalidInput_String(self):
        '''
        An invalid input (String instead of char) returns None
        '''
        test_input = ['abc', 'a']  # abc is not a char, its a string
        expected_output = None
        output = RevChar(test_input).computeOutput()
        msg = 'Input %s \n Expected Output: %s \n Output: = %s' % (test_input, expected_output, output)
        self.assertEqual(expected_output, output, msg)


if __name__ == '__main__':
    unittest.main()
