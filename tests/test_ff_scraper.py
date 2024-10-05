from ffscraper import scraper
import unittest

class TestFFScraper(unittest.TestCase):
    def setUp(self):
        self.scrp = scraper.Scraper()
        
    def test_get_page_content(self):
        content = self.scrp.get_page_content()
        self.assertTrue(isinstance(content,str))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFFScraper)
    unittest.TextTestRunner(verbosity=2).run(suite)