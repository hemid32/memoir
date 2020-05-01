var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
var s1 = new Gpio(4, 'out');
var s2 = new Gpio(4, 'out');
var s3 = new Gpio(4, 'out');
var s4 = new Gpio(4, 'out');
var s5 = new Gpio(4, 'out');
function setting(val) { //function to start blinking
  //if (s1.readSync() === 0) { //check the pin state, if the state is 0 (or off)
  //  LED.writeSync(1); //set pin state to 1 (turn LED on)
  //} else {
  //  LED.writeSync(0); //set pin state to 0 (turn LED off)
  alert(val);

  }
