# standard libraries
from datetime import datetime
import json

# local libraries
from vtsapi.exceptions import *


class VTSResponse(object):
    """Response object takes a JSON response from VTS, parses the JSON, and
    raises any errors.
    """

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

    def __str__(self):
        return f'response {self._id} {self._msg_type}:\n{self._payload}'

    def __repr__(self):
        return self.__str__()

    def check_error(self):
        
        if self._msg_type == 'APIError':
            error_id = self._data['errorID']

            # general errors
            if error_id == 0:
                raise VTSInternalServerError()
            elif error_id == 1:
                raise VTSAPIAccessDeactivated()
            elif error_id == 2:
                raise VTSJSONInvalid()
            elif error_id == 3:
                raise VTSAPINameInvalid()
            elif error_id == 4:
                raise VTSAPIVersionInvalid()
            elif error_id == 5:
                raise VTSRequestIDInvalid()
            elif error_id == 6:
                raise VTSRequestTypeUnknown()
            elif error_id == 7:
                raise VTSRequestTypeMissingOrEmpty()
            elif error_id == 8:
                raise VTSRequestRequiresAuthetication()

            # token request related errors
            elif error_id == 50:
                raise VTSTokenRequestDenied()
            elif error_id == 51:
                raise VTSTokenRequestCurrentlyOngoing()
            elif error_id == 52:
                raise VTSTokenRequestPluginNameInvalid()
            elif error_id == 53:
                raise VTSTokenRequestDeveloperNameInvalid()
            elif error_id == 54:
                raise VTSTokenRequestPluginIconInvalid()

            # authentication request related errors
            elif error_id == 100:
                raise VTSAuthenticationTokenMissing()
            elif error_id == 101:
                raise VTSAuthenticationPluginNameMissing()
            elif error_id == 102:
                raise VTSAuthenticationPluginDeveloperMissing()

            # model load related errors
            elif error_id == 150:
                raise VTSModelIDMissing()
            elif error_id == 151:
                raise VTSModelIDInvalid()
            elif error_id == 152:
                raise VTSModelIDNotFound()
            elif error_id == 153:
                raise VTSModelLoadCooldownNotOver()
            elif error_id == 154:
                raise VTSCannotCurrentlyChangeModel()

            # hotkey trigger request related errors
            elif error_id == 200:
                raise VTSHotkeyQueueFull()
            elif error_id == 201:
                raise VTSHotkeyExecutionFailedBecauseNoModelLoaded()
            elif error_id == 202:
                raise VTSHotkeyIDNotFoundInModel()
            elif error_id == 203:
                raise VTSHotkeyCooldownNotOver()
            elif error_id == 204:
                raise VTSHotkeyIDFoundButHotkeyDataInvalid()
            elif error_id == 205:
                raise VTSHotkeyExecutionFailedBecauseBadState()
            elif error_id == 206:
                raise VTSHotkeyUnknownExecutionFailure()

            # color tint request related errors
            elif error_id == 250:
                raise VTSColorTintRequestNoModelLoaded()
            elif error_id == 251:
                raise VTSColorTintRequestMatchOrColorMissing()
            elif error_id == 252:
                raise VTSColorTintRequestInvalidColorValue()

            # model move request related errors
            elif error_id == 300:
                raise VTSMoveModelRequestNoModelLoaded()
            elif error_id == 301:
                raise VTSMoveModelRequestMissingFields()
            elif error_id == 302:
                raise VTSMoveModelRequestValuesOutOfRange()        
