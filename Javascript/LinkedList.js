var head;

class Node {
  constructor(d) {
    this.data = d;
    this.next = null;
  }
}

// add node to begin of linked list
function push(newData) {
  var newNode = new Node(newData);
  newNode.next = head;
  head = newNode;
}
// insert node at given pos
function insert(newData, pos = 0) {
  if (pos === 0) {
    push(newData);
  } else {
    var newNode = new Node(newData);
    var node = head;
    var index = 1;

    while (index <= pos && node != null) {
      if (pos == index) {
        newNode.next = node.next;
        node.next = newNode;
        break;
      } else {
        node = node.next;
        index++;
      }
    }
  }
}
// add node to end of linked list
function append(newData) {
  var newNode = new Node(newData);
  var last = head;
  while (last.next != null) {
    last = last.next;
  }
  last.next = newNode;
  newNode.next = null;
}

function removeKey(key) {
  if (head.data == key) {
    head = head.next;
  } else {
    var prev = head;
    var node = head.next;
    while (node != null) {
      if (node.data == key) {
        prev.next = node.next;
      }
      prev = node;
      node = node.next;
    }
  }
}

function printList() {
  node = head;
  while (node != null) {
    console.log(node.data);
    node = node.next;
  }
}

var head = new Node(1);
var second = new Node(2);
var third = new Node(3);
head.next = second;
second.next = third;
push(10);
append(20);
insert(5);
insert(4, 1);
insert(21, 7);
removeKey(5);
removeKey(1);
removeKey(21);
printList();
