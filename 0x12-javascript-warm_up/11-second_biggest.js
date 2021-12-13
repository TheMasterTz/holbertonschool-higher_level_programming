#!/usr/bin/node
const LISTS_NUMBER = process.argv.slice(2);
let second_max = 0;

if (LISTS_NUMBER.length > 1) {
  LISTS_NUMBER.sort();
  second_max = LISTS_NUMBER[LISTS_NUMBER.length - 2];
}

console.log(second_max);
