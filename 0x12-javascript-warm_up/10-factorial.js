#!/usr/bin/node
const res = Number(process.argv[2]);
function fac (a) {
  if (a === 0) {
    return (1);
  } else {
    return a * fac(a - 1);
  }
}
if (isNaN(res)) {
  console.log(1);
} else {
  console.log(fac(res));
}
