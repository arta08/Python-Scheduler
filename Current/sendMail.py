import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import conf_email, conf_email_password

def action_send(penerima, subjek, isi_pesan):
    email_pengirim = conf_email
    password = conf_email_password

    msg = MIMEMultipart()
    msg['From'] = email_pengirim
    msg['To'] = penerima
    msg['Subject'] = subjek

    msg.attach(MIMEText(isi_pesan, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_pengirim, password)
    server.send_message(msg)
    server.quit()
