#!/usr/bin/node
exports.esrever = function (list) {
  let myStr = '';
  for (let idx = 0; idx < list.length / 2; idx++) {
    myStr = list[idx];
    list[idx] = list[list.length - idx - 1];
    list[list.length - idx - 1] = myStr;
  }
  return list;
};
