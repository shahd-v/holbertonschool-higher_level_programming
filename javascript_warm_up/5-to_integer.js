#!/usr/bin/node

const value = parseInt(process.argv[2]);
console.log(Number.isNaN(value) ? 'Not a number' : `My number: ${value}`);
