'''Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.'''

from collections import deque

class MyQueue:
    # Easy solution - not amortized
    def __init__(self):
        # Initialize with two stacks
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x):
        # Always push to stack 1
        self.stack1.append(x)
    
    def pop(self):
        # Pop each item from stack 1 and place on stack 2
        while not self.empty():
            current = self.stack1.popleft()
            self.stack2.append(current)
        # The top of stack 2 is now our first in
        # Pop this and then push all items back to stack 1
        pop = self.stack2.popleft()
        while len(self.stack2) > 0:
            current = self.stack2.popleft()
            self.push(current)
        return pop
    
    def peek(self):
        # Same as push but without removing the first in
        while not self.empty():
            current = self.stack1.popleft()
            self.stack2.append(current)
        peek = self.stack2[0]
        while len(self.stack2) > 0:
            current = self.stack2.popleft()
            self.push(current)
        return peek 

    def empty(self):
        return len(self.stack1) < 1

class MyAmortQueue:   
    # Amortized O(1) time complexity
    def __init__(self):
        # Use dynamic lists for both stacks
        self.capacity1 = 1
        self.length1 = 0
        self.stack1 = [None] * self.capacity1
        self.capacity2 = 1
        self.length2 = 0
        self.stack2 = [None] * self.capacity2

    def push(self, x):
        # Double capacity if list filled
        if self.length1 == self.capacity1:
            new_capacity = 2 * self.capacity1
            new_stack1 = [None] * new_capacity
            for i in range(self.length1):
                new_stack1[i] = self.stack1[i]
            self.stack1 = new_stack1
            self.capacity1 = new_capacity
        # Assign x to item at index of current length
        self.stack1[self.length1] = x
        # Increment length
        self.length1 += 1
    
    def pop(self):
        # Iterate the list starting the last assigned element and working backwards
        end = self.length1 - 1
        for i in range(end, -1, -1):
            # Get the value at index and reassign to None
            x = self.stack1[i]
            self.stack1[i] = None
            self.length1 -= 1
            # Push this value to stack 2, same as in push method above
            if self.length2 == self.capacity2:
                new_capacity = 2 * self.capacity2
                new_stack2 = [None] * new_capacity
                for i in range(self.length2):
                    new_stack2[i] = self.stack2[i]
                self.stack2 = new_stack2
                self.capacity2 = new_capacity
            self.stack2[self.length2] = x
            self.length2 += 1
        # Pop the last value at the index of stack2 length - 1 and reassign to None
        pop = self.stack2[self.length2 - 1]
        self.stack2[self.length2 - 1] = None
        self.length2 -= 1
        end = self.length2 - 1
        # Pop and push back to stack1
        for i in range(end, -1, -1):
            x = self.stack2[i]
            self.stack2[i] = None
            self.length2 -= 1
            if self.length1 == self.capacity1:
                new_capacity = 2 * self.capacity1
                new_stack1 = [None] * new_capacity
                for i in range(self.length1):
                    new_stack1[i] = self.stack1[i]
                self.stack1 = new_stack1
                self.capacity1 = new_capacity
            self.stack1[self.length1] = x
            self.length1 += 1
        return pop
    
    # Same as pop but with peek instead of pop
    def peek(self):
        end = self.length1 - 1
        for i in range(end, -1, -1):
            x = self.stack1[i]
            self.stack1[i] = None
            self.length1 -= 1
            if self.length2 == self.capacity2:
                new_capacity = 2 * self.capacity2
                new_stack2 = [None] * new_capacity
                for i in range(self.length2):
                    new_stack2[i] = self.stack2[i]
                self.stack2 = new_stack2
                self.capacity2 = new_capacity
            self.stack2[self.length2] = x
            self.length2 += 1
        # Only difference between pop() and peek()
        peek = self.stack2[self.length2 - 1]
        end = self.length2 - 1
        for i in range(end, -1, -1):
            x = self.stack2[i]
            self.stack2[i] = None
            self.length2 -= 1
            if self.length1 == self.capacity1:
                new_capacity = 2 * self.capacity1
                new_stack1 = [None] * new_capacity
                for i in range(self.length1):
                    new_stack1[i] = self.stack1[i]
                self.stack1 = new_stack1
                self.capacity1 = new_capacity
            self.stack1[self.length1] = x
            self.length1 += 1
        return peek

    def empty(self):
        return self.length1 < 1

# TESTS

queue = MyQueue()

# print(queue.empty())

for n in [1,2,3,4]:
    queue.push(n)

print(queue.peek())
# >>1
print(queue.pop())
# >>1
queue.push(5)

while not queue.empty():
    print(queue.pop())
# >>2,3,4,5
print(queue.empty())