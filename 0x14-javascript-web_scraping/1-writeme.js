#!/usr/bin/node
// import the fs module
const fs = require('fs');

const filepath = process.argv[2];
const data = process.argv[3];
// using the writeFile method
fs.writeFile(filepath, data, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
