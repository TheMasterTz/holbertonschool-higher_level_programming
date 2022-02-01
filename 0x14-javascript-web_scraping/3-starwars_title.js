#!/usr/bin/node
const request = require("request");
const user_id = process.argv[2];
const url = "https://swapi-api.hbtn.io/api/films/" + user_id;

request(url, function (error, response, body) {
  body = JSON.parse(body);
  console.log(body);
});
