#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (process.argv.length < 3 || isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
