#!/usr/bin/node
// Print message

if (typeof process.argv[2] === 'undefined' || process.argv.length === 3) {
  console.log('0');
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i], 10));
  }
  arr.sort(function (a, b) { return a - b; });
  console.log(arr[arr.length - 2]);
}
