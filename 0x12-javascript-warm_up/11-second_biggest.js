#!/usr/bin/node
const LISTS_NUMBER = process.argv.slice(2);

if (process.argv.length <= 3) {
  console.log(0);
} else {
  LISTS_NUMBER.sort();
  console.log(LISTS_NUMBER[LISTS_NUMBER.length - 2]);
}
