#!/usr/bin/node
// returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let con = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      con += 1;
    }
  }
  return con;
};
