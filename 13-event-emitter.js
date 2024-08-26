const EventEmitter = require('events');

const customEmitter = new EventEmitter();

// Hint: Event handler needs to be defined for a event
// before the event is emitted: on before emit

customEmitter.on('response', (name, id) => {
  console.log(`data received: \nName: ${name}\nID:   ${id}`);
});

customEmitter.on('response', () => {
  console.log('some other application logic');
});

customEmitter.emit('response', 'Matt', 125);
