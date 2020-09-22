#!/usr/bin/node
const { list } = require('./100-data');

const thelist = list.map((element, index) => {
  return (element * index);
});
console.log(list);
console.log(thelist);

