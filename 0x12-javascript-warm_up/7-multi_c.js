#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let value = parseInt(process.argv[2]);
  while (value > 0) {
    console.log('C is fun');
    value--;
  }
}
