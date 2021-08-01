# VTube Studio API
Library for working with the [VTube Studio API](https://github.com/DenchiSoft/VTubeStudio).

I am doing this for fun and learning. I am not an expert so please don't learn any bad habits from this project. All constructive feedback and/or suggestions are welcome.

Use the current version at your own risk, as I play with this more I may significantly change the architecture.

I also have not implemented any error handling or documentation.

## Example Usage
```python
# standard libraries
import asyncio

# third-party libraries
from vtsapi import *

# plugin settings, icon MUST be 128x128 PNG
name = 'My Test Plugin'
developer = 'Gomory Chvatal'
icon_path = 'gomory-idea_128.png'
app_token = 'f8a47bed2e2ec3e9b8102ea5ff390b9ebb1318f00f262c70142022c1e85cb836'

# app control logic goes here
async def app_control_loop():
    async with VTSSession(name, developer, icon_path) as vts:

        # THIS MUST BE THE FIRST METHOD CALLED
        # There is probably a better way to do this, but I am terrible at
        # concurrency in python
        print(f'Starting: "{vts._plugin_name}"')
        asyncio.ensure_future(vts.start())
        
        # authenticate, save token if you don't want the user to have to
        # approve every time
        token = await vts.authenticate(app_token)
        print(f'authenticated with token:\n{token}\n\n')

        # test some of the various requests
        state = await vts.get_state()
        print(f'state:\n{state}\n\n')

        stats = await vts.get_stats()
        print(f'stats:\n{stats}\n\n')

        folders = await vts.get_vts_folders()
        print(f'folders:\n{folders}\n\n')

        current_model = await vts.get_current_model()
        print(f'current_model:\n{current_model}\n\n')

        all_models = await vts.get_available_models()
        print(f'all_models:\n{all_models}\n\n')

        hotkeys = await vts.get_available_hotkeys()
        print(f'hotkeys:\n{hotkeys}\n\n')

        artmeshes = await vts.get_available_artmeshes()
        print(f'artmeshes:\n{artmeshes}\n\n')

        # this will depend on your setup
        #await vts.load_model('c90aca0edc39484881a4a8e3bc3841cc') # akari
        #await asyncio.sleep(15)
        #await vts.load_model('eb23674409ba4ef4937611da23840758') # gomory
        #await asyncio.sleep(5)
        
        #await vts.trigger_hotkey('f04ed6a1f24e4ceb8d5dabaf27db3ec6') # game mode
        #await asyncio.sleep(5)
        #await vts.trigger_hotkey('f04ed6a1f24e4ceb8d5dabaf27db3ec6') # game mode
        #await asyncio.sleep(5)

        # move model
        for i in range(360):
            data = {
                'timeInSeconds': 0.0167,
                'valuesAreRelativeToModel': True,
                'positionX': 0.0,
                'positionY': 0.0,
                'rotation': 10.0,
                'size': 0.0
            }
            await vts.move_model(data)
            await asyncio.sleep(0.0167)
        await asyncio.sleep(3)

        # tint artmesh
        for i in range(256):
            data = {
                'colorTint': {
                    'colorR': 255,
                    'colorG': 255,
                    'colorB': 255,
                    'colorA': 255 - i
                },
                'artMeshMatcher': {'tintAll': True}
            }
            await vts.tint_artmesh(data)
            await asyncio.sleep(0.0167)
        for i in range(256):
            data = {
                'colorTint': {
                    'colorR': 255,
                    'colorG': 255,
                    'colorB': 255,
                    'colorA': 0 + i
                },
                'artMeshMatcher': {'tintAll': True}
            }
            await vts.tint_artmesh(data)
            await asyncio.sleep(0.0167)
        await asyncio.sleep(3)


# run till control logic is complete
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(app_control_loop())
```