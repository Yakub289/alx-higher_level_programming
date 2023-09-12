#!/usr/bin/node

const size = process.argv[2];

if (process.argv.length < 3 || isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let symbol = '';
    for (let j = 0; j < size; j++) symbol += 'X';
    console.log(symbol);
  }
}
