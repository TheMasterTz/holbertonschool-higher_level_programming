#!/usr/bin/node
const dict = require('./101-data.js').dict;
const NewDict = {};

Object.keys(dict).map(function (key) {
  if (!Array.isArray(NewDict[dict[key]])) {
    NewDict[dict[key]] = [];
  }
  NewDict[dict[key]].push(key);
});

console.log(dict);
console.log(NewDict);
