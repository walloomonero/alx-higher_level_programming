#!/usr/bin/node
//The script that prints the title of a Star Wars movie
//  where the episode number matches a given integer.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
