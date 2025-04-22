
# 🧩 Django REST API - User Manager

Olá! Este projeto é uma aplicação Django com Django REST Framework e Django Templates para gerenciar usuários.
Ele implementa tanto um CRUD de API quanto views que renderizam HTML, permitindo a criação, leitura, atualização e exclusão de usuários, além de estilização com Bootstrap.


---

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Bootstrap](https://getbootstrap.com/)
---

## 📁 Estrutura do Projeto

A estrutura geral do projeto pode ser visualizada na imagem abaixo:

![estrutura do projeto](estrutura.png)


---
## 📦 Instalando as dependências

Para instalar todas as bibliotecas necessárias do projeto, siga os passos abaixo:

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # no Linux/macOS
venv\Scripts\activate     # no Windows
```
## 🐳 Rodando com Docker

> Não quer instalar tudo manualmente? Rode o projeto em um container com Docker! 

### 📋 Pré-requisitos

- [Docker](https://www.docker.com/) instalado na sua máquina  
- [Docker Compose](https://docs.docker.com/compose/) (já vem incluso no Docker Desktop)

### ▶️ Como iniciar o projeto

No terminal, dentro da pasta raiz do projeto (onde está o arquivo `docker-compose.yml`), execute:

```bash
docker-compose up --build

Isso irá:

- ✅ Construir a imagem da aplicação Django
- 🚀 Subir o container com tudo pronto (Python, dependências, servidor)

O app estará rodando em:  
🔗 [http://localhost:8000](http://localhost:8000)

---

## ⛔ Como parar o projeto

Para parar e remover os containers, use:

```bash
docker-compose down


## 🔗 Endpoints Disponíveis

### 🔍 GET todos os usuários
`GET /`  
- Retorna uma lista com todos os usuários cadastrados.

---

### 🔍 GET por nickname
`GET /user/<nick>`  
- Retorna os dados de um usuário específico com base no nickname (chave primária).

---

### 🔍 GET via query string
`GET /data?user=<user_nickname>`  
- Alternativa para buscar um usuário passando o nickname como parâmetro de URL.

---

### ➕ POST - Criar novo usuário
`POST /new_user`  
**Body (JSON):**
```json
{
  "user_nickname": "matheus123",
  "user_name": "Matheus",
  "user_email": "matheus@email.com",
  "user_age": 23
}
```

---

### ✏️ PUT - Atualizar usuário
`PUT /edit_user`  
⚠️ O campo `user_nickname` **não pode ser alterado**.  
**Body (JSON):**
```json
{
  "user_nickname": "matheus123",
  "user_name": "Novo Nome",
  "user_email": "novo@email.com",
  "user_age": 25
}
```

---

### 🗑️ DELETE - Excluir usuário
`DELETE /delete_user`  
**Body (JSON):**
```json
{
  "user_nickname": "matheus123"
}
```

---

### Frontend - Views HTML

Esses endpoints são responsáveis pela renderização de páginas HTML para as operações de usuário, utilizando templates do Django.

#### 🔍 Visualizar usuários
`GET /pages/users/`  
Exibe a lista de todos os usuários cadastrados.

#### ➕ Criar usuário
`GET /pages/users/create/`  
Exibe o formulário para criar um novo usuário.

#### ✏️ Editar usuário
`GET /pages/users/edit/<str:nickname>/`  
Exibe o formulário para editar os dados de um usuário específico.

#### 🗑️ Excluir usuário
`GET /pages/users/delete/<str:nickname>/`  
Exibe a confirmação para excluir um usuário específico.


## 🧪 Testando com Postman

- Certifique-se de que o servidor Django está rodando com `python manage.py runserver`
- Use os endpoints acima no Postman com os métodos HTTP correspondentes
- O content-type das requisições deve ser `application/json`

---

## 🌱 Futuras Features & Melhorias

- ✅ Atualização parcial com método `PATCH`
- 🔒 Autenticação e permissões com `TokenAuthentication`
- 🌐 Substituir o banco de dados SQLite por PostgreSQL 
- 🌍 Deploy na nuvem (Render, Vercel ou Heroku)
- 🔎 Filtros, ordenação e paginação

---

## 🙋🏽‍♂️ Autor

Feito com 💻 e ☕ por **Matheus Rocha | Dev**  
Se quiser conversar ou colaborar, me chama!
