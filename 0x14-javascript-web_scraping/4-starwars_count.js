#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let movies = JSON.parse(body).results;
    for (let movie of movies) {
      for (let character of movie.characters) {
        if (character.endsWith('/18/')) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
