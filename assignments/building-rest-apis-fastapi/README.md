# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST simples usando o framework FastAPI. Você irá criar endpoints, trabalhar com dados JSON e aplicar códigos de status HTTP para disponibilizar um catálogo de livros.

## 📝 Tarefas

### 🛠️ Criar o primeiro endpoint

#### Descrição
Complete o código inicial e crie um endpoint `GET /` que confirme que a API está funcionando. Depois, crie um endpoint `GET /books` que retorne a lista de livros armazenada em memória.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI
- Retornar uma mensagem JSON em `GET /`
- Retornar todos os livros em `GET /books`
- Iniciar localmente com `uvicorn` e responder sem erros


### 🛠️ Implementar operações de livros

#### Descrição
Adicione operações para consultar um livro específico e cadastrar novos livros no catálogo. Cada livro deve possuir um identificador, título e autor.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` para buscar um livro pelo identificador
- Implementar `POST /books` para adicionar um livro usando dados JSON
- Retornar o livro criado na resposta do `POST`
- Retornar o código de status `404` quando o identificador não existir


### 🛠️ Validar entradas e atualizar livros

#### Descrição
Use modelos Pydantic para validar os dados recebidos e complete o CRUD do catálogo adicionando atualização e remoção de livros.

#### Requisitos
O programa concluído deve:

- Rejeitar requisições sem título ou autor válidos
- Implementar `PUT /books/{book_id}` para atualizar um livro existente
- Implementar `DELETE /books/{book_id}` para remover um livro existente
- Retornar `404` nas operações que receberem um identificador inexistente
- Usar códigos de status HTTP coerentes para criação, sucesso e remoção