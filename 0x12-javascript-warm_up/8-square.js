#!/usr/bin/node
// Print message

let number = parseInt(process.argv[2], 10);
x = ''
if (isNaN(number)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < number; i++) {
	x += 'X';
    }
    for (let j = 0; j < number; j++) {
	console.log(x)
    }
}
