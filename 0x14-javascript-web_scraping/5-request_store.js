#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const file = process.argv[3];
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
