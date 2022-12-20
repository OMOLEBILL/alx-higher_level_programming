#!/usr/bin/node
const array = process.argv.slice(2);
const ans = Number(array[0]);
const str = 'X';
let i = 0;
if (isNaN(ans)) {
  console.log('Missing size');
}
while (i < ans) {
  console.log(str.repeat(ans));
  i++;
}
