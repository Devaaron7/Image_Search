import random
import requests
import unittest
from ImageApi_test import Connect



class TestSearchResults(unittest.TestCase):


    def test_ping_backend(self):
        url = "http://127.0.0.1:5000/wake"

        myobj = {"alarm": "wake up"}

        for runs in range(3):

            x = requests.post(url, json = myobj)

            actual = x.text
            expected = "awake"
            
            print("Actual: {}   Expected: {}".format(actual, expected))


            self.assertEqual(actual, expected)