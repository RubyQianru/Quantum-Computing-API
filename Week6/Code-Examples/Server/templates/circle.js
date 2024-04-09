let websocket;
let x = 0;

function setup() {
  createCanvas(400, 400);
  background(255);
  websocket = new WebSocket('ws://localhost:8000/randomfloat');

  websocket.onopen = function(event) {
    console.log("Connection established");
  };

  websocket.onmessage = function(event) {
    x = parseFloat(event.data) * width; 
    if (x >= 0) { 
      drawPoint(); 
    }
  };
}

function drawPoint() {
    noStroke();
    fill(0, 10);
    circle(x, 120, 16);
  
}

