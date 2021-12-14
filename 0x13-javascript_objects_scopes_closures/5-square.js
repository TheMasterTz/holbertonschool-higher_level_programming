#!/usr/bin/node

module.exports = class Rectangle {
  constructor (size) {
    if (size > 0) {
      this.width = size;
      this.height = size;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
