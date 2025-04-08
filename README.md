
# 🧩 Django REST API - User Manager

Olá! Este projeto é uma API REST que desenvolvi com **Django** e **Django REST Framework** para gerenciar usuários.  
Ela implementa o CRUD completo: criação, leitura, atualização e exclusão de usuários.

---

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/index.html)

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

## 🧪 Testando com Postman

- Certifique-se de que o servidor Django está rodando com `python manage.py runserver`
- Use os endpoints acima no Postman com os métodos HTTP correspondentes
- O content-type das requisições deve ser `application/json`

---

## 🌱 Futuras Features & Melhorias

- ✅ Atualização parcial com método `PATCH`
- 🔒 Autenticação e permissões com `TokenAuthentication`
- 🖼️ Integração com um frontend feito em React
- 🌐 Substituir o banco de dados SQLite por PostgreSQL 
- 🌍 Deploy na nuvem (Render, Vercel ou Heroku)
- 📄 Documentação automática com Swagger ou Redoc
- 🔎 Filtros, ordenação e paginação

---

## 🙋🏽‍♂️ Autor

Feito com 💻 e ☕ por **Matheus Rocha | Dev**  
Se quiser conversar ou colaborar, me chama!
