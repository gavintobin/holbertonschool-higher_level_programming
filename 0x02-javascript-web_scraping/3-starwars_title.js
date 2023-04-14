#!/usr/bin/node
const request = require('request');

const movie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movie;

request.get(url, function (err, response, body) {
    if (err) throw err;
    console.log(JSON.parse(body).title);
});
