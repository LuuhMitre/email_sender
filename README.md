# 📬 Automatizador de Envio de E-mails

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![SMTP](https://img.shields.io/badge/SMTP-Automation-green)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![Status](https://img.shields.io/badge/Status-Ativo-success)

## 📄 Descrição

Este projeto em Python automatiza o envio de e-mails personalizados em massa com base em uma lista de contatos em formato Excel. A versão atual inclui melhorias como modularização, uso de template HTML, medição do tempo de execução com decorator e suporte total a execução com ou sem Docker.

## ✨ Funcionalidades

- 📑 Leitura de contatos via planilha `.xlsx`
- 💌 Geração de mensagens personalizadas com template HTML
- 🐳 Execução compatível com ou sem Docker
- 🔐 Uso de variáveis sensíveis via `.env` ou módulo `user_logs`
- ⏱️ Exibe o tempo total de execução do envio com decorador
- 📥 Feedback direto no terminal (envios bem-sucedidos ou falhas)

## 🛠️ Tecnologias

- **Python 3**
- **Pandas** – Manipulação de planilha Excel
- **smtplib & email** – Envio de e-mails
- **dotenv** – Variáveis de ambiente com `.env`
- **Docker** – Execução containerizada (opcional)

---

## ⚙️ Instalação

### 🔁 Clone o projeto

```bash
git clone https://github.com/FelRFDev/email_sender.git
cd email_sender
```

### 📦 Instale as dependências (sem Docker)

```bash
pip install -r requirements.txt
```

### 🔐 Configuração das Credenciais

Você pode escolher entre **dois modos de execução**:

#### ✅ **Modo 1 – Com Docker:**

1. Crie um arquivo `.env` com as seguintes variáveis:

```env
SMTP_SERVER=smtp.seuprovedor.com
PORT=587
SENDER_EMAIL=seu@email.com
PASSWORD=sua_senha_de_app
```

> 💡 Recomendado para produção. Para Gmail, ative a autenticação em duas etapas e gere uma senha de app.

#### ✅ **Modo 2 – Sem Docker:**

1. Crie um arquivo `user_logs.py` com as credenciais:

```python
SMTP_SERVER = 'smtp.seuprovedor.com'
PORT = 587
SENDER_EMAIL = 'seu@email.com'
PASSWORD = 'sua_senha_de_app'
```

2. Descomente a linha abaixo no início do `email_sender.py`:

```python
# import user_logs as ul
```

3. Comente as variáveis do `os.environ.get(...)` para evitar conflito.

---

### 📇 Prepare a planilha de contatos

Crie o arquivo `contatos.xlsx` com as colunas `cliente` e `email`. Exemplo:

| cliente          | email                      |
|------------------|----------------------------|
| João da Silva    | joao.silva@email.com       |
| Maria Oliveira   | maria.o@gmail.com          |
| Carlos Fernandes | carlos.fernandes@empresa.com |

---

### 📨 Personalize o template HTML

Edite o arquivo `email_message.html` e insira `{cliente}` onde desejar personalizar com o nome do destinatário.

```html
<p>Olá {cliente},</p>
<p>Temos uma novidade incrível para você!</p>
```

---

## 🚀 Como executar

### 🐳 Executando com Docker

```bash
docker compose up --build
```
ou, dependendo da sua versão:

```bash
docker-compose up --build
```

### 💻 Executando sem Docker

```bash
python email_sender.py
```

Ao final, será exibido o tempo de execução total, exemplo:

```
send_email executada em 0 minuto(s) e 10.16 segundo(s)
```

---

## 🤝 Projeto Base

Este repositório foi aprimorado com base no projeto da desenvolvedora [Luana Mitre](https://github.com/LuuhMitre/email_sender), incorporando modularização, suporte a Docker, medições de desempenho e melhor separação de responsabilidades.

---

## 👨‍💻 Autor desta versão

**Felipe Rodrigues**  
🔗 [github.com/FelRFDev](https://github.com/FelRFDev)  
🔗 [Portfólio:](https://felrfdev.netlify.app)  