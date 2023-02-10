#!/usr/bin/node
const request = require('request');

const API_URL = process.argv[2];

request(API_URL, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const movies = body.results;
  let length = 0;
  movies.forEach(movie => movie.characters.forEach(charUrl => {
    if (charUrl.slice(-3, -1) === '18') {
      length++;
    }
  }));
  console.log(length);
});
