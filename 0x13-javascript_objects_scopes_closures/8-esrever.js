#!/usr/bin/node
//  reversed version of a list:

exports.esrever = function (list) {
  const revlist = [];
  for (const i in list) {
    revlist.push(list[list.length - i - 1]);
  }
  return revlist;
};
