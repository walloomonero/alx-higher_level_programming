#!/usr/bin/node
//The script that prints the number of movies
// where the character “Wedge Antilles” is present.
const request = require('request');
let num = 0;

request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});
