import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class GoogleMail:
    SMTP = "smtp.gmail.com"
    IMAP = "imap.gmail.com"

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def __set_smtp_connection(self):
        connection = smtplib.SMTP(self.SMTP, 587)

        connection.ehlo()
        connection.starttls()
        connection.ehlo()

        if connection.login(self.login, self.password):
            self.smtp_connection = connection
            return True

        return False

    def send_message(self, recipients: list, subject: str,
                     text: str) -> bool:
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject

        message.attach(MIMEText(text))

        if self.__set_smtp_connection():
            self.smtp_connection.sendmail(self.login, message,
                                          message.as_string())
            self.smtp_connection.quit()
            return True

        return False

    def receive_message(self, category='inbox', header='ALL'):
        mail = imaplib.IMAP4_SSL(self.IMAP)
        mail.login(self.login, self.password)

        mail.list()
        mail.select(category)
        criterion = f"(HEADER Subject \"{header}\")"
        result, data = mail.uid('search', criterion)

        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)

        mail.logout()

        if email_message:
            return email_message
        return None
