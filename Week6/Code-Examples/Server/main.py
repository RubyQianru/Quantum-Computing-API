from fastapi import (
    FastAPI,
    WebSocket,
    # WebSocketException,
)
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from ConnectionManager import ConnectionManager
import utils as u

app = FastAPI()

manager = ConnectionManager()

app.mount("/static", StaticFiles(directory="templates"), name="static")

@app.get("/")
async def get():
    return FileResponse("templates/index.html")

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

async def handle_random_walker():
    return u.randomWalker()

async def handle_random_float():
    return u.randomFloat()

@app.websocket("/randomwalker")
async def websocket_endpoint_randomwalker(websocket: WebSocket):
    await websocket_connection_handler(websocket, handle_random_walker)

@app.websocket("/randomfloat")
async def websocket_endpoint_randomfloat(websocket: WebSocket):
    await websocket_connection_handler(websocket, handle_random_float)