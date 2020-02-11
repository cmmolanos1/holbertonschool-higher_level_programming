#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = body;
    try {
      fs.writeFileSync(process.argv[3], content, 'utf-8');
    } catch (err) {
      console.error(err);
    }
  }
});
