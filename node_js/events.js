let events = require('events');

let notifySpecialDay = (data) => {
    console.log('Happy ' + data + '!');
}

let myEmitter = new events.EventEmitter();
myEmitter.on('specialDay', notifySpecialDay);
myEmitter.emit('specialDay', 'World Wombat Day');