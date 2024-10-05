from bs4 import BeautifulSoup

class Formatter:
    def __init__(self, page_content) -> None:
        self.page_content = page_content
        self.soup = BeautifulSoup(page_content, 'html.parser') #create soup
        self.find_currency_pairs()
        self.pair_infos = {}

    def find_currency_pairs(self):
        self.currency_pairs_container = self.soup.find('ul', class_='currencyPairUL')
        self.currency_pairs = self.currency_pairs_container.find_all('li')
    
    def create_pairs_dictonary(self):
        
        for pair in self.currency_pairs:
            
            pair_result = self.split_pair_change(pair.get_text(strip=True))
                    
            if pair_result:          
                self.pair_infos[pair_result[0]] = pair_result[1]
                
    def split_pair_change(self,pair):
        pair_name = ""
        pair_change = ""
        
        for i in range(len(pair)):
            if pair[i] == '+' or pair[i] == '-':
                pair_name = pair[:i]
                pair_change = pair[i:]
                
        if pair_name:
            return (pair_name,pair_change)
        else:
            return ()
    
    def get_pair_infos(self):
        return self.pair_infos