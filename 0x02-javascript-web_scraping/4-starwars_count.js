#!/usr/bin/node
const request = require('request');

const id = '18'
const url = 'https://swapi-api.hbtn.io/api/films/' + id

request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
  
    const data = JSON.parse(body);
    const films = data.results;
  
    const numMoviesWithWedgeAntilles = films.reduce((count, film) => {
      if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${id}/`)) {
        return count + 1;
      } else {
        return count;
      }
    }, 0);
  
    console.log(`Number of movies with Wedge Antilles: ${numMoviesWithWedgeAntilles}`);
  });


