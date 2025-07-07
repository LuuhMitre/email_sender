from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def generate_msg(html_template, customer_name:str, from_email:str, to_email:str):
    """
    Gera uma mensagem de e-mail personalizada no formato HTML.

    A função recebe um template HTML e insere o nome do cliente nele,
    criando uma mensagem pronta para ser enviada via SMTP. Também define
    remetente e destinatário nos headers da mensagem.

    Args:
        html_template (str): Conteúdo HTML base da mensagem, com placeholders.
        customer_name (str): Nome do cliente, que será inserido no template.
        from_email (str): Endereço de e-mail do remetente.
        to_email (str): Endereço de e-mail do destinatário.

    Returns:
        MIMEMultipart: Objeto de e-mail com o HTML personalizado, pronto para envio.
    """
    msg = ''

    try:
        # Personalizando o template HTML com o nome do cliente
            html_personalizado = html_template.format(cliente=customer_name)
            # Criando a mensagem de e-mail
            msg = MIMEMultipart('related')
            msg['Subject'] = 'Novidade! Telefonia Fixa Master Internet.'
            msg['From'] = from_email
            msg['To'] = to_email
            msg.attach(MIMEText(html_personalizado, 'html'))
    
    except Exception as e:
        print(f'Erro ao tentar ler o arquivo HTML: {e}')

    else:
        print('Msg gerada com sucesso!')
        return msg    