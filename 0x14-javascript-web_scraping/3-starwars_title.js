#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const resobj = JSON.parse(body);
    console.log(resobj.title);
  } else {
    console.log('error code: ', response.statusCode);
  }
});
