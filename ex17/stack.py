#!/usr/bin/python
import array

class stack(object):
    def __init__(self):
        # self.stack always starts with one index to support subscript instead
        # of appending.
        self.stack = array.array('i')
        self.new = True

    def push(self, item):
        # if the stack is new, change the new flag, and insert the first item
        # into stack[0]
        if self.new:
            self.new = False
            self.stack.append(item)
            pass
        # if the stack is not new
        else:
            # initialize a new array that is n+1 the length of self.stack
            self.longer_stack = array.array('i')
            # insert 'item' into longer_stack[0]
            self.longer_stack.append(item)
            # insert self.stack[i+1] into longer_stack[i]
            for i in xrange(len(self.stack)):
                self.longer_stack.append(self.stack[i])
            del self.stack
            self.stack = self.longer_stack
            pass

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            item = self.stack[0]
            self.shorter_stack = array.array('i')
            for i in xrange(len(self.stack)-1):
                self.shorter_stack = self.stack[i+1]
            del self.stack
            self.stack = self.shorter_stack
            return item

mystack = stack()

mystack.push(1)
mystack.push(2)
print mystack.pop()
print mystack.pop()
