Design
======

Installation
============

pip install notifications

Setup
=====

Add to installed apps

Getting started
===============

Create a file named `notifications`

Create class that extends `notifications.Notification`

Register the Notification

Backends
========

Configure in settings:

Email

Zeromq

Notifications
=============

Extending the base class:

Methods:

* n = Notification(id, from, to=[], message, short_message, backends=[])
  n.send()

* Receive:
  n = Notificaiont(id)
  n.filter(prefix)
  message = n.listen()

Required methods:

* One

