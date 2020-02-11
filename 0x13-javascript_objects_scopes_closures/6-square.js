#!/usr/bin/node
const Square2 = require('./5-square.js');

module.exports = class Square extends Square2 {
  charPrint (c) {
    let x = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      x += c;
    }

    for (let j = 0; j < this.height; j++) {
      console.log(x);
    }
  }
};
