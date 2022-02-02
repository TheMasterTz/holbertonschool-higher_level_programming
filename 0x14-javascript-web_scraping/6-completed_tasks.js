#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const tacksDisct = {};
    const json = JSON.parse(body);

    for (let i = 0; i < json.length; i++) {
      const userId = json[i].userId;
      const completed = json[i].completed;

      if (!tacksDisct[userId]) {
        tacksDisct[userId] = 0;
      }
      if (completed) ++tacksDisct[userId];
    }
    console.log(tacksDisct);
  }
});
