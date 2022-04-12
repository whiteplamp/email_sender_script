import os
import smtplib
from config import LOGIN, PASSWORD
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(address_to: str, msg_subj: str, filepath):
    address_from = LOGIN
    password = PASSWORD
    msg = MIMEMultipart()
    msg['From'] = address_from
    msg['To'] = address_to
    msg['Subject'] = msg_subj

    attach_file(msg, filepath)

    # Login
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    # server.set_debuglevel(1)
    server.ehlo(address_from)
    server.login(address_from, password)
    server.send_message(msg)
    server.quit()


def attach_file(msg, filepath):
    filename = os.path.basename(filepath)
    with open(filepath, encoding='utf-8') as fp:
        file = MIMEText(fp.read(), _subtype='plain')
        fp.close()

    file.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(file)


def main():
    send_email("yan_netsky@mail.ru", "Timetable bot log",
               "..\shiyabin_bot\logs\message_logs.txt")


if __name__ == '__main__':
    main()
