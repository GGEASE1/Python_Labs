class Node:
    """
    Вспомогательный класс для узлов двусвязного списка.
    """
    def __init__(self, data):
        self.data = data       # Храним информацию
        self.nref = None       # Ссылка на следующий узел (ближе к концу очереди)
        self.pref = None       # Ссылка на предыдущий узел (ближе к началу очереди)

class Queue:
    """
    Основной класс Очереди (FIFO - First In, First Out).
    """
    def __init__(self):
        self.start = None # Ссылка на начало очереди (откуда забираем)
        self.end = None   # Ссылка на конец очереди (куда добавляем)

    def pop(self):
        """
        Возвращаем элемент val из начала списка с удалением из списка.
        """
        # Если очередь пуста
        if self.start is None:
            return None
            
        # Запоминаем данные первого элемента
        val = self.start.data
        
        # Сдвигаем указатель начала на следующий элемент
        self.start = self.start.nref
        
        if self.start is not None:
            # Если очередь не опустела, у нового начала не должно быть ссылки назад
            self.start.pref = None
        else:
            # Если удалили последний элемент, то конец тоже должен стать None
            self.end = None
            
        return val

    def push(self, val):
        """
        Добавление элемента val в конец списка.
        """
        new_node = Node(val)
        
        # Если очередь была пуста
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            # Привязываем новый узел к текущему концу
            new_node.pref = self.end
            self.end.nref = new_node
            # Обновляем указатель конца
            self.end = new_node

    def insert(self, n, val):
        """
        Вставить элемент val между элементами с номерами n-1 и n.
        (То есть вставка на позицию n, считая с 0 от начала).
        """
        # Создаем новый узел
        new_node = Node(val)
        
        # Если вставка в самое начало (индекс 0)
        if n == 0:
            if self.start is None: # Если очередь пуста
                self.push(val)
                return
            
            # Вставляем перед start
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
            return

        # Ищем элемент, который сейчас стоит на позиции n
        current_node = self.start
        index = 0
        while current_node is not None and index < n:
            current_node = current_node.nref
            index += 1
        
        # Если дошли до конца списка (индекс n равен длине), вставляем в конец
        if current_node is None:
            self.push(val)
            return
        
        # Вставка "между" узлами (перед current_node)
        prev_node = current_node.pref
        
        # Связываем новый узел с соседями
        new_node.nref = current_node
        new_node.pref = prev_node
        
        # Обновляем ссылки у соседей
        if prev_node is not None:
            prev_node.nref = new_node
        current_node.pref = new_node

    def print(self):
        """
        Вывод на печать содержимого очереди (от начала к концу).
        """
        current_node = self.start
        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.nref
        print()

# --- Блок тестирования (выполнится при запуске файла) ---
if __name__ == "__main__":
    print("--- Тест Очереди ---")
    my_queue = Queue()
    
    # Добавляем элементы
    my_queue.push(10)
    my_queue.push(20)
    my_queue.push(30)
    
    print("Очередь после push 10, 20, 30:")
    my_queue.print() # Ожидаем: 10 20 30
    
    # Вставляем 99 на позицию 1 (между 10 и 20)
    my_queue.insert(1, 99)
    print("После insert(1, 99):")
    my_queue.print() # Ожидаем: 10 99 20 30
    
    # Удаляем из начала
    val = my_queue.pop()
    print(f"Извлекли pop(): {val}") # Ожидаем: 10
    
    print("Очередь после pop:")
    my_queue.print() # Ожидаем: 99 20 30