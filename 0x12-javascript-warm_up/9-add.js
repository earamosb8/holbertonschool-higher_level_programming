#!/usr/bin/node
// script that prints the addition of 2 integers

function add (a, b) {
  console.log(a + b);
}
const numOne = parseInt(process.argv[2]);
const numTwo = parseInt(process.argv[3]);
if (Number.isInteger(numOne) && Number.isInteger(numTwo)) {
  add(numOne, numTwo);
} else {
  console.log('NaN');
}
