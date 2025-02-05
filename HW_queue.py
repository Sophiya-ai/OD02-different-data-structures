# Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out)
from collections import deque
#- **collections.deque**: Использует двустороннюю очередь, которая оптимизирована
# для операций добавления и удаления с обоих концов, что делает её более эффективной для реализации очереди.
# Операции добавления и удаления имеют амортизированную временную сложность O(1).

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    # добавления элемента в конец очереди, те. вначало списка
    def enqueue(self, item):
        self.items.appendleft(item)

    # Удалять будем первый элемент очереди, то есть последний элемент списка
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        print("IndexError: peek from empty stack!")
        return 'Add elements, please'

    # Подсчет количество элементов находится в очереди
    def size(self):
        return len(self.items)


queue = Queue()
print(queue.is_empty())
queue.enqueue('Act1')
queue.enqueue('Act2')
queue.enqueue('Act3')
print(queue.size())
print(queue.dequeue())
print(queue.is_empty())
print(queue.size())

