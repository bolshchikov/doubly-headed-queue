function generateNumber() {
  return Math.floor(Math.random()*101);
}

function AppView() {

  this.queues = ko.observableArray();

  this.create = function () {
    if (this.queues().length !== 0 && this.queues()[this.queues().length - 1].attemps === 0) {
      alert('I would recommend you to add members to the previous queue first');
      return;
    }
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
    var qToBeAppended, qToAppend, i = 0, len;
    qToAppend = this.queues()[this.queues().length - 2].array;
    qToBeAppended = this.queues()[this.queues().length - 1].array;
    len = qToBeAppended().length;
    for (i; i < len; i+=1) {
      var member = qToBeAppended.shift();
      qToAppend.push(member);
    }
    this.queues.pop();
  };
}

ko.applyBindings(new AppView());