#!/usr/bin/node

// A script that prints all characters of a Star Wars movie:

const request = require('request');
const episodeId = process.argv[2];
const url = `https://swapi.dev/api/films/${episodeId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});