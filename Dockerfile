# Usa imagem oficial leve
FROM python:3.12-slim

# variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

# Setar diretório de trabalho
WORKDIR /app

# Copia requirements
COPY requirements.txt ./

# Atualiza o pip e instala dependências
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Copia o resto do projeto
COPY . .


# Comando padrão: executa o script
CMD ["python", "main.py"]
