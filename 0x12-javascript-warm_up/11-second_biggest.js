#!/usr/bin/node
const LISTS_NUMBER = process.argv.slice(2);

if (LISTS_NUMBER.length > 1) {
  LISTS_NUMBER.sort();
  console.log(LISTS_NUMBER[LISTS_NUMBER.length - 2]);
} else {
  console.log(0);
}
