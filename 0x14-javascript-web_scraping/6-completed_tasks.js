#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
const request = require('request');
const result = {};
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const jsn = JSON.parse(body);
    for (const task of jsn) {
      if (task.completed) {
        if (task.userId in result) {
          result[task.userId] += 1;
        } else {
          result[task.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
