import smtplib,ssl
port = 465
smtp_server = "smtp.gmail.com"
sender_email = ""
reciever_email = ""
password = "Your Password"
message = """\
Subject: Hi There
There was no error in the webserver It ran successfully. """

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,reciever_email,message)
