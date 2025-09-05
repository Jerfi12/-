class Node:
    def __init__(self, data):
        self.data = data    # Хранимое значение узла
        self.next = None    # Ссылка на следующий узел (по умолчанию нет)

class LinkedList:
    def __init__(self):
        self.head = None    # Голова списка, изначально пустой (None)

    def append(self, data):
        """Добавить элемент в конец списка"""
        new_node = Node(data)   # Создаём новый узел с данными
        if not self.head:       # Если список пуст
            self.head = new_node
            return
        cur = self.head
        while cur.next:         # Идём до последнего узла
            cur = cur.next
        cur.next = new_node     # Добавляем новый узел в конец

    def prepend(self, data):
        """Добавить элемент в начало списка"""
        new_node = Node(data)
        new_node.next = self.head  # Следующий узел для нового - прежняя голова
        self.head = new_node       # Новый узел становится головой списка

    def delete_with_value(self, data):
        """Удалить первый узел с заданным значением"""
        if not self.head:      # Если список пуст, ничего не делаем
            return
        
        if self.head.data == data:   # Если голова содержит нужное значение
            self.head = self.head.next  # Удаляем голову, сдвигая ссылку
            return
        
        cur = self.head
        # Проходим по списку, пока есть следующий узел
        while cur.next:
            if cur.next.data == data:    # Если следующий узел содержит искомое значение
                cur.next = cur.next.next # Пропускаем этот узел (удаляем)
                return
            cur = cur.next

    def find(self, data):
        """Поиск значения в списке. Возвращает True, если найден."""
        cur = self.head
        while cur:
            if cur.data == data:
                return True   # Элемент найден
            cur = cur.next
        return False  # Элемент не найден

    def print_list(self):
        """Вывод всех элементов списка через '->'"""
        cur = self.head
        elems = []
        while cur:
            elems.append(str(cur.data))  # Преобразуем данные узла в строку
            cur = cur.next
        print(" -> ".join(elems))