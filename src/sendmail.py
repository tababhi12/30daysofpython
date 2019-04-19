from smtplib import SMTP,SMTPAuthenticationError

host = 'smtp.gmail.com'
port = 587
username = 'pytesting1207@gmail.com'
password = 'Python@123'
from_email = 'pytesting1207@gmail.com'
to_mail = ['abhishekebay02@gmail.com']
msg = 'This is a testing mail'
try:
    email_conn = SMTP(host,port)
    print(email_conn.ehlo())
    email_conn.starttls()
    print(email_conn.login(username,password))
    email_conn.sendmail(from_email,to_mail,msg)

except SMTPAuthenticationError as s:
    print(s)
except Exception as e:
    print(e)

finally:
    email_conn.quit()