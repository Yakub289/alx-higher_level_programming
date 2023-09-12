#!/usr/bin/node

// Write a class Square that defines a square and inherits from Square of 5-square.js:

// You must use the class notation for defining your class and extends
// Create an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X.

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const symbolic = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let dynamics = '';
      let y = 0;
      while (y < this.width) {
        dynamics += symbolic;
        y++;
      }
      console.log(dynamics);
    }
  }
}
module.exports = Square;
