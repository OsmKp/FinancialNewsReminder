import requests
import undetected_chromedriver as uc

class Scraper:
    
    """
    This class is responsible for connecting to x-rates and getting the contents of the page.
    
    This is done with a simple HTTP request.
    """
    
    WEBSITE = "https://www.x-rates.com"
    
    def get_page_content(self):
        page_content = requests.get(self.WEBSITE)
        return page_content.text
    