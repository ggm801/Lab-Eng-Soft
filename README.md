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
ou
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
http://localhost:8000
```

##### Dentro da tela de loguin escolha o usuario para a sua finalidade:

| Usuario  | Senha | Função |
| ------------- | ------------- | ------------- |
| gustavo  | !@#$1234  |CRUD|
| admin  | 123  |TUDO|
| user1  | pass123word  |Relatorio|
| user2  | pass123word  |Atualizar Voo|
