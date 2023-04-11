#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

function secondLargest(arr) {
  if (arr.length < 2) {
    return 0;
  }
  let largest = arr[0];
  let secondLargest = -Infinity;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
      secondLargest = largest;
      largest = arr[i];
    } else if (arr[i] > secondLargest && arr[i] < largest) {
      secondLargest = arr[i];
    }
  }
  return secondLargest;
}

console.log(secondLargest(args));
