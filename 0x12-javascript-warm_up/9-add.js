#!/usr/bin/node
const arr = process.argv.slice(2);
function add (a, b) {
  return (Number(a) + Number(b));
}
console.log(add(arr[0], arr[1]));
