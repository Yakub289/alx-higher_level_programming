#!/usr/bin/node

// Write a script that concats 2 files.

// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination

const fs = require('fs');
const a = fs.readFileSync(process.argv[2], 'utf-8');
const b = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], a + b);
