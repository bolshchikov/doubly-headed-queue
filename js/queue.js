function AppView() {
  this.value = '';
  this.queue = ko.observableArray();

  this.create = function () {};

  this.enqueueHead = function () {
    if (!this.value) {
      alert('Please, enter the value');
      return;
    }
    this.queue.unshift(this.value);
  };
  this.dequeueHead = function () {
    if (!this.value) {
      alert('Please, enter the value');
      return;
    }
    this.queue.shift(this.value);
  };
  this.enqueueTail = function () {
    if (!this.value) {
      alert('Please, enter the value');
      return;
    }
    this.queue.push(this.value);
  };
  this.dequeueTail = function () {
    if (!this.value) {
      alert('Please, enter the value');
      return;
    }
    this.queue.pop(this.value);
  };

  this.concate = function () {};
}

ko.applyBindings(new AppView());