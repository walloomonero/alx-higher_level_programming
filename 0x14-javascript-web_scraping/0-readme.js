#!/usr/bin/node
// The script that reads and prints the content of a file.

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf-8',
  function (error, data) {
    if (error) {
      console.log(error);
      return;
    }
    console.log(data);
  });
