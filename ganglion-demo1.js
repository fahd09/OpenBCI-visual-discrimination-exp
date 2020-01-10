const Ganglion = require("@openbci/ganglion");
const ganglion = new Ganglion();
ganglion.once("ganglionFound", peripheral => {
  // Stop searching for BLE devices once a ganglion is found.
  ganglion.searchStop();
  ganglion.on("sample", sample => {
    /** Work with sample */
    console.log(sample.sampleNumber);
    //for (let i = 0; i < ganglion.numberOfChannels(); i++) {
      // console.log(
      //   "Channel " +
      //     (i + 1) +
      //     ": " +
      //     sample.channelData[i].toFixed(8) +
      //     " Volts."
      // );
    //}
    var d = new Date()
    st = sample.channelData.join(' ');
    //var s = ''+ sample.timeStamp + ': '+ st
    var s = ''+ d.getTime() + ': '+ st
    console.log(s)
    //lsloutlet.send(s)    
  });
  ganglion.once("ready", () => {
    ganglion.streamStart();
  });
  ganglion.connect(peripheral);
});
// Start scanning for BLE devices
ganglion.searchStart();


// const Ganglion = require('@openbci/ganglion');
// let ganglion = new Ganglion({
//   nobleAutoStart: true,
//   sendCounts: true,
//   verbose: true
// }, (error) => {
//   if (error) {
//     console.log(error);
//   } else {
//     if (verbose) {
//       console.log('Ganglion initialize completed');
//     }
//   }
// });

// ganglion.once('ganglionFound', (peripheral) => {
//   ganglion.searchStop();
//   ganglion.on('sample', (sample) => {
    
//     console.log('Sending Sample...');
//     // sendToPython({
//     //   action: 'process',
//     //   command: 'sample',
//     //   message: sample
//     // });
//   });
//   ganglion.once('ready', () => {
//     console.log('Starting Streaming...');
//     ganglion.streamStart();
//   });
//   ganglion.connect(peripheral);
// });

// // ganglion.searchStart();
// function exitHandler (options, err) {
//   if (options.cleanup) {
//     if (verbose) console.log('clean');
//     ganglion.manualDisconnect = true;
//     ganglion.disconnect();
//     ganglion.removeAllListeners('droppedPacket');
//     ganglion.removeAllListeners('accelerometer');
//     ganglion.removeAllListeners('sample');
//     ganglion.removeAllListeners('message');
//     ganglion.removeAllListeners('impedance');
//     ganglion.removeAllListeners('close');
//     ganglion.removeAllListeners('error');
//     ganglion.removeAllListeners('ganglionFound');
//     ganglion.removeAllListeners('ready');
//     ganglion.destroyNoble();
//   }
//   if (err) console.log(err.stack);
//   if (options.exit) {
//     if (verbose) console.log('exit');
//     if (ganglion.isSearching()) {
//       ganglion.searchStop().catch(console.log);
//     }
//     ganglion.manualDisconnect = true;
//     ganglion.disconnect(true).catch(console.log);
//     process.exit(0);
//   }
// }

// // do something when app is closing
// process.on('exit', exitHandler.bind(null, {
//   cleanup: true
// }));

// // catches ctrl+c event
// process.on('SIGINT', exitHandler.bind(null, {
//   exit: true
// }));

// // catches uncaught exceptions
// process.on('uncaughtException', exitHandler.bind(null, {
//   exit: true
// }));
