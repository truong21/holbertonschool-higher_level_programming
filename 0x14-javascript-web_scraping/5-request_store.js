#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.appendFile(file, body, function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
