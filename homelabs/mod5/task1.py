class Node:
    """
    Вспомогательный класс для узлов списка (элементов стека).
    Хранит сами данные и ссылку на предыдущий элемент.
    """
    def __init__(self, data):
        self.data = data       # Полезная нагрузка (число, строка и т.д.)
        self.pref = None       # Ссылка на предыдущий узел (внизу стека)

class Stack:
    """
    Основной класс для стека (LIFO - Last In, First Out).
    """
    def __init__(self):
        self.end = None  # Ссылка на вершину стека (последний добавленный элемент)

    def pop(self):
        """
        Возвращение последнего элемента из списка с удалением его из списка.
        """
        # Если стек пуст, возвращаем None (или можно вызвать ошибку)
        if self.end is None:
            return None
        
        # Сохраняем значение вершины во временную переменную
        val = self.end.data
        
        # Перемещаем указатель вершины на предыдущий элемент
        self.end = self.end.pref
        
        # Возвращаем сохраненное значение
        return val

    def push(self, val):
        """
        Добавление элемента val в конец списка (на вершину стека).
        """
        # Создаем новый узел
        new_node = Node(val)
        
        # Новый узел должен ссылаться на текущую вершину как на предыдущий элемент
        new_node.pref = self.end
        
        # Обновляем вершину стека - теперь это новый узел
        self.end = new_node

    def print(self):
        """
        Вывод на печать содержимого стека (от вершины к низу).
        """
        current_node = self.end
        
        # Проходим по цепочке ссылок pref, пока не дойдем до None
        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.pref
        
        # Перевод строки для красоты вывода
        print()

# --- Блок тестирования (выполнится при запуске файла) ---
if __name__ == "__main__":
    print("--- Тест Стека ---")
    my_stack = Stack()
    
    # Добавляем элементы
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    
    print("Стек после добавления 1, 2, 3:")
    my_stack.print()  # Ожидаем: 3 2 1
    
    # Удаляем элемент
    deleted = my_stack.pop()
    print(f"Удалили элемент: {deleted}")  # Ожидаем: 3
    
    print("Стек после удаления:")
    my_stack.print()  # Ожидаем: 2 1