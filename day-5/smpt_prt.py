import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'bhageshbandi39@gmail.com'
email_passwd = 'qone tjid ggmz eigf'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='hirohamada6max@gmail.com', msg="hi this is Bhagesh Bandi from cisco training sep-24 my team no.is T9 teammate name is pranil")
connection.close()
print('Mail sent successfully')
#mt.nithin@gmail.com
