#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const argM = parseInt(process.argv[2]);
const argN = parseInt(process.argv[3]);

const result = add(argM, argN);
console.log(result);
