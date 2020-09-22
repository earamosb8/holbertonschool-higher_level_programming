#!/usr/bin/node
// count print:
let con = 0;
exports.logMe = function (item) {
  console.log(con + ': ' + item);
  con += 1;
};
