from fastapi import WebSocket
from ConnectionManager import ConnectionManager
import asyncio
import utils as u

manager = ConnectionManager()

async def websocket_connection_handler(websocket: WebSocket, data_handler):
    print("WebSocket Connected")
    await manager.connect(websocket)
    print("Connection Manager Connected")

    try:
        while True:
            qcResponse = await data_handler()
            await manager.send_data(f"{qcResponse}", websocket)
            await asyncio.sleep(0.5)  

    except asyncio.CancelledError:
        print("WebSocket connection closed by client.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        manager.disconnect(websocket)
        print("WebSocket Disconnected")

async def handle_random_walker():
    return u.randomWalker()

async def handle_random_float():
    return u.randomFloat()