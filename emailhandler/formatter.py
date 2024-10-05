from tabulate import tabulate
from datetime import date


class Formatter:
    
    SUBJECT_START = "Daily Financial News Report - "
    BODY_FF = "News that might affect the stock market:"
    BODY_FX = "Daily update for popular currencies:"
    
    def __init__(self,ff_data,fx_data) -> None:
        self.ff_data = ff_data
        self.fx_data = fx_data
        self.tabulate_ff_data()
        self.tabulate_fx_data()
        
    def tabulate_ff_data(self):
        headers = self.ff_data[0].keys()
        headers = [h.replace("_", " ") for h in headers]
        headers = [h.title() for h in headers]
        
        rows = [event.values() for event in self.ff_data]
        self.final_ff_data = tabulate(rows,headers,tablefmt='double_grid')
        
    def tabulate_fx_data(self):
        headers = ["Currency", "Daily Change"]
        rows = [[k,v] for (k,v) in self.fx_data.items()]
        
        self.final_fx_data = tabulate(rows,headers,tablefmt="double_grid")
        
    def generate_email_subject(self):
        today = date.today()
        formatted_date = today.strftime("%d/%m/%Y")
        self.subject = self.SUBJECT_START + formatted_date
        
    def generate_email_body(self):
        ff_body = self.BODY_FF + "\n" + self.final_ff_data
        margin = "\n\n"
        fx_body = self.BODY_FX + "\n" + self.final_fx_data
        
        self.body = ff_body + margin + fx_body
    
    def get_email_subject(self):
        return self.subject
    
    def get_email_body(self):
        return self.body
        
        
        