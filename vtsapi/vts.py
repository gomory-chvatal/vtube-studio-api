# standard libraries
import asyncio
from base64 import b64encode
import json
import os

# third-party libraries
import websockets

# local libraries
from vtsapi.exceptions import *
from vtsapi.response import *
from vtsapi.request import *


class VTSSession(object):
    """Class description here!"""

    def __init__(self, name, developer, icon_path=None, port=None, debug=False):
        
        # plugin settings
        self._plugin_name = name
        self._plugin_dev = developer
        self._plugin_icon_path = icon_path
        self._debug = debug

        # vts settings
        self._api_name = 'VTubeStudioPublicAPI'
        self._api_version = '1.0'

        # websocket settings
        self._host = 'localhost'
        if port:
            self._port = port
        else:
            self._port = 8001
        self._ws = None

        # api state
        self._authenticated = False
        self._token = None
        self._request_awaiting_response = {}
        self._response_awaiting_processing = {}

    async def __aenter__(self):
        await self._ws_connect()
        return self

    async def __aexit__(self, exc_type, exc_val, traceback):
        try:
            await self._ws_close()
        finally:
            if exc_type:
                print(f'{exc_type}: {exc_val}\n{traceback}\n')

    
    # private websocket methods
    async def _ws_connect(self):

        uri = f'ws://{self._host}:{self._port}'
        if self._debug:
            print(f'Attempting to connect to {uri}')
        
        self._ws = await websockets.connect(uri)

        if self._debug:
            if self._ws.open:
                print(f'Connected to {uri}')
            else:
                print(f'Unable to connect to {uri}')

        # start listening for responses, this will run
        # until the object is destroyed
        asyncio.ensure_future(self._receive_responses())

    async def _ws_close(self):
        
        if self._ws and self._ws.open:

            if self._debug:
                (host, port) = self._ws.remote_address
                print(f'Closing websocket connected to ws://{host}:{port}')

            await self._ws.close()
            self._ws = None

    async def _receive_responses(self):
        """Listen for all incoming messages from VTS."""

        async for message in self._ws:
            response = VTSResponse(message)

            if self._debug:
                print(f'received response:\n{response}')

            if response.id in self._request_awaiting_response:
                del self._request_awaiting_response[response.id]
                self._response_awaiting_processing[response.id] = response

    async def _get_specific_response(self, request_id):
        """Wait for specific response."""

        while True:
            if request_id in self._response_awaiting_processing:
                response = self._response_awaiting_processing[request_id]
                del self._response_awaiting_processing[request_id]
                return response

            # momentarily yield control
            await asyncio.sleep(0)

    async def _send_request(self, request, track_response=True):
        """Send the request, and if response needs to be tracked add the
        request id to the queue.
        """
        
        if track_response:
            self._request_awaiting_response[request.id] = None

        if self._debug:
            print(f'preparing to send request:\n{request}')

        await self._ws.send(request.json)

    
    # private utility methods
    def _get_icon_data(self):

        # check user provided file path and revert to default if missing
        if self._plugin_icon_path and os.path.isfile(self._plugin_icon_path):
            icon_path = self._plugin_icon_path
        else:
            icon_path = os.path.join(
                os.path.dirname(__file__), 'data', 'default-icon_128.png')

        # try to load file
        if os.path.isfile(icon_path):
            try:
                with open(icon_path, 'rb') as icon_file:
                    icon_data = b64encode(icon_file.read()).decode('ascii')
            except:
                icon_data = None
        else:
            icon_data = None

        return icon_data        

    async def _get_token(self):

        # prepare and send payload
        data = {
            'pluginName': self._plugin_name,
            'pluginDeveloper': self._plugin_dev,
            'pluginIcon': self._get_icon_data()      
        }
        request = VTSRequest('AuthenticationTokenRequest', data=data)
        await self._send_request(request)
        response = await self._get_specific_response(request.id)

        if 'authenticationToken' in response.data:
            self._token = response.data['authenticationToken']

    async def _authenticate(self):
        
        # prepare and send payload
        data = {
            'pluginName': self._plugin_name,
            'pluginDeveloper': self._plugin_dev,
            'authenticationToken': self._token    
        }
        request = VTSRequest('AuthenticationRequest', data=data)
        await self._send_request(request)
        response = await self._get_specific_response(request.id)

        if 'authenticated' in response.data and response.data['authenticated']:
            self._authenticated = True

    async def _get_state(self):

        # prepare and send payload
        request = VTSRequest('APIStateRequest')
        await self._send_request(request)
        response = await self._get_specific_response(request.id)
        return response

    async def _get_stats(self):

        # prepare and send payload
        request = VTSRequest('StatisticsRequest')
        await self._send_request(request)
        response = await self._get_specific_response(request.id)
        return response

    async def _get_vts_folders(self):

        # prepare and send payload
        request = VTSRequest('VTSFolderInfoRequest')
        await self._send_request(request)
        response = await self._get_specific_response(request.id)
        return response

    async def _get_current_model(self):

        # prepare and send payload
        request = VTSRequest('CurrentModelRequest')
        await self._send_request(request)
        response = await self._get_specific_response(request.id)
        return response

    async def _get_available_models(self):

        # prepare and send payload
        request = VTSRequest('AvailableModelsRequest')
        await self._send_request(request)
        response = await self._get_specific_response(request.id)
        return response

    async def _get_available_hotkeys(self):

        # prepare and send payload
        request = VTSRequest('HotkeysInCurrentModelRequest')
        await self._send_request(request)
        response = await self._get_specific_response(request.id)
        return response

    async def _get_available_artmeshes(self):

        # prepare and send payload
        request = VTSRequest('ArtMeshListRequest')
        await self._send_request(request)
        response = await self._get_specific_response(request.id)
        return response
   
    async def _load_model(self, model_id):
        # prepare and send payload
        data = {
            'modelID': model_id 
        }
        request = VTSRequest('ModelLoadRequest', data=data)
        await self._send_request(request, track_response=False)

    async def _trigger_hotkey(self, hotkey_id):
        # prepare and send payload
        data = {
            'hotkeyID': hotkey_id
        }
        request = VTSRequest('HotkeyTriggerRequest', data=data)
        await self._send_request(request, track_response=False)

    async def _move_model(self, data):
        
        # prepare and send payload
        request = VTSRequest('MoveModelRequest', data=data)
        await self._send_request(request, track_response=False)

    async def _tint_artmesh(self, data):
        
        # prepare and send payload
        request = VTSRequest('ColorTintRequest', data=data)
        await self._send_request(request, track_response=False)
    
    
    # public methods
    async def get_state(self):
        
        response = await self._get_state()
        return response.data

    async def authenticate(self, token=None):

        # user provided token
        if token:
            self._token = token

        # keep trying to get a token and authenticate
        while True:
            if self._token:
                await self._authenticate()
                if self._authenticated == True:
                    break
            else:
                await self._get_token()

        return self._token

    async def get_stats(self):
        
        response = await self._get_stats()
        return response.data

    async def get_vts_folders(self):
        
        response = await self._get_vts_folders()
        return response.data

    async def get_current_model(self):
        
        response = await self._get_current_model()
        return response.data

    async def get_available_models(self):
        
        response = await self._get_available_models()
        return response.data

    async def get_available_hotkeys(self):
        
        response = await self._get_available_hotkeys()
        return response.data

    async def get_available_artmeshes(self):
        
        response = await self._get_available_artmeshes()
        return response.data

    async def get_available_tracking_params(self):
        fn = 'get_available_tracking_params'
        print(f'{fn} has not yet been implemented!')

    async def get_param_value(self):
        # if no param get all
        fn = 'get_param_value'
        print(f'{fn} has not yet been implemented!')

    async def load_model(self, model_id):

        await self._load_model(model_id)

    async def trigger_hotkey(self, hotkey_id):
        
        await self._trigger_hotkey(hotkey_id)

    async def move_model(self, data):
        
        await self._move_model(data)

    async def tint_artmesh(self, data):
        
        await self._tint_artmesh(data)

    async def add_custom_param(self):
        fn = 'add_custom_param'
        print(f'{fn} has not yet been implemented!')

    async def delete_custom_param(self):
        fn = 'delete_custom_param'
        print(f'{fn} has not yet been implemented!')

    async def set_param_value(self):
        fn = 'set_param_value'
        print(f'{fn} has not yet been implemented!')
