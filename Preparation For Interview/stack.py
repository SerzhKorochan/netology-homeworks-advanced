class Stack:
    def __init__(self):
        self.stack_elements = []

    def is_empty(self) -> bool:
        if len(self.stack_elements):
            return True
        return False

    def push(self, element) -> None:
        self.stack_elements.append(element)

    def pop(self):
        return self.stack_elements.pop()

    def peek(self):
        return self.stack_elements[-1]

    def size(self) -> int:
        return len(self.stack_elements)


def is_brackets_balanced(subsequence: str) -> bool:
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = Stack()

    for bracket in subsequence:
        if bracket in '([{':
            stack.push(bracket)
        elif stack.size() and bracket == pairs[stack.peek()]:
            stack.pop()
        else:
            return False

    return stack.size() == 0


brackets = '{{}}'
res = is_brackets_balanced(brackets)

if res:
    print('Balanced!')
else:
    print('Unbalanced!')
