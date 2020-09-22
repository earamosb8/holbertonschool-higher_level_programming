#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
