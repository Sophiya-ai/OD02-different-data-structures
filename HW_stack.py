# Стек (Stack) — это структура данных, работающая по принципу "последний пришел, первый ушел" (Last In, First Out, LIFO)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # добавление элемента в стек
    def push(self, item):
        self.items.append(item)

    # удаление верхнего последнего вошедшего элемента
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    # получение верхнего элемента без удаления
    def peek(self):
        if not self.is_empty():
            return f"Верхний элемент стека - {self.items[-1]}"
        else:
            print("IndexError: peek from empty stack!")
            return 'Add elements, please'


stack = Stack()
print(stack.peek())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.is_empty())
print(stack.peek())
stack.pop()
print(stack.peek())

