# Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # добавления элемента в конец очереди, те. вначало списка
    def enqueue(self, item):
        self.items.insert(0, item)

    # Удалять будем первый элемент очереди, то есть последний элемент списка
    def dequeue(self):
        return self.items.pop()

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

