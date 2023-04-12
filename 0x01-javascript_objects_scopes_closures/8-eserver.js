#!/usr/bin/node
exports.esrever = function (list) {
    var i =0; j= list.length-1;
    while(i < j) {
      var temp = list[i];
      list[i] = list[j];
      list[j] = temp;
      i++;
      j--;
    }
    return list;
  }
