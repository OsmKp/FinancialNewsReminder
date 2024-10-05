from emailhandler import formatter
import unittest

FF_DATA = [{"time":"1:00pm","currency":"USD","impact":"Medium Impact Expected", "event_name":"S&P/CS Composite-20 HPI y/y"},
           {"time":"2:00pm","currency":"USD","impact":"High Impact Expected", "event_name":"CB Consumer Confidence"},
           {"time":"2:00pm","currency":"USD","impact":"High Impact Expected", "event_name":"JOLTS Job Openings"}]

FX_DATA = {"EUR/USD":"+0.16111%","USD/JPY":"+0.04164%","GBP/USD":"+0.14648%","USD/CHF":"-0.15439%","USD/CAD":"-0.03122%","EUR/JPY":"+0.20282%","AUD/USD":"+0.20547%","CNY/USD":"0.00163%"}

FF_TABLE = """╔════════╦════════════╦════════════════════════╦═════════════════════════════╗
║ Time   ║ Currency   ║ Impact                 ║ Event Name                  ║
╠════════╬════════════╬════════════════════════╬═════════════════════════════╣
║ 1:00pm ║ USD        ║ Medium Impact Expected ║ S&P/CS Composite-20 HPI y/y ║
╠════════╬════════════╬════════════════════════╬═════════════════════════════╣
║ 2:00pm ║ USD        ║ High Impact Expected   ║ CB Consumer Confidence      ║
╠════════╬════════════╬════════════════════════╬═════════════════════════════╣
║ 2:00pm ║ USD        ║ High Impact Expected   ║ JOLTS Job Openings          ║
╚════════╩════════════╩════════════════════════╩═════════════════════════════╝"""

FX_TABLE = """╔════════════╦════════════════╗
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

class TestEmailFormatter(unittest.TestCase):
    def setUp(self):
        self.frmt = formatter.Formatter(FF_DATA,FX_DATA)
        
    def test_tabulate_ff_data(self):
        self.assertEqual(FF_TABLE,self.frmt.final_ff_data)
        
    def test_tabulate_fx_data(self):
        self.assertEqual(FX_TABLE,self.frmt.final_fx_data)
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmailFormatter)
    unittest.TextTestRunner(verbosity=2).run(suite)