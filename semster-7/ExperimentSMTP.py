# import necessary packages
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# create message object instance
class EmailSender:
    @staticmethod
    def send_mail(message, subject, email):
        msg = MIMEMultipart()
        # setup the parameters of the message
        password = ""
        msg['From'] = "maximilian.sommer@stud.hshl.de"
        msg['To'] = email
        msg['Subject'] = subject
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        # create server
        try:
            server_ssl = smtplib.SMTP_SSL('smtp.stud.hshl.de', 465)
            server_ssl.ehlo()
            # Login Credentials for sending the mail
            server_ssl.login(msg['From'], password)
            # send the message via the server.
            server_ssl.sendmail(msg['From'], msg['To'], msg.as_string())
            server_ssl.close()
            print("successfully sent email to %s:" % (msg['To']))
        except smtplib.SMTPException as e:
            logging.error(e)


if __name__ == '__main__':

    message = 'Test'
    subject = 'SMTP'
    email = 'maximilian.sommer@stud.hshl.de'
    EmailSender.send_mail(message, subject, email)
