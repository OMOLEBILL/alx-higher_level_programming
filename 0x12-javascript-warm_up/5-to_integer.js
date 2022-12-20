#!/usr/bin/node
const array = process.argv.slice(2);
let ans = Number(array[0]);
if (isNaN(ans)) {
  ans = 'Not a number';
} else {
  ans = ('My number: ' + ans);
}
console.log(ans);
