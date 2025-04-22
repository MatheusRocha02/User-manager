
#cria imagem python
FROM python:3.11

#Usa pasta DJANGO_API 
WORKDIR /DJANGO_API

#Copia o arquivo requirements.txt
COPY requirements.txt .

#Instala todas as dependências listadas nesse arquivo
RUN pip install --no-cache-dir -r requirements.txt

#Copia todos os arquivos do diretório para a imagem
COPY . .

#Porta onde o servidor da aplicação está rodando
EXPOSE 8000

#comandos para rodar nop cmd pra abrir o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]