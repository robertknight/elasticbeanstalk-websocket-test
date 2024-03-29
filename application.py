#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(f"received {message}")

async def main():
    async with serve(echo, "0.0.0.0", 8000):
        await asyncio.Future()  # run forever

asyncio.run(main())
