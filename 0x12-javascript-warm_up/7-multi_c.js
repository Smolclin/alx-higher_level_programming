#!/usr/bin/node

const argM = process.argv[2];
const y = parseInt(argM);

if (isNaN(y)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < y; i++) {
    console.log('C is fun');
  }
}
