let websocket;
let line;
let t = 0.0;

function setup() {
  createCanvas(400, 400);
  background(255);

  websocket = new WebSocket('ws://localhost:8000/randomfloat');
}

function draw() {

  noFill();
  stroke(0);
  strokeWeight(2);

  websocket.send();
  websocket.onmessage = function(event) {

    beginShape();
    for (let i = 0; i < width; i++) {
      let y = event.data * height;
      xoff += 0.01;
      vertex(i, y);
    }
    endShape();
    t += 0.01;
  };
}




