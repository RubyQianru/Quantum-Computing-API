from fastapi import (
    FastAPI,
    WebSocket,
)
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import utils as u
import helper as h

app = FastAPI()
connections = []

app.mount("/static", StaticFiles(directory="templates"), name="static")

@app.get("/")
async def get():
    return FileResponse("templates/index.html")

@app.websocket("/randomwalker")
async def websocket_endpoint_randomwalker(websocket: WebSocket):
    await h.websocket_connection_handler(websocket, h.handle_random_walker)

@app.websocket("/randomfloat")
async def websocket_endpoint_randomfloat(websocket: WebSocket):
    await h.websocket_connection_handler(websocket, h.handle_random_float)


