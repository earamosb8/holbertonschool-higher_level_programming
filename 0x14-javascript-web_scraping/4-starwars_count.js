#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    for (const element of data.results) {
      for (const character of element.characters) {
        if (character.includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
