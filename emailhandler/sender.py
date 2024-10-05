import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage

class Sender:
    def __init__(self,subject,body) -> None:
        load_dotenv()
        self.body = body
        self.subject = subject
        self.start_smtp_server()
        self.login_to_account()
        
    def start_smtp_server(self):
        self.server = smtplib.SMTP("smtp.gmail.com",587)
        self.server.starttls()
        
    def login_to_account(self):
        self.server.login(os.getenv('SENDER_EMAIL'),os.getenv('PASSWORD'))
        
    def make_body_html(self):
        html_body = '<font face="Courier New, Courier, monospace"><pre>' + self.body + "</pre></font>"
        return html_body
        
    def send_email(self):
        message = EmailMessage()
        message.set_content(self.make_body_html(),subtype='html')
        
        message['Subject'] = self.subject
        message['From'] = os.getenv('SENDER_EMAIL')
        message['To'] = os.getenv("RECEIVER_EMAIL")
        
        #message = ('<font face="Courier New, Courier, monospace"> ' + f"Subject: {self.subject}\n\n{self.body}" + '</font>').encode("utf-8")
        #print(message.decode("utf-8"))
        self.server.send_message(message)