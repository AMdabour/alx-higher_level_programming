#!/usr/bin/node
const dict = require('./101-data').dict;
const totalDictList = Object.entries(dict);
const dictValueList = Object.values(dict);
const dictUniqValueList = [...new Set(dictValueList)];

const newDict = {};
for (const i in dictUniqValueList) {
  const list = [];
  for (const j in totalDictList) {
    if (totalDictList[j][1] === dictUniqValueList[i]) {
      list.push(totalDictList[j][0]);
    }
  }
  newDict[dictUniqValueList[i]] = list;
}

console.log(newDict);
