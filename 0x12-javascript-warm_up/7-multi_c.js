#!/usr/bin/node
const array = process.argv.slice(2);
const ans = Number(array[0]);
let i = 0;
if (isNaN(ans)) {
  console.log('Missing number of occurrences');
}
while (i < ans) {
  console.log('C is fun');
  i++;
}
