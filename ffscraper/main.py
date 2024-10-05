import scraper
import formatter

scp = scraper.Scraper()
page_content = scp.get_page_content()


fmt = formatter.Formatter(page_content)
fmt.handle_all_events()

row_infos = fmt.get_row_infos()

for i in range(len(row_infos)):
    print(row_infos[i])
