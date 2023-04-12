#!/usr/bin/node
exports.esrever = function (list) {
    var i =0; j= list.length-1;
    const reversedList = [];

    for (let i = list.length - 1; i >= 0; i--) {
      reversedList.push(list[i]);
    }
  
    return reversedList;
  };
