

export default class StreamClient {

  base_url = `ws://${import.meta.env.VITE_BACKEND_HOST}/stream/`;

  constructor(path) {
    this.url = this.base_url + path;
    this.ws = null;
  }

  run (func, params={}) {
    this.open(params)
    this.ws.onmessage = (event) => func(event.data);
    window.onbeforeunload = () => this.close()
  }

  open (params = {}) {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => {  
      this.ws.send(JSON.stringify(params));
    }
  }

  close () {
    this.ws.close();
  }

}
