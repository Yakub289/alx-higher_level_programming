#!/usr/bin/node

// Write a function that returns the number of occurrences in a list:

// Prototype: exports.nbOccurences = function (list, searchElement).

exports.nbOccurences = function (list, searchElement) {
  let totalIndex = 0;
  for (let i = 0; i < list.length; i++) {
    totalIndex = (list[i] === searchElement ? totalIndex + 1 : totalIndex);
  }
  return (totalIndex);
};
