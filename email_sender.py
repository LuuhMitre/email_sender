import smtplib

#import user_logs as ul #Importar somente se não utilizar o docker
from email.mime.image import MIMEImage
import os
from dotenv import load_dotenv
from contact_reader import load_contacts
from msg_generator import generate_msg
from utils import tempo_de_execucao

'Utilize este import caso não vá utilizar docker'
#import user_logs as ul

load_dotenv()  # Carrega as variáveis do .env automaticamente

#Variáveis de ambiente para docker

SMTP_SERVER = os.environ.get("SMTP_SERVER")
PORT = int(os.environ.get("PORT"))
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
PASSWORD = os.environ.get("PASSWORD")


# Configurações do servidor SMTP

"""Utilizar as variáveis abaixo somente quando
não utilizar o docker."""

# SMTP_SERVER = ul.SMTP_SERVER
# PORT = ul.PORT
# SENDER_EMAIL = ul.SENDER_EMAIL
# PASSWORD = ul.PASSWORD

@tempo_de_execucao
def send_email():
    """
    Envia e-mails personalizados em massa utilizando um servidor SMTP.

    Esta função:
    - Lê os contatos de um arquivo Excel (.xlsx)
    - Carrega um template HTML de mensagem
    - Gera e personaliza mensagens com nome e e-mail de cada destinatário
    - Anexa uma imagem (logo ou assinatura) à mensagem
    - Envia os e-mails via servidor SMTP, usando credenciais definidas no arquivo .env

    Requisitos:
        - Arquivo .env com as variáveis: SMTP_SERVER, PORT, SENDER_EMAIL e PASSWORD
        - Arquivo 'contatos.xlsx' com colunas 'cliente' e 'email'
        - Arquivo 'email_message.html' como template base da mensagem
        - Imagem em 'images/logo_master.png' para assinatura visual
        - Função generate_msg() para montar a mensagem (importada de msg_generator)
        - Função load_contacts() para ler o arquivo de contatos (importada de contact_reader)

    Prints são exibidos no console para acompanhar o status de cada envio.
    Eventuais erros são tratados individualmente para que o processo continue mesmo com falhas.
    """
    server = None  # Inicializa a variável do servidor como nula
    clientes = load_contacts('./contatos.xlsx')
    with open("email_message.html", "r", encoding="utf-8") as file:
        html_template = file.read()

    try:
        # Conectando ao servidor SMTP
        print("Conectando ao servidor SMTP")
        server = smtplib.SMTP(SMTP_SERVER, PORT)
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        print("Conexão estabelecida com sucesso!")

        # Enviando e-mails para todos os clientes listados no arquivo emails.xlsx
        for _ , customers in clientes.iterrows():
            nome = customers['cliente']
            destinatario = customers['email']
            mensagem = generate_msg(html_template, nome, SENDER_EMAIL, destinatario)

            # Verificando se será possível enviar o e-mail
            try:
                # Anexando a imagem da assinatura
                with open("images/logo_master.png", "rb") as img_file:
                    img = MIMEImage(img_file.read())
                    img.add_header('Content-ID', '<signature_image>')
                    mensagem.attach(img)

                # Enviando o e-mail
                server.sendmail(mensagem['From'], mensagem['To'], mensagem.as_string())
                print(f"E-mail enviado para {nome} com sucesso!!")
            except Exception as e:
                # Tratando erros ao enviar o e-mail
                print(f"Falha ao enviar o e-mail para {nome}. Erro: {e}")

    except Exception as e:
        # Tratando erros de conexão com o servidor SMTP
        print(f"Ocorreu um erro ao conectar ao servidor SMTP: {e}")
    finally:
        # Encerrando a conexão com o servidor SMTP
        if server:
            server.quit()
            print("Conexão com o servidor SMTP encerrada.")