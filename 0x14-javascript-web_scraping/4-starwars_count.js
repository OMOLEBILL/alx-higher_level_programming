#!/usr/bin/node
const request = require('request');

const API_URL = process.argv[2];
const CHARACTER_ID = 18;

request(API_URL, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const movies = body.results.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${CHARACTER_ID}/`));
  console.log(movies.length);
});
