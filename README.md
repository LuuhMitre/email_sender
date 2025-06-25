# Automatizador de Envio de E-mails

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![SMTP](https://img.shields.io/badge/SMTP-Email-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

## 📄 Descrição

Este projeto em Python foi desenvolvido para automatizar o envio de e-mails personalizados a partir de uma lista de contatos em uma planilha Excel. O programa viabiliza o envio de mensagens em massa com um toque pessoal, sem a necessidade de depender de serviços de e-mail marketing.

## ✨ Funcionalidades Principais

- **Leitura de Contatos via Excel**: Lê múltiplos contatos (com nome e e-mail) diretamente de uma planilha `.xlsx`.
- **Mensagens Personalizadas**: Personaliza o corpo do e-mail e se refere a cada contato pelo seu respectivo nome.
- **Feedback de Envio**: Fornece um status no terminal, informando para qual contato o e-mail foi enviado com sucesso ou apontando o erro apresentado em caso de falhas.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas**: Para leitura e manipulação da planilha de contatos.
- **smtplib** e **email**: Bibliotecas padrão do Python para o envio dos e-mails.

## ⚙️ Instalação e Configuração

Antes de começar, garanta que você tenha o **Python 3** e o **pip** instalados em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/LuuhMitre/email_sender.git](https://github.com/LuuhMitre/email_sender.git)
    cd email_sender
    ```

2.  **Instale as dependências necessárias:**
    ```bash
    pip install pandas 
    ```

3.  **Crie e configure o arquivo de credenciais:**
    Crie um arquivo `user_logs.py` na raiz do projeto para armazenar as credenciais e os dados do servidor. Você pode usar como base o arquivo `examples/user_logs_example.py` ou o modelo abaixo
    ```user_logs
    SMTP_SERVER = 'smtp.example.com'
    PORT = 123
    SENDER_EMAIL = 'email@email.com'
    PASSWORD = 'password'
    ```

4.  **Prepare sua lista de contatos:**
    Adicione sua planilha de contatos com o nome `emails.xlsx` na raiz do projeto. Utilize o arquivo `examples/emails_example` como modelo. A planilha deve conter as colunas com o nome do cliente e o e-mail de destino.


    | nome          | email                   |
    |---------------|-------------------------|
    | João Silva    | joao.silva@email.com    |
    | Maria Souza   | maria.s@exemplo.org     |
    | Carlos Santos | carlos-santos@provedor.net|


## 🚀 Como Executar

Com tudo configurado corretamente, basta executar o script principal através do terminal:

```bash
python email_sender.py
```

O script irá percorrer a lista de contatos e enviar um e-mail para cada um, imprimindo o status no terminal.


## ✍️ Autor

* **Luana Mitre** - [GitHub](https://github.com/LuuhMitre)