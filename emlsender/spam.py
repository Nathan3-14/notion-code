import smtplib
from rich import print

usrpass = open("./s--pswd.txt", "r").readlines()
gmail_user = usrpass[0].strip()
gmail_app_password = usrpass[1].strip()


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

sent_from = gmail_user
sent_to = "nathan.watson@oasisbrislington.org"


server.login(gmail_user, gmail_app_password)
print("[bright_green bold]Logged in[/bright_green bold]")

server.sendmail(sent_from, sent_to, "hi!")
print(f"[bright_cyan]Sent email to {sent_to}[/bright_cyan]")

server.close()

