#!/usr/bin/node
// Print message

const number = parseInt(process.argv[2], 10);
let x = '';

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    x += 'X';
  }
  for (let j = 0; j < number; j++) {
    console.log(x);
  }
}
