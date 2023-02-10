#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const baseUrl = url + process.argv[2];
request(baseUrl, { json: true }, (err, resp, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const Char = data.characters;
  Char.forEach((path) => {
    request(path, { json: true }, (err, resp, body) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(body.name);
    });
  });
});
