# Solução de Automação para Envio de E-mails Personalizados

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)

## 📄 Descrição

Esta é uma solução de automação desenvolvida em Python para otimizar e escalar a comunicação por e-mail. O script lê uma base de contatos de uma planilha Excel, insere dinamicamente informações personalizadas em um template HTML e envia os e-mails em massa, provendo feedback em tempo real sobre o status de cada envio.

O projeto foi criado para resolver a necessidade de realizar campanhas de e-mail marketing ou comunicação direta sem depender de serviços de terceiros, oferecendo total controle sobre o processo.

## ✨ Funcionalidades Principais

* **Fonte de Dados Flexível:** Lê nativamente contatos de planilhas `.xlsx`, permitindo fácil integração com bases de clientes existentes.
* **Templating HTML Dinâmico:** Utiliza um arquivo `.html` como template, personalizando o conteúdo para cada destinatário com seu nome, criando uma comunicação mais pessoal e eficaz.
* **Incorporação de Imagens:** Anexa imagens (como logos na assinatura) diretamente no corpo do e-mail, garantindo que elas sejam exibidas corretamente na maioria dos clientes de e-mail.
* **Tratamento de Erros e Logging:** Informa no terminal o sucesso ou a falha de cada envio individualmente e trata exceções de conexão com o servidor SMTP, garantindo a robustez da aplicação.
* **Separação de Configurações:** Mantém dados sensíveis (credenciais de e-mail) em um arquivo de configuração separado (`user_logs.py`), seguindo boas práticas de segurança.

## 🛠️ Tecnologias e Bibliotecas

* **Python 3:** Linguagem principal para toda a lógica de automação.
* **Pandas:** Utilizada para a leitura e manipulação eficiente dos dados da planilha de contatos.
* **smtplib:** Biblioteca padrão do Python para a comunicação com o servidor SMTP e envio dos e-mails.
* **email.mime:** Módulo padrão utilizado para construir as mensagens de e-mail em formato MIME, permitindo a criação de e-mails complexos com HTML e imagens anexadas.
* **HTML:** Linguagem de marcação para a criação do template de e-mail.

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

---

Feito com 💜 por Luana Mitre!

<p align="left">
  <a href="https://www.linkedin.com/in/luana-mitre/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
  <a href="https://github.com/LuuhMitre" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="Link para o GitHub">
  </a>
  <a href="https://my-portfolio-jet-one-93.vercel.app/" target="_blank">
    <img src="https://img.shields.io/badge/Portfólio-%238A2BE2?style=for-the-badge&logoColor=white" alt="Link para o Portfólio">
  </a>
</p>

