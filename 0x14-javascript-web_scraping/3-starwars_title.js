#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const userid = args[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + userid;

request(url, function (error, response, body) {
  body = JSON.parse(body);
  console.log(body);
});
