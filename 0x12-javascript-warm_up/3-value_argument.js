#!/usr/bin/node
const ARGS_LENGTH = process.argv[2];

if (ARGS_LENGTH === undefined) {
  console.log('No argument');
} else {
  console.log(ARGS_LENGTH);
}
