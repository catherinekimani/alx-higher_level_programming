#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  const count = Number(process.argv[2]);
  for (let idx = 0; idx < count; idx++) {
    console.log('C is fun');
  }
}
