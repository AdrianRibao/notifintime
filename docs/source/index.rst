.. django-users documentation master file, created by
   sphinx-quickstart on Thu Jul 19 12:19:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{ app_name }} documentation!
========================================

Contents:

.. toctree::
   :maxdepth: 2

Installation
============

.. code::

    pip install {{ app_name }}

Add ``'{{ app_name }}'`` to ``INSTALLED_APPS``

Add the URLs to urls.py:

.. code::

    # Django users
    url(r'^{{ app_name }}/', include('{{ app_name }}.urls')),

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

