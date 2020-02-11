#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const charac of film.characters) {
        if (charac.search('/18/') > 0) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
