#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
      if (w <= 0 || h <= 0) {
        // create an empty object if either w or h is 0 or negative
        return;
      }
      this.width = w;
      this.height = h;
    }
  }
