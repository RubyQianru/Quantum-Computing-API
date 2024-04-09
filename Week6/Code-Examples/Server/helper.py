from fastapi import WebSocket
from ConnectionManager import ConnectionManager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

manager = ConnectionManager()


async def websocket_connection_handler(websocket: WebSocket, data_handler):
    print("WebSocket Connected")
    await manager.connect(websocket)
    print("Connection Manager Connected")

    while True:
        data_text = await websocket.receive_text()
        try:
            qcResponse = await data_handler()
            await manager.send_data(f"{qcResponse}", websocket)
        except ValueError:
            await websocket.send_text("Invalid format")