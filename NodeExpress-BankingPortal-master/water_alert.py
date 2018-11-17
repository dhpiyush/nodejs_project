#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 01:25:47 2018

@author: piyushdhingra
"""

import smtplib
import email.message
#import random
#import goslate
#from googletrans import Translator

#https://py-googletrans.readthedocs.io/en/latest/


def send_mail():
    #lang=['hi']
    s = smtplib.SMTP('smtp.gmail.com:587')
    email_content = "Drink Water"
    msg = email.message.Message()
    #choice = random.choice(lang)
    #print(choice)
    #text = "Drink Water"
    #gs = goslate.Goslate()
    #translatedText = gs.translate(text,'hi')
    #print(translatedText)
    #translator = Translator()
    #t = translator.translate('Drink Water',dest=choice,src='en')
    msg['Subject'] = 'Dawayi lo aur Paani Piyooo'
     
    recipients = ['narang.richa1995@gmail.com','richa8feb1995@gmail.com']
    #recipients = ['piyushdh94@gmail.com']
    msg['From'] = 'f20130710g@alumni.bits-pilani.ac.in'
    #msg['To'] = ['piyushdh94@gmail.com','f20130710@goa.bits-pilani.ac.in']
    
    password = "432165"
    msg.add_header('Content-Type', 'text/html')
    
    msg.set_payload(email_content)
     
    
    s.starttls()
     
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    for x in recipients:
        print(x)
        
        s.sendmail(msg['From'], x, msg.as_string())
    

send_mail()
