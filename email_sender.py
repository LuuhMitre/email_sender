import pandas as pd
import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import user_logs as ul

smtp_server = ul.SMTP_SERVER
port = ul.PORT
sender_email = ul.SENDER_EMAIL
password = ul.PASSWORD

clientes = pd.read_excel("/content/Emails.xlsx")

for index, cliente in clientes.iterrows():
    print(cliente['cliente'], cliente['email'])
    msg = MIMEMultipart()
    msg['Subject'] = 'Novidade! Telefonia Fixa Master Internet.'
    msg['From'] = sender_email
    msg['To'] = cliente['email']

    message = ""

    msg.attach(MIMEText(message, 'html'))
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        server.quit()  # Close the connection
