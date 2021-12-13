#!/usr/bin/node
let args_length = process.argv.length;

if (args_length === 2) {
  console.log('No argument');
} else if (args_length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
