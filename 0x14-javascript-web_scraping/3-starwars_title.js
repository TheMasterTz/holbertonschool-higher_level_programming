#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const user_id = args[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + user_id;

request(url, function (error, response, body) {
  body = JSON.parse(body);
  console.log(body);
});
