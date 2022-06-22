import random
import requests
import unittest
from UnsplashApi import Connect



class TestSearchResults(unittest.TestCase):


    def test_ping_backend(self):
        fake_words = ["apple", "goyance", "oshu", "skimat", "disacrucesser", "kerbardefeell", "apple", "fectiven", "iwart", "labarb", "quarropt", "ve", "lunasac"]

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





    def test_no_results(self):
        fake_words = ["apple", "goyance", "oshu", "skimat", "disacrucesser", "kerbardefeell", "apple", "fectiven", "iwart", "labarb", "quarropt", "ve", "lunasac"]

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

            

        
        
    

