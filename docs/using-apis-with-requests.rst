Utilizando o módulo Requests para trabalhar com APIs
====================================================

O Python possui uma lib nativa chamada urllib2 que nos fornece a interface necessária para trabalhar com todos os
métodos HTTP programando em alto nível, porém, isso não significa que vamos usar os métodos de uma forma mais "humana".

Foi para isso que o Kenneth Reitz (@kennethreitz, engenheiro de APIs do Heroku). Criou o Requests. Para tornar simples
as tarefas que devem ser simples.

Começando com um exemplo básico de uso do módulo Requests com a API do github:

.. sourcecode:: python

    # Importando a lib Requests
    import requests

    # Instanciando um objeto requests "r" que usa o método get para acessar o endpoint da API do github
    # e passando como parametro o usuário e a senha
    r = requests.get('https://api.github.com', auth=('user', 'pass'))

    # Imprimindo o status code que vai retornar ok (código: 200)
    print(r.status_code)
    # Imprimindo os Headers que vai retornar a string 'application/json; charset=utf-8'
    print(r.headers['content-type'])



Instalação
----------

Antes de tudo é necessário ter o Python instalado na máquina.

Máquinas com S.O. Linux e Mac já possuem o Python instalado e para instalar no Windows é bem simples.
Basta ir no site oficial https://www.python.org/downloads/ baixar e instalar a ultima versão.

Após ter o Python instalado em sua máquina, é muito aconselhado utilizar o pip (package manager) do python para instalar
libs externas.

Para instalar o pip, basta fazer download do script para baixar e instalar o pip: https://bootstrap.pypa.io/get-pip.py

Após o download é necessário abrir o terminal no mesmo diretório do script do pip e executar com: ``python get-pip.py``.

Caso o comando python não execute em seu terminal é porquê na hora da instalação não foi inserido automaticamente no
path do Windows. Então adicione no Path do Windows o caminho do Python que geralmente é ``C:\Python27\python``.

    Obs.: ``C:\Python27\python`` quer dizer que sua instalação do Python foi a 2.7 para 3.4 deve ser Python34. Para
    saber o certo basta olhar onde você instalou.

Após ter o Python e o pip instalado você poderá instalar facilmente milhões de libs #superlegais que só o python tem :D
e então basta executar: ``pip install requests``.



Criando seus primeiros requests com sua nova lib
------------------------------------------------

Abra o cmd (terminal), digite python e dê enter para entrar no modo interativo da linguagem.

.. sourcecode:: python

    # Importando a lib
    import requests

    # Veja como o requests usa a mesma interface para qualquer método HTTP
    r = requests.get("http://httpbin.org/get")
    r = requests.post("http://httpbin.org/post")
    r = requests.put("http://httpbin.org/put")
    r = requests.patch("http://httpbin.org/patch")
    r = requests.delete("http://httpbin.org/delete")
    r = requests.head("http://httpbin.org/get")
    r = requests.options("http://httpbin.org/get")

    # Você pode usar métodos simples para retornar os dados
    r.text # u'[{"created_at":"2014-06-08T20:50:27-07:00","payload":{"sha...
    r.encoding # 'utf-8'
    r.json() # [{u'actor_attributes': {u'name': u'Tin...



Passando parametros chave/valor na URL usando o método GET
----------------------------------------------------------

Exemplo: httpbin.org/get?key=val

.. sourcecode:: python

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)
    print(r.url) # http://httpbin.org/get?key2=value2&key1=value1



Vamos supor que você queira recuperar a listagem de seus repositórios usando a API do github, mas não quer apenas
a listagem, quer aproveitar um recurso da própria API do github que pode navegar para uma página específica (page) e
dizer a quantidade de itens por página (per_page).

.. sourcecode:: python

    params = {'page': 2, 'per_page':100}
    r = requests.get('https://api.github.com/user/repo/', params=params)
    print(r.url) # https://api.github.com/user/repos?page=2&per_page=100



Passando Headers customizados
--------------------------------

Para passar Headers customizados em uma requisição basta passar um simples dicionário Python para o parametro headers.
Por exemplo se quiser passar um content-type na requisição do exemplo anterior.

.. sourcecode:: python

    import json
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(payload), headers=headers)



Como a grande maioria das APIs exigem um access token para que possa ser obtido os dados, vamos adicionar esse access
token ao header.

.. sourcecode:: python

    # Supondo que você guardou o token na variável token e seu endpoint na variável url
    headers = {'Authorization': 'token {0}'.format(token)}
    params  = {'page': 2, 'per_page': 100}
    r = requests.get(url, params=params, headers=headers)



Se no caso sua autenticação for do tipo basic, por exemplo com email@domain.com:password encoded para base 64.

.. sourcecode:: python

    import base64
    encoded = base64.b64encode('{0}:{1}'.format(email, password))
    headers = {'Authorization': 'Basic {0}'.format(encoded)}
    params  = {'page': 2, 'per_page': 100}
    r = requests.get(url, params=params, headers=headers)



Status codes
------------

Podemos checar facilmente os status codes para o response da seguinte forma.

.. sourcecode:: python

    r = requests.get('http://httpbin.org/get')
    r.status_code
    200


Se o request for alguns do tipo bad request como 4XX ou 5XX, podemos lançar a excessão com a
classe ``Response.raise_for_status()``

.. sourcecode:: python

    # Testando no interpretador interativo do python (terminal)
    >>> bad_r = requests.get('http://httpbin.org/status/404')
    >>> bad_r.status_code
    404

    >>> bad_r.raise_for_status()
    Traceback (most recent call last):
    File "requests/models.py", line 832, in raise_for_status
        raise http_error
    requests.exceptions.HTTPError: 404 Client Error

    Response.raise_for_status() returns None for status_code 200
