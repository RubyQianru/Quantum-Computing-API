let websocket;
let line;

function setup() {
  createCanvas(400, 400);
  background(255);

  websocket = new WebSocket('ws://localhost:8000/randomfloat');
  line =  new Line()
}

function draw() {
  
  walker.show()
  websocket.send("simulation")

  websocket.onmessage = function(event) {
    walker.step(event.data)
  };
}

class Line {
  constructor() {

    this.t = 0.0;
  }

  show() {
    beginShape();
    for (let i = 0; i < width; i+= 1) {
      let y = 
    }
  }

  step(seed) {

  }
}


