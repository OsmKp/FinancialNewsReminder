from ffscraper import formatter
import unittest
from pathlib import Path
from bs4 import BeautifulSoup

DATA_PATH = Path(__file__).parent / 'testdata' / 'ff_formatter_page_content.txt'

PROCESS_ROW_YELLOW_TEST_DATA = """
<tr class="calendar__row" data-event-id="141577" data-touchable=""><!-- --> <td class="calendar__cell calendar__time"><div><!-- --> 
<!-- --><span>5:15pm</span></div></td> <td class="calendar__cell calendar__sub crunched nowrap"><div><a class="mini-sub mini-sub" href="/login" title="Subscribe to FOMC Member Barkin Speaks">
<span class="icon icon--mini-unsubscribed"></span></a> <!-- --> <!-- --></div></td> <td class="calendar__cell calendar__currency"><span class="">USD</span></td> <td class="calendar__cell calendar__impact">
<span class="icon icon--ff-impact-yel" title="Low Impact Expected"></span> <div class="calendar__impact-icon calendar__impact-icon--print"><img alt=""
height="12" src="https://resources.faireconomy.media/images/sprites/ff-impact-yel.png" width="14"/></div></td> <td class="calendar__cell calendar__event event" colspan="1">
<div><span class="calendar__event-title">FOMC Member Barkin Speaks</span></div></td> <!-- --> <td class="calendar__cell calendar__detail"><a class="calendar__detail-link calendar__detail-link--level-0"
title="Open Detail"></a></td> <td class="calendar__cell calendar__actual"><!-- --><!-- --><!-- --> <!-- --></td> <td class="calendar__cell calendar__forecast"><span>
</span></td> <td class="calendar__cell calendar__previous"><span></span></td> <td class="calendar__cell calendar__graph"><!-- --></td></tr>
"""

PROCESS_ROW_IMPORTANT_TEST_DATA = """
<tr class="calendar__row" data-event-id="137603" data-touchable=""><!-- --> <td class="calendar__cell calendar__time"><div><!-- --> 
<!-- --><span>3:30pm</span></div></td> <td class="calendar__cell calendar__sub crunched nowrap"><div><a class="mini-sub mini-sub" href="/login" 
title="Subscribe to Crude Oil Inventories"><span class="icon icon--mini-unsubscribed"></span></a> <!-- --> <!-- --></div></td> <td class="calendar__cell 
calendar__currency"><span class="">USD</span></td> <td class="calendar__cell calendar__impact"><span class="icon icon--ff-impact-ora" title="Medium Impact Expected">
</span> <div class="calendar__impact-icon calendar__impact-icon--print"><img alt="" height="12" src="https://resources.faireconomy.media/images/sprites/ff-impact-ora.png"
width="14"/></div></td> <td class="calendar__cell calendar__event event" colspan="1"><div><span class="calendar__event-title">Crude Oil Inventories</span></div></td>
<!-- --> <td class="calendar__cell calendar__detail"><a class="calendar__detail-link calendar__detail-link--level-0" title="Open Detail"></a></td>
<td class="calendar__cell calendar__actual"><!-- --><!-- --><!-- --> <!-- --></td> <td class="calendar__cell calendar__forecast"><span>-1.5M</span>
</td> <td class="calendar__cell calendar__previous"><span>-4.5M</span></td> <td class="calendar__cell calendar__graph">
<a class="calendar__detail-link calendar__detail-link--graph-icon" title="Open Graph"></a></td></tr>
"""


class TestFFFormatter(unittest.TestCase):
    def setUp(self):
        f = open(DATA_PATH,"r")
        page_content = f.read()
        f.close()
        
        self.frmt = formatter.Formatter(page_content)
        
    def test_find_events(self):
        self.assertEqual(18,self.frmt.num_events)
    
    def test_handle_all_events(self):
        self.frmt.handle_all_events()
        row_infos = self.frmt.get_row_infos()
        self.assertEqual(4,len(row_infos))
        
    def test_process_row_yellow(self):
        row_info = self.frmt.process_row(BeautifulSoup(PROCESS_ROW_YELLOW_TEST_DATA, features="lxml"),"3:30pm")
        self.assertFalse(row_info)
        
    def test_process_row_important(self):
        row_info = self.frmt.process_row(BeautifulSoup(PROCESS_ROW_IMPORTANT_TEST_DATA, features="lxml"),"1:15pm")
        self.assertEqual("3:30pm",row_info["time"])
        self.assertEqual("USD",row_info["currency"])
        self.assertEqual("Medium Impact Expected",row_info["impact"])
        self.assertEqual("Crude Oil Inventories",row_info["event_name"])
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFFFormatter)
    unittest.TextTestRunner(verbosity=2).run(suite)