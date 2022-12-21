#!/usr/bin/node
const array = process.argv.slice(2);
array.sort(function (a, b) {
  return a - b;
});
const n = Number(array[array.length - 2]);
if (isNaN(n)) {
  console.log(0);
} else {
  console.log(n);
}
