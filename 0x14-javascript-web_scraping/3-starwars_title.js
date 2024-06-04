#!/usr/bin/node

const request = require('request');
const urlApi = 'https://swapi.co/api/films/' + process.argv[2];

request(urlApi, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
