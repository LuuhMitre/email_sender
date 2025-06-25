import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import user_logs as ul
from email.mime.image import MIMEImage

# Configurações do servidor SMTP
smtp_server = ul.SMTP_SERVER
port = ul.PORT
sender_email = ul.SENDER_EMAIL
password = ul.PASSWORD

clientes = pd.read_excel("emails.xlsx")

# Lendo o template HTML do e-mail
with open("email_message.html", "r", encoding="utf-8") as file:
    html_template = file.read()

server = None  # Inicializa a variável do servidor como nula
try:
    # Conectando ao servidor SMTP
    print("Conectando ao servidor SMTP")
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    print("Conexão estabelecida com sucesso!")

    # Enviando e-mails para todos os clientes listados no arquivo emails.xlsx
    for index, cliente in clientes.iterrows():
        nome = cliente['cliente']
        destinatario = cliente['email']

        # Personalizando o template HTML com o nome do cliente
        html_personalizado = html_template.format(cliente=nome)

        # Criando a mensagem de e-mail
        msg = MIMEMultipart('related')
        msg['Subject'] = 'Novidade! Telefonia Fixa Master Internet.'
        msg['From'] = sender_email
        msg['To'] = destinatario
        msg.attach(MIMEText(html_personalizado, 'html'))

        # Verificando se será possível enviar o e-mail
        try:
            # Anexando a imagem da assinatura
            with open("images/logo_master.png", "rb") as img_file:
                img = MIMEImage(img_file.read())
                img.add_header('Content-ID', '<signature_image>')
                msg.attach(img)

            # Enviando o e-mail
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print(f"E-mail enviado para {nome} com sucesso!!")
        except Exception as e:
            # Tratando erros ao enviar o e-mail
            print(f"Ao enviar o e-mail para {nome} ocorreu o erro: {e}")

except Exception as e:
    # Tratando erros de conexão com o servidor SMTP
    print(f"Ocorreu um erro ao conectar ao servidor SMTP: {e}")
finally:
    # Encerrando a conexão com o servidor SMTP
    if server:
        server.quit()
        print("Conexão com o servidor SMTP encerrada.")
