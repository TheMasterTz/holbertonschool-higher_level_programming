#!/usr/bin/node
const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films';
let count = 0;

request(starWarsUri, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const json = JSON.parse(body).results;

    for (let i = 0; i < json.length; i++) {
      const characters = json[i].characters;

      for (let j = 0; j < characters.length; j++) {
        const character = characters[j];
        const characterId = character.split('/');

        if (characterId[5] == 18) {
          count++;
        }
      }
    }
  }

  console.log(count);
});
