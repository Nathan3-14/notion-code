import smtplib
from rich import print
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

usrpass = open("./s--pswd.txt", "r").readlines()
gmail_user = usrpass[0].strip()
gmail_app_password = usrpass[1].strip()

sent_from = gmail_user
sent_to = "ethan.denton@oasisbrislington.org"
# sent_to = "nathan.watson@oasisbrislington.org"

message = MIMEMultipart("alternative")
message["Subject"] = "Cat?"
message["From"] = sent_from
message["To"] = sent_to
with open("email.html", "r") as f:
    html = f.read()

html_part = MIMEText(html, "html")
message.attach(html_part)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

server.login(gmail_user, gmail_app_password)
print(f"[bright_green bold]Logged in as {gmail_user}[/bright_green bold]")

server.sendmail(sent_from, sent_to, message.as_string())
print(f"[bright_cyan]Sent email to {sent_to}[/bright_cyan]")

server.close()

