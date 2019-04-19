from smtplib import SMTP,SMTPAuthenticationError,SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = 'smtp.gmail.com'
port = 587
username = 'pytesting1207@gmail.com'
password = 'Python@123'
from_email = 'pytesting1207@gmail.com'
to_mail = ['abhishekebay02@gmail.com']
msg = 'This is a testing mail'
try:
    email_conn = SMTP(host,port)
    print(email_conn.ehlo()) #to check SMTP is working
    email_conn.starttls() #for encruption
    print(email_conn.login(username,password)) # check connection has been made

    #for HTML
    the_msg = MIMEMultipart('alternative')
    the_msg['Subject'] = 'Testing'
    the_msg['From'] = from_email
    #the_msg['To'] = to_mail
    plain_text = 'This is a testing message'
    html_text = '''
    <html>
    <head></head>
    <body>
    <p>Hey!<br/>This is a testing message.Made by me</p>
    </body>
    </html>
    '''
    part1 = MIMEText(plain_text,'plain')
    part2 = MIMEText(html_text,'html')
    the_msg.attach(part1)
    the_msg.attach(part2)
    email_conn.sendmail(from_email,to_mail,the_msg.as_string())

except SMTPAuthenticationError as s:
    print(s)
except SMTPException as a:
    print(a)
except Exception as e:
    print(e)

finally:
    email_conn.quit()