let websocket;

function setup() {
  createCanvas(400, 400);
  
  websocket = new WebSocket('ws://localhost:8000/simulation');
  
  websocket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    console.log('Received:', data);
    background(255);
    fill(0);
    textSize(20);
    text('Random Number: ' + data.random_number, 50, height/2);
  };
}

function draw() {
  websocket.send()
}

