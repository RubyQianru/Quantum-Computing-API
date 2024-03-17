let websocket;
let walker;

function setup() {
  createCanvas(400, 400);
  background(255);

  websocket = new WebSocket('ws://localhost:8000/simulation');
  walker =  new Walker()
}

function draw() {
  
  walker.show()
  websocket.send("simulation")

  websocket.onmessage = function(event) {
    walker.step(event.data)
  };
}

class Walker {
  constructor() {
    this.x = width / 2;
    this.y = height / 2;
  }

  show() {
    stroke(0);
    strokeWeight(10);
    point(this.x, this.y);
  }

  step(seed) {
    if (seed == "00") {
      this.x+=10;
    } else if (seed == "10") {
      this.x-=10;
    } else if (seed == "01") {
      this.y+=10;
    } else {
      this.y-=10;
    }
  }
}


