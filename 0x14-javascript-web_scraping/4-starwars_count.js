#!/usr/bin/node
const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/';
const movies = 0;

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  console.log(movies);
});
