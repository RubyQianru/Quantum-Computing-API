class Walker {
    constructor() {
      this.x = width / 2;
      this.y = height / 2;
    }
  
    show() {
      stroke(0);
      point(this.x, this.y);
    }
  
    step() {
        let choice;
        
        websocket.onmessage = function(data) {
            choice = data
        };

        if (choice == [0,0]) {
            this.x++;
        } else if (choice == [0,1]) {
            this.x--;
        } else if (choice == [1,0]) {
            this.y++;
        } else {
            this.y--;
        }
    }
  }