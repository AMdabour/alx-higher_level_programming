#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const value = Number(process.argv[2]);
  let i = 0;
  while (i < value) {
    console.log('X'.repeat(value));
    i++;
  }
}
