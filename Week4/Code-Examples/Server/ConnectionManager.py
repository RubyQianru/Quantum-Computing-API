from fastapi import WebSocket

class ConnectionManager:
    """Class defining socket events"""
    def __init__(self):
        """init method, keeping track of connections"""
        self.active_connections = []
    
    async def connect(self, websocket: WebSocket):
        """connect event"""
        await websocket.accept()
        self.active_connections.append(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        """Direct Message"""
        await websocket.send_text(message)

    async def send_data(self, data, websocket: WebSocket):
        """Direct Message: data from qc"""
        await websocket.send_text(data)
    
    def disconnect(self, websocket: WebSocket):
        """disconnect event"""
        self.active_connections.remove(websocket)
        