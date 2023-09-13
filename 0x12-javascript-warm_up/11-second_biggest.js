#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2]) || isNaN(args[3])) {
  console.log('0');
} else {
  const arr = args.map(Number);
  arr.slice(2, args.length);
  arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
