from fxscraper import formatter
import unittest
from pathlib import Path
from bs4 import BeautifulSoup

DATA_PATH = Path(__file__).parent / 'testdata' / 'fx_formatter_page_content.txt'




SPLIT_PAIR_CHANGE_TEST_DATA = "EUR/USD-0.51624%"



class TestFXFormatter(unittest.TestCase):
    def setUp(self):
        f = open(DATA_PATH,"r")
        page_content = f.read()
        f.close()
        
        self.frmt = formatter.Formatter(page_content)
        
    def test_find_currency_pairs(self):
        self.assertEqual(8,len(self.frmt.currency_pairs))
    
    def test_create_pairs_dictionary(self):
        self.frmt.create_pairs_dictonary()
        row_infos = self.frmt.get_pair_infos()
        self.assertEqual(8,len(row_infos))
        
    def test_split_pair_change(self):
        pair_result = self.frmt.split_pair_change(SPLIT_PAIR_CHANGE_TEST_DATA)
        self.assertEqual(("EUR/USD","-0.51624%"),pair_result)

        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFXFormatter)
    unittest.TextTestRunner(verbosity=2).run(suite)