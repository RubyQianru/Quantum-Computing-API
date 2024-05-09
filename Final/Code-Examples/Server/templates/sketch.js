let websocket;
let x = 0;
let arr = [];

function setup() {
  createCanvas(windowWidth, 400);
  background(255);
  websocket = new WebSocket('ws://localhost:8000/randomfloat');

  websocket.onopen = function(event) {
    console.log("Connection established");
  };

  websocket.onmessage = function(event) {
    y = parseFloat(event.data) * height; 
    if (y >= 0) { 
      arr.push(y);
      drawCurve(); 
    }
  };
}

function draw() {
  websocket.send("Heartbeat");
}

function drawCurve() {
  background(255);
  stroke(0);
  strokeWeight(2);
  beginShape();
  for (let i = 0; i < arr.length; i += 1) {
    curveVertex(i*10, arr[i]);
  }
  endShape();

}

