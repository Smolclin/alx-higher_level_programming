#!/usr/bin/node

const addMeMaybe = (num, thisFunction) => {
	num++;
	thisFunction(num);
};
module.exports.addMeMaybe = addMeMaybe;
