// code by Alexandre Barachant

//const Ganglion = require('openbci-ganglion').Ganglion;
const Ganglion = require("@openbci/ganglion");
const ganglion = new Ganglion();
// Construct LSL Handoff Python Shell
var PythonShell = require('python-shell');
var lsloutlet = new PythonShell('LSLHandoff.py');

lsloutlet.on('message', function(message){
    console.log('LslOutlet: ' + message);
});
console.log('Python Shell Created for LSLHandoff');

ganglion.once('ganglionFound', (peripheral) => {
  console.log('Ganglion Found');
  // Stop searching for BLE devices once a ganglion is found.
  ganglion.searchStop();
  ganglion.on('sample', (sample) => {
    /** Work with sample */
    //console.log(sample)
    st = sample.channelData.join(' ');
    var s = ''+ sample.timestamp+Math.abs((sample.sampleNumber%2)-1) + ': '+ st
    //console.log(s)
    lsloutlet.send(s)
  });
  ganglion.once('ready', () => {
    console.log('Streaming now...');
    ganglion.streamStart();
  });
  ganglion.connect(peripheral);
});
// Start scanning for BLE devices
ganglion.searchStart();
