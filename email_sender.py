import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import user_logs as ul
from email.mime.image import MIMEImage

smtp_server = ul.SMTP_SERVER
port = ul.PORT
sender_email = ul.SENDER_EMAIL
password = ul.PASSWORD

clientes = pd.read_excel("emails.xlsx")

with open("email_message.html", "r", encoding="utf-8") as file:
    html_template = file.read()

for index, cliente in clientes.iterrows():
    nome = cliente['cliente']
    destinatario = cliente['email']

    print(nome, destinatario)

    html_personalizado = html_template.format(cliente=nome)

    msg = MIMEMultipart()
    msg['Subject'] = 'Novidade! Telefonia Fixa Master Internet.'
    msg['From'] = sender_email
    msg['To'] = destinatario

    msg.attach(MIMEText(html_personalizado, 'html'))
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        # substitua com o nome da imagem real
        with open("images/logo_master.png", "rb") as img_file:
            img = MIMEImage(img_file.read())
            # precisa bater com o cid no HTML
            img.add_header('Content-ID', '<signature_image>')
            img.add_header('Content-Disposition', 'inline',
                           filename="logo_master.png")
            msg.attach(img)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        server.quit()
