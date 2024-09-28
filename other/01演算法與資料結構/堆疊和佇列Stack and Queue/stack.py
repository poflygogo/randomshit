from collections.abc import Iterable


class Stack:
    def __init__(self, initial_data):
        self.stack = []
        self.initial_data = initial_data

        # 判斷是否是initial_data是否是可迭代的資料
        if isinstance(initial_data, Iterable):
            self.stack = list(initial_data)

        else:
            raise NotImplementedError('Initial_data was not iterable data')

    #給python Interpreter看的
    def __repr__(self):
        return "Stack(initial_data={!r})".format(self.initial_data)
    
    #給使用者看的print()
    def __str__(self):
        return "stack({})".format(self.stack)

    #return: int
    def __len__(self):
        return len(self.stack)

    def __getitem__(self, i):
        return self.stack[i]

    @property
    def is_empty(self):
        return len(self.stack) == 0

    
    def push(self, data):
        self.stack.append(data)

    #return: data that pop out
    def pop(self):
        if not self.is_empty:
            return self.stack.pop()

    # return: top element in stack
    def peek(self):
        return self.stack[-1]
    

def main():
    list1 = []
    stack = Stack(list1) 
    print(stack) # stack([])

    stack.push(1)
    print(stack) # stack([1])

    stack.pop()
    print(stack) # stack([])

    stack.push(3)
    print(stack) # stack([3])

    stack.push(4)
    print(stack) # stack([3, 4])

    print(stack.peek()) # 4


if __name__ == '__main__':
    main()


"""
【Python】Stack(堆疊) 資料結構實作 | 愛喝咖啡 X 咖啡程式
https://lovedrinkcafe.com/python-stack-data-structure/
"""