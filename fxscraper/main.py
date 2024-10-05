import scraper
import formatter

scp = scraper.Scraper()
page_content = scp.get_page_content()

fmt = formatter.Formatter(page_content)
fmt.create_pairs_dictonary()

pair_infos = fmt.get_pair_infos()

for key, value in pair_infos.items():
    print(f"{key}: {value}")