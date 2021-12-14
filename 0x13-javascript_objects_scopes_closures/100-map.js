#!/usr/bin/node

const list = require('./100-data.js').list;
const lis_temp = list.map((x, index) => x * index);

console.log(list);
console.log(lis_temp);
