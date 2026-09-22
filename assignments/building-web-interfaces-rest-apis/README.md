# 📘 Assignment: Building Web Interfaces for REST APIs

## 🎯 Objective

Crie uma interface web que consuma uma API REST criada com FastAPI. Você irá usar HTML, JavaScript e `fetch` para exibir livros, enviar novos dados e lidar com respostas da API.

## 📝 Tasks

### 🛠️ Exibir dados da API

#### Descrição
Crie uma página `index.html` com uma seção para listar livros. No arquivo `script.js`, faça uma requisição `GET` para o endpoint `/books` da API FastAPI e mostre cada livro na página.

#### Requisitos
O programa concluído deve:

- Ter uma página HTML com título e uma área para a lista de livros
- Usar `fetch` para consultar o endpoint `GET /books`
- Exibir o título e o autor de cada livro retornado pela API
- Mostrar uma mensagem compreensível quando a lista estiver vazia ou ocorrer um erro


### 🛠️ Enviar novos livros

#### Descrição
Adicione um formulário para cadastrar livros. Ao enviar o formulário, envie os dados como JSON para o endpoint `POST /books` e atualize a lista sem recarregar a página.

#### Requisitos
O programa concluído deve:

- Ter campos obrigatórios para título e autor
- Interceptar o envio do formulário com JavaScript
- Enviar uma requisição `POST` com o cabeçalho `Content-Type: application/json`
- Limpar o formulário e atualizar a lista após um cadastro bem-sucedido
- Exibir uma mensagem de erro quando a API rejeitar o cadastro


### 🛠️ Adicionar interação e estados da interface

#### Descrição
Melhore a experiência da página permitindo remover livros e comunicando ao usuário os estados de carregamento, sucesso e erro.

#### Requisitos
O programa concluído deve:

- Exibir um botão de remoção para cada livro
- Enviar uma requisição `DELETE /books/{book_id}` ao remover um livro
- Atualizar a lista depois de uma remoção bem-sucedida
- Desabilitar ou identificar controles enquanto uma requisição estiver em andamento
- Mostrar mensagens diferentes para carregamento, sucesso e erro