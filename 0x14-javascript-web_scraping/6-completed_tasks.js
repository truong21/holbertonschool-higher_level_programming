#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let task = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (let user of JSON.parse(body)) {
      if (user.completed === true) {
        if (!(user.userId in task)) {
          task[user.userId] = 1;
        } else {
          task[user.userId] = task[user.userId] + 1;
        }
      }
    }
  }
  console.log(task);
});
