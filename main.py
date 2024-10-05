import emailhandler
import emailhandler.formatter
import emailhandler.sender
import ffscraper
import ffscraper.formatter
import ffscraper.scraper
import fxscraper
import fxscraper.scraper
import fxscraper.formatter

from tabulate import tabulate

ff_scraper = ffscraper.scraper.Scraper()
ff_page_content = ff_scraper.get_page_content()
ff_formatter = ffscraper.formatter.Formatter(ff_page_content)
ff_formatter.handle_all_events()
ff_data = ff_formatter.get_row_infos()

fx_scraper = fxscraper.scraper.Scraper()
fx_page_content = fx_scraper.get_page_content()
fx_formatter = fxscraper.formatter.Formatter(fx_page_content)
fx_formatter.create_pairs_dictonary()
fx_data = fx_formatter.get_pair_infos()

email_formatter = emailhandler.formatter.Formatter(ff_data,fx_data)
email_formatter.generate_email_body()
email_formatter.generate_email_subject()
email_subject = email_formatter.get_email_subject()
email_body = email_formatter.get_email_body()

email_sender = emailhandler.sender.Sender(email_subject,email_body)
email_sender.send_email()

