.. image:: http://img.ge/images/31651738274206239600.png
  :target: https://github.com/FZX/url-shortener
  :alt: Url-shortener Logo
  :align: right


.. _Python: http://python.org/
.. _Bottlepy: http://bottlepy.org/
.. _SQLAlchemy: http://sqlalchemy.org/
.. _plugin: https://github.com/iurisilvio/bottle-sqlalchemy
.. _greenlent: https://greenlet.readthedocs.io/en/latest/
.. _gevent: http://www.gevent.org/
.. _Validation: https://validators.readthedocs.io/en/latest/




============================
URL-Shortener
============================

URL-Shortener is simple service built using Bottlepy.
Used packages.

* **Bottlepy** is a fast, simple and lightweight WSGI_ micro web-framework for Python_. It is distributed as a single file module and has no dependencies other than the `Python Standard Library <http://docs.python.org/library/>`_..
* **SqlAlchemy:** as their site says SQLAlchemy_ is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL..
* **Bottle-SQLAlchemy:** plugin_ integrates SQLAlchemy with Bottle application. It injects a SQLAlchemy session in route and handle the session cycle.
* **Gevent:** gevent_ is a coroutine -based Python_ networking library that uses greenlet to provide a high-level synchronous API on top of the libev event loop.
* **Validators:** Python_ Data Validation_ for Humans™.


Example: Simple developer api
----------------------------------

.. code-block:: javascript

   var request = $.ajax({
       url: "http://yoursite.com/api",
       method: "POST"
       data: {
           link: "http://github.com"
       },
       success: function(response){
           console.log(response.status);
           console.log(response.url);
       }
   })

Post to api with jquery and you will get json object back with status and shrinked url.

.. code-block:: python

   import requests

   data = {"link": "github.com"}
   respond = requests.post("http://yoursite.com/api", params=data)
   print(respond.text)


Post to api with requests module


Download and Setup
--------------------

.. __: https://github.com/FZX/Url-shortener/raw/master/app.py

* First you need to get this repository on your machine ``git clone https://github.com/FZX/url-shortener.git``
* Move to directory ``cd url-shortener``
* Install all necessary packages ``pip3 install -r requirements.txt`` . 
* Change variable ``site`` to your address.
Url-Shortener runs with **Python 3.3+**.

License
-------

.. __: https://github.com/FZX/url-shortener/raw/master/LICENSE

Code and documentation are available according to the GPL 3.0 License (see LICENSE__).

The Url-Shortener logo however is *NOT* covered by that license. It is allowed to use the logo as a link to the Url-shortener page. In all other cases please ask first.
