function generateNumber() {
  return Math.floor(Math.random()*101);
}

function AppView() {

  this.queues = ko.observableArray();

  this.create = function () {
    this.queues.push({array: ko.observableArray(), attemps: 0});
    this.queues()[this.queues().length - 1].array.push('Hi, I\'m your new queue');
  };

  this.enqueueHead = function () {
    if (this.queues()[this.queues().length - 1].attemps === 0) {
      this.queues()[this.queues().length - 1].array.pop();
    };
    this.queues()[this.queues().length - 1].array.unshift(generateNumber());
    this.queues()[this.queues().length - 1].attemps += 1;
  };
  this.dequeueHead = function () {
    if (this.queues()[this.queues().length - 1].attemps === 0) {
      alert('Please, append a member before dequeueing');
      return;
    };
    this.queues()[this.queues().length - 1].array.shift();
  };
  this.enqueueTail = function () {
     if (this.queues()[this.queues().length - 1].attemps === 0) {
      this.queues()[this.queues().length - 1].array.pop();
    };
    this.queues()[this.queues().length - 1].array.push(generateNumber());
    this.queues()[this.queues().length - 1].attemps += 1;
  };
  this.dequeueTail = function () {
    if (this.queues()[this.queues().length - 1].attemps === 0) {
      alert('Please, append a member before dequeueing');
      return;
    };
    this.queues()[this.queues().length - 1].array.pop();
  };

  this.concat = function () {

  };
}

ko.applyBindings(new AppView());