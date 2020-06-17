import smtplib,ssl
port = 465
smtp_server = "smtp.gmail.com"
sender_email = ""
reciever_email = ""
password = ""
message = """\
Subject: Hi There
There was some error during the launching of the webserver. """

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,reciever_email,message)
