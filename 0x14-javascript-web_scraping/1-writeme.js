#!/usr/bin/node
// write a file and print the content
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
