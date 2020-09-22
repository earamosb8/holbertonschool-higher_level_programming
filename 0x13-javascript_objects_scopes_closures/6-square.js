#!/usr/bin/node
// other Square class that inhererit from Square
const SquareOne = require('./5-Square');

module.exports = class Square extends SquareOne {
  charPrint (c = 'X') {
    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};