#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let data;
const myDict = {};

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    data = JSON.parse(body);
    data.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in myDict)) {
          myDict[userid] = 0;
        }
        myDict[userid] += 1;
      }
    });
    console.log(myDict);
  }
});
