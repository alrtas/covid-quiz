# Chatbot que faz Quiz sobre COVID-19

Neste projeto temos uma simples implmentacao de um chatbot, desenvolvido em Python que tem como objetivo principal, realizar um Quiz, com perguntas pre-definidas e as respostas coletadas a partir de uma API. Este chtbot em sua Versao 1 esta somente disponivel em linha de comando e na sua Versao 2 estara disponivel no Telegram.

## Conteudos
* [A API](#api)
* [Regras do jogo](#regras-do-jogo)
* [Infraestrutura](#infraestrutura)
* [Instalacao](#instalacao)



## API

Para este quiz estaremos usando a API disponibilizada pela equipe do [Postman](https://www.postman.com/) que nao requer nenhum autorizacao para coleta da maioria dos dados, para conferir voce pode checar este [link](https://documenter.getpostman.com/view/10808728/SzS8rjbc#27454960-ea1c-4b91-a0b6-0468bb4e6712), em nossa implementacao usamos as seguintes rotas:

* /summary
* /countries
* /live/country/`country`/status/confirmed
* /dayone/country/`country`/status/confirmed

## Regras do jogo

O jogo foi construido de maneira a ser extramente simples e customizavel, atraves do documento `.env` sera possivel customizar alguns parametros como, a duracao do jogo, sendo um numero que pode variar de 1 ao numero de perguntas que existem e tambem existe um parametro que controle a quantidade de opcoes por pergunta. 

Uma vez ambos parametros configurados, o jogo ira carregar, chamando todos os endpoints para todas as perguntas, por padrao o jogo tera 7 perguntas na lista de perguntas mas somente fara 5 perguntas, sempre em uma ordem randomica, para tornar o jogo mais unico para cada participante. O jogo tambem ira apresentar as opcoes de resposta em uma ordem randomica, tornando ainda mais unico o jogo para cada usuario.

O usuario devera responder a pergunta sempre com o Index da opcao, entao ira apresenta a opcao A: ..., B: ... e o usuario ira escolher a opcao digitando a letra correspondente, caso o cliente digite algo que nao corresponto a algum Index o mesmo recebera uma mensagem de erro e a oportunidade de responder novamente.

Ao final do jogo sera calculado a sua nota mostrando quantas questoes voce acertou do total de questoes e qual a sua nota de 0 a 10.

## Infraestrutura

Para conseguirmos escalar o jogo o mesmo foi construido em cima de Container, para isso temos junto ao projeto um Dockerfile e um Makefile, o Dockerfile tem as instrucoes para baixar a imagem do Python e instalar as dependencias necessarias.

O Makefile vem para facilitar a usabilidade em criacao de uma docker e rodar o mesmo, por conta disso o mesmo implementa os comandos `./make setup` e `./make run`

## Instalacao

A instalacao por ser baseado em Container sera super simples, basta baixar o [Docker](https://www.docker.com/), uma vez baixado e instalado, baixar fazer o download do source deste projeto, uma vez navegado ate pasta do projeto basta executar os comandos:
* `./make setup`
* `./make run`

Executado estes comandos basta conferir no seu Docker Desktop se esta rodando o container. Para jogar o jogo basta entrar na CLI do Docker e divertir-se!
