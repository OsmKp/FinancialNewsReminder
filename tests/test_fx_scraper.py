from fxscraper import scraper
import unittest
import requests

class TestFXScraper(unittest.TestCase):
    def setUp(self):
        self.scrp = scraper.Scraper()
        
    def test_get_page_content(self):
        content = self.scrp.get_page_content()
        self.assertTrue(isinstance(content,str))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFXScraper)
    unittest.TextTestRunner(verbosity=2).run(suite)