#!/usr/bin/node
// script that display the status code of a GET request.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
