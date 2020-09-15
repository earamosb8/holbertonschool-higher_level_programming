#!/usr/bin/node
// script that prints a square
if (process.argv.length === 2) {
  console.log('Missing size');
} else if (process.argv.length === 3) {
  const num = parseInt(process.argv[2]);
  if (Number.isInteger(num) && num >= 0) {
    for (let i = 0; i < process.argv[2]; i++) {
      console.log('X'.repeat(num));
    }
  } else {
    console.log('Missing size');
  }
}
