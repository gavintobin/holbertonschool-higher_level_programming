#!/usr/bin/node
const [arg1, arg2] = process.argv.slice(2);
console.log(`${arg1} is ${arg2}`);
if (!arg2);
console.log(`${arg1} is undefinded`);
if (!arg1 || !arg2);
console.log('undefinded is undefined');
