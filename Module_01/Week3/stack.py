class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        if self.is_empty():
            raise IndexError('Underflow!')
        return self.__stack.pop()

    def push(self, value):
        if self.is_full():
            raise IndexError('Overflow!')
        self.__stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError('Underflow!')
        return self.__stack[-1]


if __name__ == "__main__":
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())
