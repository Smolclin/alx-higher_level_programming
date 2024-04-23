#!/usr/bin/node

const argueLength = process.argv.length;

if (argueLength === 2) {
  console.log('No argument');
} else if (argueLength === 3) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
