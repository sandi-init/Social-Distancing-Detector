import smtplib
import ssl

class Mailer:

    """
    This script initiaties the email alert function.
    """


    def send(self,mail,s):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        # Authentication
        server.login("sandiashwi@gmail.com", "Srini1234")

        # message to be sent
        SUBJECT = 'ALERT!'
        TEXT = 'Social distancing violations exceeded! \nserious violation is :{}'.format(s)
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        # sending the mail
        server.sendmail("sandiashwi@gmail.com", mail, message)

        # terminating the session
        server.quit()
