#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocuure = 0;
  for (let idx = 0; idx < list.length; idx++) {
    if (searchElement === list[idx]) {
      ocuure++;
    }
  }
  return ocuure;
};
