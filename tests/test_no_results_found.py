import random
import requests
import unittest
from UnsplashApi import Connect




class TestSearchResults(unittest.TestCase):

    def test_no_results(self):

        session = Connect()

        session.start()

        ## sessions lists received from the API shouldn't be empty if there is a return
        pass
    pass