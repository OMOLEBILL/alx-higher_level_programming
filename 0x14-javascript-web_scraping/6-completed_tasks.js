#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const userDict = {};

  body.forEach((todo) => {
    if (todo.completed) {
      if (userDict[todo.userId]) {
        userDict[todo.userId]++;
      } else {
        userDict[todo.userId] = 1;
      }
    }
  });
  console.log(userDict);
});
