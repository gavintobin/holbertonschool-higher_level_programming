#!/usr/bin/node
const request = require('request');

const url = 'https://www.example.com';

request.get(url, function(error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
