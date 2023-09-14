#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let idx1 = 0; idx1 < this.width; idx1++) {
      let row = '';
      for (let idx2 = 0; idx2 < this.height; idx2++) {
        row += c;
      }
      console.log(row);
    }
  }
};
