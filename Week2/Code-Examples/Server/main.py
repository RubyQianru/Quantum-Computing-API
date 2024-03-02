from fastapi import (
    FastAPI,
    WebSocket,
    WebSocketException,
)
from fastapi.responses import FileResponse
from ConnectionManager import ConnectionManager
import utils as u

app = FastAPI()

manager = ConnectionManager()
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
            data_integer = int(data_text)
            print(f"Received integer data: {data_integer}")
            qcResponse = u.generateNoise(data_integer)
            await manager.send_data(f"Received:{qcResponse}",websocket)

        except ValueError:
                await websocket.send_text("Invalid integer format")




