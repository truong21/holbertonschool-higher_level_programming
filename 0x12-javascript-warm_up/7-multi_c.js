#!/usr/bin/node

let word = 'C is fun';
let num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
let i = 0;
while (i < num) {
  console.log(word);
  i++;
}
