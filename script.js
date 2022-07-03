#! /usr/bin/env node

const fs = require("fs");
const argv = require("yargs").argv._;

// This is the information we pass through in the driver config via
// the placeholders `%A %O %B %P`
// %A = tmp filepath to our version of the conflicted file
// %O = tmp filepath to the base version of the file
// %B = tmp filepath to the other branches version of the file
// %P = placeholder / real file name
// %L = conflict marker size (to be able to still serve according to this setting)

console.log('argv',argv);
const ours = argv[0];
const base = argv[1];
const theirs = argv[2];
const filename = argv[3];

console.log('ours',ours);
console.log('base',base);
console.log('theirs',theirs);
console.log('filename',filename);

const baseJson = fs.readFileSync(base);
const oursJson = fs.readyFileSync(ours);
const theirsJson = fs.readyFileSync(theirs);

console.log('baseJson',baseJson);
console.log('oursJson',oursJson);
console.log('theirsJson',theirsJson);

// We can do whatever we want, in this example we just take the new entries from
// our branch and put the new entries from the other branch on top of them
const mergedJson = {
  entries: [
    ...baseJson.entries,
    ...oursJson.entries.slice(baseJson.entries.length),
    ...theirsJson.entries.slice(baseJson.entries.length)
  ]
};

// To resolve the conflict simply write to the current branch file
fs.writeFileSync(ours, JSON.stringify(mergedJson, null, 2));