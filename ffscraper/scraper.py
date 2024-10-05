import requests
import undetected_chromedriver as uc
from bs4 import BeautifulSoup

class Scraper:
    
    WEBSITE = "https://www.forexfactory.com/calendar?day=today"
    
    def __init__(self) -> None:
        self.chrome_options = uc.ChromeOptions()
        #self.chrome_options.add_argument("--start-maximized")
        self.chrome_driver = uc.Chrome(options=self.chrome_options)
        self.update_interceptor()
        
    def update_interceptor(self):
        self.chrome_driver.request_interceptor = self.interceptor


    def interceptor(request):
        request.headers["authority"] = "www.forexfactory.com"
        request.headers["method"] = "GET"
        request.headers["path"] = "/calendar?day=today"
        request.headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        request.headers["scheme"] = "https"
        request.headers["Accept-Encoding"] = "gzip, deflate, br, zstd"
        request.headers["Accept-Language"] = "en-US,en;q=0.9"
        request.headers["Cache-Control"] = "max-age=0"
        request.headers["Priority"] = "u=0, i"
        request.headers["Referer"] = "https://www.forexfactory.com/calendar?day=today"
        request.headers["Sec-Ch-Ua"] =  "Not/A)Brand";v="8", "Chromium";v="126", "Opera GX";v="112"
        request.headers["Sec-Ch-Ua-Mobile"] = "?0"
        request.headers["Sec-Ch-Ua-Platform"] = "Windows"
        request.headers["sec-fetch-dest"] = "document"
        request.headers["sec-fetch-mode"] = "navigate"
        request.headers["sec-fetch-site"] = "same-origin"
        request.headers["sec-fetch-user"] = "?1"
        request.headers["Upgrade-Insecure-Requests"] = "1"
        request.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0"


    def get_page_content(self):
        self.chrome_driver.get(self.WEBSITE)
        page_content = self.chrome_driver.page_source
        return page_content
        




    