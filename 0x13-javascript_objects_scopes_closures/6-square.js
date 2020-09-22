#!/usr/bin/node
// other Square class that inherit from Square::

const squareOne = require('./5-Square');

module.exports = class Square extends squareOne {
  charPrint (c = 'X') {
    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};

