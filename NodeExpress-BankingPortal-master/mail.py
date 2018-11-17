import random
import time
import smtplib

From = 'piyushdh94@gmail.com'
To = 'piyushdh94@gmail.com'
Subject = 'test_code'

def send_mail(text):
	try:	
		
		message = 'Subject: %s\n\n%s' % (Subject, text)
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login("EMAIL", "PASSWORD")
		server.sendmail(From, To , message)
		server.quit()
		# print ("success")
	except Exception:
		pass
		# print ("error")
dict1={}
while 1==1 :
	lines = open('mail.txt').read().splitlines()
	myline =random.choice(lines)
	if myline in dict1:
		continue
	else:
		print(myline)
		send_mail(myline)
		dict1[myline] = 1
		time.sleep(3600)
	
