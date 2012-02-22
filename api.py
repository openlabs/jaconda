# -*- coding: utf-8 -*-
"""
    api

    Python API for Jaconda

    :copyright: (c) 2012 by Openlabs Technologies & Consulting (P) LTD
    :license: BSD, see LICENSE for more details.
"""
import json
import requests
from requests.auth import HTTPBasicAuth


class Notification(object):
    """
    Send notifications from your systems to Jaconda rooms.
    """

    path = property(
        lambda self: "/api/v2/rooms/%s/notify.xml" % self.room_id
    )
    site = property(
        lambda self: "https://%s.jaconda.im" % self.subdomain
    )

    def __init__(self, subdomain, room_id, room_token):
        self.subdomain = subdomain
        self.room_id = room_id
        self.room_token = room_token
        self.password = "x"

    def notify(self, text, kind='api', sender_name="Python API"):
        """
        Says something in the room.

        :param text: The text of the message. The value must pass xhtml
                     validation. Allowed tags are: a, br, em, b, i, span.
                     All other tags will be removed. Don't forget to escape
                     special characters.
        :param kind: The kind of the message. Can be chat (default), me or 
                     voice.
        """
        data = {
            'message': {
                'text': text,
                'kind': kind,
                'sender-name': sender_name,
            }
        }
        return requests.post(
            self.site + self.path,
            data = json.dumps(data),
            auth = HTTPBasicAuth(self.room_token, self.password),
            headers = {'Content-Type': 'application/json'},
        )
