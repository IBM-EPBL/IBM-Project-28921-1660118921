import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def alert(main_msg):
    mail_from = 'arunkmarc0610@gmail.com'
    mail_to = 'carunkumar19cs@srishakthi.ac.in'
    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Subject'] = '!Alert Mail On Product Shortage! - Regards'
    mail_body = main_msg
    msg.attach(MIMEText(mail_body))

    try:
        server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)
        server.ehlo()
        server.login('api-key',
                     'xsmtpsib-5307f275b210ef3e04490e7374d9532de521b684c7803419e2eb655be375a061-I5yCbx3kszc4PLaS')
        server.sendmail(mail_from, mail_to, msg.as_string())
        server.close()
        print("Mail sent successfully!")
    except Exception as e:
        print(e)
        print("Some Issue, Mail not Sent :(")
