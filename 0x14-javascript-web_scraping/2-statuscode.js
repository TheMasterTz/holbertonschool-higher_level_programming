#!/usr/bin/node
const request = require('request');
const url = process.argv[2]

request(url, function (error, res) {
  if (error) {
    console.log(err);
  } else {
    console.log('code:', res.statusCode);
  }
});