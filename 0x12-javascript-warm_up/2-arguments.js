#!/usr/bin/node

const argueLength = process.argv.length;

if (argueLength === 2) {
  console.log("No argument");
} else if (argueLength === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
