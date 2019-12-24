'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
'''

class MyQueue1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        n = len(self.stack1) - 1
        for i in range(n):
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop()
        for i in range(n):
            self.stack1.append(self.stack2.pop())
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        n = len(self.stack1) - 1
        for i in range(n):
            self.stack2.append(self.stack1.pop())
        res = self.stack1[0]
        for i in range(n):
            self.stack1.append(self.stack2.pop())
        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()






class MyQueue2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
