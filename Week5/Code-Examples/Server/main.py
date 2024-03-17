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

@app.websocket("/simulation")
async def websocket_endpoint(websocket: WebSocket):
    print("WebSocket Connected")
    await manager.connect(websocket)
    print("Connection Manager Connected")

    while True:
        data_text = await websocket.receive_text()
        try:
            qcResponse = u.randomWalker()
            await manager.send_data(f"{qcResponse}",websocket)
        except ValueError:
                await websocket.send_text("Invalid integer format")




