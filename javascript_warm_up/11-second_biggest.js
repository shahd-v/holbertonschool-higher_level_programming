#!/usr/bin/node

const values = process.argv.slice(2).map(Number);
if (values.length < 2) console.log(0);
else {
  values.sort((a, b) => b - a);
  console.log(values[1]);
}
