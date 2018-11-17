#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 01:54:09 2018

@author: piyushdhingra
"""
import random
import json
import os
import smtplib
import email.message


def random_num_generator():
    return random.randint(1,30000)

def append_number(number):
    with open('/Users/piyushdhingra/Documents/numbers.txt', 'a') as f:
        json.dump(number, f)
        f.write(os.linesep)
'''
def send_mail(word_details):
    #li = ["piyushdh94@gmail.com", "richa8feb1995@gmail.com"]
    li = ["f20130710@goa.bits-pilani.ac.in"]
    try:
        for i in li:
            s = smtplib.SMTP('smtp.gmail.com', 465)
            s.ehlo()
            s.starttls()
            s.login("piyushdh94@gmail.com", "pd26397@")
            #message = 'Word: '+ word_details['word']+ ' \n Meaning: ' + word_details['meaning']+'\n If you want to look up examples: '+ word_details['url']
            message = "test1"
            s.sendmail("piyushdh94@gmail.com", i , message)
            s.quit()
        print ("Successfully sent email")
    except:
        print ("Error: unable to send email")

'''
def read_record():
    file = open('/Users/piyushdhingra/Documents/dictionary.txt', 'r') 
    lines = file.readlines()
    #d = json.loads(h)
    #for i in range(1,3):
     #   d = json.loads(lines[i])
        #y = d["word"]
      #  print(d['word'])
    file2 = open('/Users/piyushdhingra/Documents/numbers.txt', 'r')
    lines2 = file2.readlines()
    lines2 = list(map(lambda s: s.strip(), lines2))
    #rint(lines2[0])
    val = 1
    while(val):
        my_dict = {}
        num = random_num_generator()
        string = str(num)
        if string not in lines2:
            #mail
            #print(num)
            
            my_dict = lines[num]
            my_dict = json.loads(my_dict)
            if(len(my_dict['meaning'])>= 2):
                send_mail2(my_dict)
                file2.close()
                append_number(num)
                file.close()
                val = 0
    #print(lines[1])
    
#read_record()
'''
def send_mail1():
    gmail_user = 'piyushdh94@gmail.com'  
    gmail_password = 'pd26397@'
    
    sent_from = gmail_user  
    to = 'f20130710@goa.bits-pilani.ac.in' 
    subject = "Where are all my Robot Women at?"
    body = ("Hey, what's up? friend!\n\n"
                 "I hope you have been well!\n"
                 "\n"
                 "Cheers,\n"
                 "Jay\n")
    
    email_text = """\
    From: %s
    To: %s
    subject: %s
    
    %s
    """ % (sent_from, to, subject, body)
    
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    
        print ('Email sent!')
    except:  
        print ('Something went wrong...')
        
'''

# Allow access : https://myaccount.google.com/u/0/lesssecureapps?pli=1&pageId=none
#               https://support.google.com/accounts/answer/6010255?authuser=1
#Link : https://code.tutsplus.com/tutorials/sending-emails-in-python-with-smtp--cms-29975
def send_mail2(word_details):
    
    s = smtplib.SMTP('smtp.gmail.com:587')
    #print(word_details['meaning'])
    #print(len(word_details['meaning']))
    #l = '\n'.join(word_details['meaning']).encode('utf-8')
    l1 = ''
    l2 = ''
    l3 = ''
    l = ''
    try :
        l1 = word_details['meaning'][0]
        l = l+ l1 + '<br>'
    except:
        pass
    try :
        l2 = word_details['meaning'][1]
        l = l + l2 + '<br>'
    except:
        pass
    try :
        l3 = word_details['meaning'][2]
        l = l + l3 
    except:
        pass
    #l = l1 + '<br>' + l2 + '<br>' + l3
    l = l.encode('utf-8')
    #l = str(l.decode('utf-8'))
    email_content = '<h2>Word: '+ str(word_details['word'])+ '</h2><h3 style="color:#500050">Meaning:<br> ' + str(l) +'<br><br>Link: '+ str(word_details['url'])+'</h3><br><br> From your loving boyfriend :)'
     
    msg = email.message.Message()
    msg['Subject'] = 'Word of the day: '+ str(word_details['word'])
     
    recipients = ['narang.richa1995@gmail.com','richa8feb1995@gmail.com','piyushdh94@gmail.com']
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
    
#send_mail2()
read_record()

