from emailhandler import sender
import unittest

SUBJECT = "TEST"
BODY = """News that might affect the stock market:\n╔════════╦════════════╦════════════════════════╦═════════════════════════════╗
║ Time   ║ Currency   ║ Impact                 ║ Event Name                  ║
╠════════╬════════════╬════════════════════════╬═════════════════════════════╣
║ 1:00pm ║ USD        ║ Medium Impact Expected ║ S&P/CS Composite-20 HPI y/y ║
╠════════╬════════════╬════════════════════════╬═════════════════════════════╣
║ 2:00pm ║ USD        ║ High Impact Expected   ║ CB Consumer Confidence      ║
╠════════╬════════════╬════════════════════════╬═════════════════════════════╣
║ 2:00pm ║ USD        ║ High Impact Expected   ║ JOLTS Job Openings          ║
╚════════╩════════════╩════════════════════════╩═════════════════════════════╝\n\nDaily update for popular currencies:\n╔════════════╦════════════════╗
║ Currency   ║ Daily Change   ║
╠════════════╬════════════════╣
║ EUR/USD    ║ +0.16111%      ║
╠════════════╬════════════════╣
║ USD/JPY    ║ +0.04164%      ║
╠════════════╬════════════════╣
║ GBP/USD    ║ +0.14648%      ║
╠════════════╬════════════════╣
║ USD/CHF    ║ -0.15439%      ║
╠════════════╬════════════════╣
║ USD/CAD    ║ -0.03122%      ║
╠════════════╬════════════════╣
║ EUR/JPY    ║ +0.20282%      ║
╠════════════╬════════════════╣
║ AUD/USD    ║ +0.20547%      ║
╠════════════╬════════════════╣
║ CNY/USD    ║ 0.00163%       ║
╚════════════╩════════════════╝"""

HTML_BODY = """<font face="Courier New, Courier, monospace"><pre>News that might affect the stock market:\n╔════════╦════════════╦════════════════════════╦═════════════════════════════╗
║ Time   ║ Currency   ║ Impact                 ║ Event Name                  ║
╠════════╬════════════╬════════════════════════╬═════════════════════════════╣
║ 1:00pm ║ USD        ║ Medium Impact Expected ║ S&P/CS Composite-20 HPI y/y ║
╠════════╬════════════╬════════════════════════╬═════════════════════════════╣
║ 2:00pm ║ USD        ║ High Impact Expected   ║ CB Consumer Confidence      ║
╠════════╬════════════╬════════════════════════╬═════════════════════════════╣
║ 2:00pm ║ USD        ║ High Impact Expected   ║ JOLTS Job Openings          ║
╚════════╩════════════╩════════════════════════╩═════════════════════════════╝\n\nDaily update for popular currencies:\n╔════════════╦════════════════╗
║ Currency   ║ Daily Change   ║
╠════════════╬════════════════╣
║ EUR/USD    ║ +0.16111%      ║
╠════════════╬════════════════╣
║ USD/JPY    ║ +0.04164%      ║
╠════════════╬════════════════╣
║ GBP/USD    ║ +0.14648%      ║
╠════════════╬════════════════╣
║ USD/CHF    ║ -0.15439%      ║
╠════════════╬════════════════╣
║ USD/CAD    ║ -0.03122%      ║
╠════════════╬════════════════╣
║ EUR/JPY    ║ +0.20282%      ║
╠════════════╬════════════════╣
║ AUD/USD    ║ +0.20547%      ║
╠════════════╬════════════════╣
║ CNY/USD    ║ 0.00163%       ║
╚════════════╩════════════════╝</pre></font>"""

class TestEmailSender(unittest.TestCase):
    def setUp(self):
        self.sender = sender.Sender(SUBJECT,BODY)
        
    def test_make_body_html(self):
        result = self.sender.make_body_html()
        self.assertEqual(result,HTML_BODY)
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmailSender)
    unittest.TextTestRunner(verbosity=2).run(suite)