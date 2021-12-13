class Stack:
    def __init__(self, stack_elements: list):
        self.stack_elements = stack_elements

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
