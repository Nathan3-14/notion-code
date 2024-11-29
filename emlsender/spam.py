import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
server.ehlo()

sent_from = "nathan.watson@oasisbrislington.org"
sent_to = "nathan.watson@oasisbrislington.org"


server.login("nathan.watson@oasisbrislington.org", "qqbz hbby ixne ascd")
print("[bright_green bold]Logged in[/bright_green bold]")

server.sendmail(sent_from, sent_to, "hi!")
print(f"[bright_cyan]Sent email to {to}[/bright_cyan]")

server.close()