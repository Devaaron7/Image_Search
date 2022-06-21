import random
import requests
import unittest
from UnsplashApi import Connect



#breakpoint()
class TestSearchResults(unittest.TestCase):

    def test_no_results(self):
        fake_words = ["apple", "goyance", "oshu", "skimat", "disacrucesser", "kerbardefeell", "apple", "fectiven", "iwart", "labarb", "quarropt", "ve", "lunasac"]

        breakpoint()
        for word in fake_words:

            session = Connect(word)

            session.start()

            if isinstance(session.start(), str) == True:
                actual = session.start()
                
                expected = "No results from your current search term. Please try another term"

                print("Search term is - {}. Actual: {}   Expected: {}".format(word, actual, expected))

                self.assertEqual(actual, expected)
            else:
                actual = "This is a valid search term"

                expected = "This is a valid search term"

                print("Search term is - {}. Actual: {}   Expected: {}".format(word, actual, expected))

                self.assertEqual(actual, expected)

            

        ## sessions lists received from the API shouldn't be empty if there is a return
        
    

