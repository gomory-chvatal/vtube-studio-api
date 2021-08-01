# standard libraries
from datetime import datetime
import json

# local libraries
from vtsapi.exceptions import *


class VTSResponse(object):
    """Docstring goes here!"""

    def __init__(self, payload):
        
        self._payload = json.loads(payload)
        self._id = int(self._payload['requestID'])
        self._vts_timestamp = int(self._payload['timestamp'])
        self._recv_time = int(datetime.now().timestamp()*1000)
        self._msg_type = self._payload['messageType']
        self._data = self._payload['data']

    @property
    def id(self):
        return self._id

    @property
    def vts_timestamp(self):
        return self._vts_timestamp
    
    @property
    def recv_time(self):
        return self._recv_time
    
    @property
    def msg_type(self):
        return self._msg_type

    @property
    def data(self):
        return self._data
