#!/usr/bin/node
// increments and calls a function
exports.addMeMaybe = function (number, myFunction) {
  number += 1;
  myFunction(number);
};
