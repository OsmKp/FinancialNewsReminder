import requests
import undetected_chromedriver as uc

class Scraper:
    
    WEBSITE = "https://www.x-rates.com"
    
    def get_page_content(self):
        page_content = requests.get(self.WEBSITE)
        return page_content.text
    