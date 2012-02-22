Jaconda API
===========

The unofficial python wrapper for working with the 
`Jaconda REST API <http://help.jaconda.im/kb/api-v2/jaconda-api-documentation>`_ 
interface

Installation
------------

    python setup.py install


Requirements
------------

Python requests library


Usage
-----

- Sending Notifications::

    from jaconda.api import Notification
    client = Notification("subdomain", "room_name", "room_token")
    client.notify("Test from API")