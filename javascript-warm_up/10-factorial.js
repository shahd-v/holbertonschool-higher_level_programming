#!/usr/bin/node

const number = parseInt(process.argv[2]);
function factorial (n) {
  return n <= 1 ? 1 : n * factorial(n - 1);
}

console.log(factorial(Number.isNaN(number) ? 1 : number));
