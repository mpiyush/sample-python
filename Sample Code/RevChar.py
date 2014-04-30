'''
Created on Apr 28, 2014

@author: Piyush Mittal
'''
import sys
VOWELS = ['a', 'e', 'i', 'o', 'u']


class RevChar(object):

    def __init__(self, charList):
        '''
        Given a list of chars (valid input):
            * Reverses the list
            * Converts Consonants to lower
            * Converts Vowels to upper
        Given invalid input:
            * Prints sample usage and returns None
        '''
        self.charList = charList

    def _convertCase(self,):
        '''
        Given a list of chars
        Converts VOWELS to upper case and Consonants to lower case
        '''
        for i, achar in enumerate(self.charList):
            if achar.lower() in VOWELS:
                self.charList[i] = achar.upper()
            else:
                self.charList[i] = achar.lower()

    def _printUsage(self):
        '''
        Prints the usage of this program
        '''
        print "Sample Usage:\n python RevChar.py a b c d e A b f"

    def _validateInput(self,):
        '''
        Validates that the list of input provided is a list of chars
        '''
        if not self.charList:
            return False
        for achar in self.charList:
            if len(achar) != 1 or not achar.isalpha():
                return False
        return True

    def computeOutput(self,):
        '''
        Given a list of chars (valid input):
            * Reverses the list
            * Converts Consonants to lower
            * Converts Vowels to upper
        Given invalid input:
            * Prints sample usage and returns None
        '''
        if not self._validateInput():
            print "Invalid Input"
            self._printUsage()
            return None
        self.charList.reverse()
        self._convertCase()
        return self.charList

if __name__ == '__main__':
    output = RevChar(sys.argv[1:]).computeOutput()
    if output:
        print output

