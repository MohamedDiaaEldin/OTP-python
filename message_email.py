from os import removexattr
import smtplib

from decouple import config

def send_email(to, message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    email = config('EMAIL')
    password = config('PASSWORD')    

    server.login(email, password)
    server.sendmail(email, to, str(message))
    server.quit()
