import express, { Express } from "express";
require("dotenv").config();

class App {
  public app: Express;
  private port: number;

  constructor(port: number) {
    this.app = express();
    this.port = port;
  }

  public listen() {
    this.app.listen(this.port, () => {
      console.log(`App listening on the port ${this.port}`);
    });
  }
}

export default App;
