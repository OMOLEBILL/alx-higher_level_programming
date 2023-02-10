#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const num = process.argv[2];
const BaseUrl = url + num;

request(BaseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const movieTitle = data.title;
  console.log(movieTitle);
});
