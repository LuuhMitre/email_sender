
# email_sender

Projeto em Python para enviar e-mails em massa usando credenciais SMTP definidas no arquivo `user_logs.py`.

---

## Descrição

Este projeto contém um script para envio de e-mails via protocolo SMTP, utilizando as credenciais armazenadas no arquivo `user_logs.py`. É uma base para facilitar o envio de mensagens personalizadas de forma automatizada.

---

## Como usar

### 1. Clonar o repositório

```bash
git clone https://github.com/LuuhMitre/email_sender.git
cd email_sender
```

### 2. Configurar as credenciais

No arquivo `user_logs.py`, insira suas credenciais SMTP, por exemplo:

```python
usuario = "seu_email@gmail.com"
senha = "sua_senha"
servidor = "smtp.gmail.com"
porta = 587
```

### 3. Executar o script

Rode o script principal para enviar o e-mail:

```bash
python email_sender.py
```



---

## Estrutura do projeto

- `user_logs.py`: arquivo com as credenciais de acesso SMTP.
- `email_sender.py`: script para enviar e-mails usando as credenciais.
- `email_message.html`: arquivo HTML com o corpo do e-mail a ser enviado.

---


## Próximos passos

- Criar interface para facilitar a inserção das credenciais.
- Implementar validações e tratamento de erros.

---
