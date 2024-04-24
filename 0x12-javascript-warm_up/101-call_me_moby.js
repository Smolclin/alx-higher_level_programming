#!/usr/bin/node

const callMeMoby = (x, thisFunction) => {
  if (x > 0) {
    thisFunction();
    callMeMoby(x - 1, thisFunction);
  }
};

module.exports.callMeMoby = callMeMoby;
