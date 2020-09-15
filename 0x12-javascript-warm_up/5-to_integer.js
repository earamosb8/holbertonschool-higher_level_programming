#!/usr/bin/node
// script that prints My number: <first argument converted in integer>
const myNum = parseInt(process.argv[2]);
if (Number.isInteger(myNum)) {
  console.log('My number: ' + myNum);
} else {
  console.log('Not a number');
}
