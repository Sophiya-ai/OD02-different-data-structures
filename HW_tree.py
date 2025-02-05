# П редставления узла в дереве
# ** Параметр `value` ** - задает значение узла
# Атрибуты:
# **`value`** - сохраняет значение параметра `value`
# **`children`** - инициализируется пустым списком. Этот список будет содержать дочерние узлы текущего узла
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    # Метод add_child добавляет дочерний узел в список `children` текущего узла.
    # `child_node` — это объект `TreeNode`, который будет добавлен в список
    def add_child(self, child_node):
        self.children.append(child_node)

    # Метод __str__ возвращает строковое представление дерева с учетом уровней вложенности.
    # Метод рекурсивно вызывает `str` для каждого дочернего узла, увеличивая уровень вложенности на 1.
    # - `level` указывает уровень текущего узла в дереве (корневой узел имеет уровень 0)
    # `"  " * level` добавляет отступы для каждого уровня вложенности, чтобы визуализировать иерархию
    # - `repr(self.value)` используется для получения строкового представления значения узла.
    def __str__(self, level=0):
        ret = "  " * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    # Метод возвращает строковое представление объекта `TreeNode`, которое включает его значение
    def __repr__(self):
        return f'TreeNode({self.value})'

# Пример использования дерева
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode(4))
child1.add_child(TreeNode(66))
child2.add_child(TreeNode(5))
child2.add_child(TreeNode(44))

print(root)