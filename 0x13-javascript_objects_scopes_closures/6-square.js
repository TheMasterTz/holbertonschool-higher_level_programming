#!/usr/bin/node
const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (char = 'X') {
    super.print(char);
  }
};
