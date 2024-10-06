from bs4 import BeautifulSoup

class Formatter:
    """
    This class is responsible for filtering out the relevant data for all the news events on the page and storing them in a list as dictionaries.
    """
    
    
    def __init__(self, page_content) -> None:
        self.page_content = page_content
        self.soup = BeautifulSoup(self.page_content, features="lxml") #create soup
        self.find_events()
        self.row_infos = []
        
    def find_events(self):
        self.event_rows = self.soup.find_all('tr', class_='calendar__row')[1:] #get all the relevant rows, pop the first row as it contains no information.
        self.num_events = len(self.event_rows)
        
    def handle_all_events(self):
        if self.num_events == 0:
            return
        for i in range(self.num_events):
            processedRow = {}
            if self.row_infos:
                processedRow = self.process_row(self.event_rows[i],self.row_infos[-1]["time"])
            else:
                processedRow = self.process_row(self.event_rows[i],"No Time")
            if processedRow:
                self.row_infos.append(processedRow)
                
            #if multiple rows on forex factory have the same time in them, the time is omitted for the following rows. So to process those rows
            #we need to pass in the time in the previous row.
    
    def process_row(self,row,timePrev):
        
        row_info = {}
        
        impact = row.find('td', class_='calendar__impact').find('span')['title']
        if "Low" in impact: #if the impact is going to be low we are not interested in it.
            return {}
        
        time_element = row.find('td', class_='calendar__time')
        time = time_element.get_text(strip=True) if time_element.get_text(strip=True) != "" else timePrev
        
        currency = row.find('td', class_='calendar__currency').get_text(strip=True)
        
        event_name = row.find('td', class_='calendar__event').get_text(strip=True)
        
        row_info["time"] = time
        row_info["currency"] = currency
        row_info["impact"] = impact
        row_info["event_name"] = event_name
        
        return row_info
    
    def get_row_infos(self):
        return self.row_infos