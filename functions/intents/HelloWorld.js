const lib = require('lib');

/**
* Basic "Hello World" intent, can receive a `name` parameter
* @param {string} name Your name
* @returns {string}
*/
module.exports = (name, callback) => {

  return callback(null, `Making tea for ${name}`);

};
