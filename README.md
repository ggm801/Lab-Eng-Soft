# Grupo 3

#### Arthur Marie Thomas Theillier - 14029901
#### Eduardo Niza Minosso - 11918543
#### Gustavo Guimarães Matsumoto - 11805130

## Setup do projeto

### Primeiro passo - Clone repository
##### No terminal de comando utilize:

```
git clone https://github.com/ggm801/Lab-Eng-Soft.git
```

### Segundo passo - criar e ativar o ambiente virtual
##### No terminal de comando primeiro utilize:

```
python -m venv env
```

##### Depois utilize o comando:

```
.\env\bin\Activate.ps1
```
se não funcionar tente:
```
.\env\Scripts\activate
```

##### Por último utilize os comandos:

```
pip install django
```
e

```
pip install django-axes
```

###### OBS: Para esses comandos funcionarem é necessário ter o python adicionado ao path. Se não sabe como fazer isso acesse esse link:
###### https://www.javatpoint.com/how-to-set-python-path

### Terceiro passo - Start server

##### Dentro do diretório MyProject utilize o comando:

```
python manage.py runserver
```

Depois, no navegador, acesse o url

```
http://127.0.0.1:8000/accounts/login/
```
### Quarto passo - Acesso
##### Dentro da tela de loguin escolha o usuario para a sua finalidade:

| Usuario  | Senha | Função |
| ------------- | ------------- | ------------- |
| gustavo  | !@#$1234  |Relatorio|
| admin  | 123  |TUDO e gestão de usuarios|
| user1  | pass123word  |CRUD|
| user2  | pass123word  |TUDO|
| user3  | pass123word  |Atualizar|
| user4  | pass123word  |Atualizar|

#####Caso seja bloqeuado apos 3 tentativas incorretas é possivel limpar o histórico de tentativas de login de todos os usuários rode o seguinte comando:
```
python manage.py axes_reset
```

### Quinto passo - Validação
##### Acesse o documento online elaborado pelo grupo 3 para visualizar os testes de verificação
https://docs.google.com/document/d/1wSJVjkT7KQu89gZl_fc7QPbQWaPXguMn/edit



