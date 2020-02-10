#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let x = '';
    for (let i = 0; i < this.width; i++) {
      x += c;
    }

    for (let j = 0; j < this.height; j++) {
      console.log(x);
    }
  }
};
