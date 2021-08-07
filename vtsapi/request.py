# standard libraries
from datetime import datetime
import json

# local libraries
from vtsapi.exceptions import *


def id_generator():
    current_id = 0
    while current_id := 1 if current_id >= 2147483647 else current_id + 1:
        yield current_id


class VTSRequest(object):
    """Object takes request type and optional dictionary and produces JSON
    request for VTS.
    """

    next_id = id_generator()

    def __init__(self, msg_type, data=None, api_name='VTubeStudioPublicAPI',
            api_version='1.0'):

        self._id = next(self.next_id)
        self._send_time = None
        self._msg_type = msg_type
        self._payload = {
            'apiName': api_name,
            'apiVersion': api_version,
            'requestID': str(self._id),
            'messageType': self._msg_type
        }
        if data:
            self._payload['data'] = data

    @property
    def id(self):
        return self._id

    @property
    def send_time(self):
        return self._send_time

    @property
    def msg_type(self):
        return self._msg_type

    @property
    def payload(self):
        return self._payload

    @property
    def json(self):
        # the first time the JSON is accessed the request is marked as sent
        if not self._send_time:
            self._send_time = int(datetime.now().timestamp()*1000)
        return json.dumps(self._payload)

    def __str__(self):
        return f'request {self._id} {self._msg_type}:\n{self._payload}'

    def __repr__(self):
        return self.__str__()
