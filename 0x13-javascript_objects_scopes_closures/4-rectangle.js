#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    const p = 'X';
    let i = 0;
    while (i < this.height) {
      console.log(p.repeat(this.width));
      i++;
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}
module.exports = Rectangle;
