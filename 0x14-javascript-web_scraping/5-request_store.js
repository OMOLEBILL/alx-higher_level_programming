#!/usr/bin/node
// import the fs module
const fs = require('fs');
const request = require('request');

const filepath = process.argv[3];
const url = process.argv[2];
// using the writeFile method
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  fs.writeFile(filepath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
