#!/usr/bin/node

const list = require('./100-data.js').list;
const lis_temp = [0];

function multiple_list (list) {
  lis_temp = [0];
  for (let iter = 0; list[iter + 1]; iter++) {
    lis_temp.push(list[iter] * list[iter + 1]);
  }
  return lis_temp;
}

console.log(list);
console.log(multiple_list(list));
