#!/usr/bin/node

const request = require('request');
const urlApi = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(urlApi, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const charUrl = JSON.parse(body).characters;

  for (let j = 0; j < charUrl.length; j++) {
    request(charUrl[j], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
