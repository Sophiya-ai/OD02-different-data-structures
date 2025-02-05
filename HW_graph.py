class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        # Добавляем рёбра для неориентированного графа
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

        if node2 in self.graph:
            self.graph[node2].append(node1)
        else:
            self.graph[node2] = [node1]

    def get_neighbors(self, node):
        return self.graph.get(node, [])


    # Такие методы с двойными подчеркиваниями называются "магическими методами"
    # Они позволяют интегрировать пользовательские классы в поведение языка Python, предоставляя возможность
    # использовать стандартные функции и операторы с пользовательскими объектами

    # **Специальное назначение**: Двойные подчеркивания с обеих сторон указывают на то,
    # что метод имеет специальное назначение и взаимодействует с внутренними механизмами Python.
    # Такие методы автоматически вызываются в определённых контекстах. Например, `__str__` вызывается,
    # когда вы используете функцию `str()` или `print()` для объекта

    # **Интеграция с языком**: Благодаря магическим методам, пользовательские классы могут интегрироваться с языком
    # на более глубоком уровне. Например, методы `__add__`, `__len__`, `__getitem__` и другие позволяют
    # перегружать операторы и функции для классов.
    def __str__(self):
        return '\n'.join(f'{node}: {neighbors}' for node, neighbors in self.graph.items())


graph = Graph()
graph.add_node(1)
graph.add_node(2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
print(graph)
