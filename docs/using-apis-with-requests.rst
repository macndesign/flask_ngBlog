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
    # Imprimindo os cabeçálhos que vai retornar a string 'application/json; charset=utf-8'
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
    >>> import requests

    # Veja como o requests usa a mesma interface para qualquer método HTTP
    >>> r = requests.get("http://httpbin.org/get")
    >>> r = requests.post("http://httpbin.org/post")
    >>> r = requests.put("http://httpbin.org/put")
    >>> r = requests.patch("http://httpbin.org/patch")
    >>> r = requests.delete("http://httpbin.org/delete")
    >>> r = requests.head("http://httpbin.org/get")
    >>> r = requests.options("http://httpbin.org/get")

    # Você pode usar métodos simples para retornar os dados
    >>> r.text # u'[{"created_at":"2014-06-08T20:50:27-07:00","payload":{"sha...
    >>> r.encoding # 'utf-8'
    >>> r.json() # [{u'actor_attributes': {u'name': u'Tin...



Passando parametros chave/valor na URL usando o método GET
----------------------------------------------------------

Exemplo: httpbin.org/get?key=val

.. sourcecode:: python

    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.get("http://httpbin.org/get", params=payload)
    >>> print(r.url) # http://httpbin.org/get?key2=value2&key1=value1

