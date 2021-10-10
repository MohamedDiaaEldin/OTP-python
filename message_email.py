from os import removexattr
import smtplib
# # secert data - import 
# import os
# from os.path import join, dirname
# from dotenv import load_dotenv

from decouple import config

def send_email(to, message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    email = config('EMAIL')
    password = config('PASSWORD')    

    print(email)
    print(password)

    server.login(email, password)
    server.sendmail(email, to, str(message))
    server.quit()
