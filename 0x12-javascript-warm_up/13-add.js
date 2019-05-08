#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return ('NaN');
  } else {
    return (Number(a) + Number(b));
  }
}

exports.add = add;
