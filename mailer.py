import os, smtplib, logging
from paired import Paired
from participant import Participant
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mailer:

    client: smtplib.SMTP_SSL
    mail_template: str

    def __init__(self) -> None:
        self.conn()
        self.read_template()

    def read_template(self):
        with open(f"{os.getenv('assets_path')}/mail.html") as mail_template:
            self.mail_template = mail_template.read()
        return self

    def conn(self):
        logging.info("Connecting to smtp server")
        self.client = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.client.login(os.getenv("mail_sender"), os.getenv("mail_password"))
        logging.info("Connected to smtp server")

    def close(self):
        self.client.close()

    def send_message(self, paired: Paired):

        logging.info(f"Sending [{paired.participant.name}] secret friend to his email [{paired.participant.email}]")

        message = MIMEMultipart()
        message['From'] = os.getenv("mail_sender")
        message['To'] = paired.participant.email
        message['Subject'] = f"🤫 Hey {paired.participant.name}, seu amigo secreto foi revelado 🎉🎁"

        body = self.mail_template.replace("{{secret_friend}}", paired.secret_friend.name)
        body = MIMEText(body, "html")
        message.attach(body)

        self.client.sendmail(os.getenv("mail_sender"), paired.participant.email, message.as_string())
        logging.info(f"Done sending [{paired.participant.name}] secret friend to his email [{paired.participant.email}]")
