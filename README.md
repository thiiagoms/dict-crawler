###  Crawler no dicionário da UOL

Fala Dev! Tudo bem com você ?! Espero que esteja tudo nos "conformes" :smiley: . Bom, pelo título, essa aplicação se trata de um crawler (fase beta ainda hehe) que recebe como valor na sua URL e consulta o primeiro resultado no dicionário da UOL. Existem algumas features que ainda precisam ser implementadas, como por exemplo.
  - Dependendo do valor passado, o crawler retorna a tag <br/>, o que é um bug que precisa ser corrigido :bug:
  - Tornar a aplicação uma  API RestFul, seguindo os melhores padrões de programação (Se você não sabe o que é uma API, não se preocupe, você pode clicar [aqui](http://https://www.youtube.com/watch?v=vGuqKIRWosk "aqui") e conhecer um pouco mais sobre esse recurso maravilhoso, depois me conta o que achou! :thumbsup: )
### Instalando os requisitos do projeto.

- Para não poluir o seu ambiente, recomendo criar um virtualenv ou subir um container (qualquer imagem Linux com Python já serve!). Em distros Debian *like* (Ubuntu, Mint, Debian, Deepin, etc), é necessário instalar o módulo venv do python3, para isso, em seu termina,  copie e cole ou simplesmente digite o seguinte comando:

```
 sudo apt install python3-venv
```

- Agora vamos clonar o projeto.

```
git clone https://github.com/ekkopy/dict-crawler.git
```
-  Vamos entrar dentro do nosso repo, criar nosso ambiente virtual e instalar suas respectivas dependências!
-- Entrando no diretório do nosso repo. Atenção! Se você passar um segundo nome como parametro ao clonar o repositório, o git irá "renomear" o nome do repo para o parametro passado, por isso atenção ao clonar! 

```
cd dict-crawler
```
- Criando nosso venv

```
python3 -m venv venv
```
- Ativando nosso ambiente virtual

 -- Em ambientes GNU/Linux`
```
  source venv\bin\activate
```
-- Em ambientes Windows

```
 .\venv\Scripts\activate.bat
```
- Instalando nossas dependências.

```
pip3 install -r requirements.txt
```
- Execute as migrations do django

```
  python manage.py migrate
```

# Como utilizar:

- Após executar as migrations é bem simples! Primeiro você deve iniciar o server do django, atráves do comando:
```
 python manage.py runserver
```
- Após isso no browser de sua escolhe, acesso o endereço http://localhost:8000/{com o valor que deseja}. Ex:
```
 http://localhost:8000/bola
```
- E será retornado a primeira definição de bola :balloon:
- O crawler ainda se encontra em desenvolvimento enquanto avanços com meus estudos no assunto. O dict-crawler definitivamente nasceu da noite pra dia, mas seu ideal significa muito pra mim e gostaria de partilhar com a comunidade! Qualquer PR será bem vindo e sinta-se livre para usar da maneira que achar melhor! Muito obrigado pela atenção and *see you!*
