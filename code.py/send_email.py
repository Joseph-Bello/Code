import smtplib

sender = "bellotemidayo@gmail.com"
receiver = "jshbellz@gmail.com"
password = "********"
subject = "Python Email Test"
body = "I wrote an email in python :D"


message = f"""From: Joseph Bello{sender}
To: Josh Bellz{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:

  server.login(sender,password)
  print ("Logged in....")
  server.sendmail(sender,receiver, message)
  print ("Email has been sent")

except smtplib.SMTPAuthenticationError:
  print("unable to sign in")
