#!/usr/bin/node

let num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
}
let i = 0; let j = 0;
while (i < num) {
  j = 0;
  let string = '';
  while (j < num) {
    string += 'X';
    j++;
  }
  console.log(string);
  i++;
}
