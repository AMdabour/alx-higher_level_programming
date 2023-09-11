#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const myArray = process.argv.slice(2).map(Number);
  const secBigNum = myArray.sort((a, b) => { return b - a; })[1];
  console.log(secBigNum);
}
