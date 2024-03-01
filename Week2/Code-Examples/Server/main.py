from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse

from ConnectionManager import ConnectionManager

app = FastAPI()

manager = ConnectionManager()
@app.get("/")
async def get():
    return FileResponse("templates/index.html")

@app.websocket("/communicate")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"Received:{data}",websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.send_personal_message("Bye!!!",websocket)



