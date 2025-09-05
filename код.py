import time

# Класс узла для односвязного списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Класс односвязного списка
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get(self, index):
        current = self.head
        for _ in range(index):
            if not current:
                return None
            current = current.next
        return current.data if current else None

    def get_last(self):
        current = self.head
        if not current:
            return None
        while current.next:
            current = current.next
        return current.data

N = 100000

# Создание массива
array = list(range(N))

# Создание односвязного списка
linked_list = LinkedList()
for i in range(N):
    linked_list.append(i)

# Замеры времени для массива
def time_array_insert_start(arr, val):
    start = time.time()
    arr.insert(0, val)
    end = time.time()
    return end - start

def time_array_insert_end(arr, val):
    start = time.time()
    arr.append(val)
    end = time.time()
    return end - start

def time_array_access_index(arr, index):
    start = time.time()
    val = arr[index]
    end = time.time()
    return end - start, val

def time_array_access_last(arr):
    start = time.time()
    val = arr[-1]
    end = time.time()
    return end - start, val

# Замеры времени для односвязного списка
def time_linkedlist_insert_start(llist, val):
    start = time.time()
    llist.insert_at_start(val)
    end = time.time()
    return end - start

def time_linkedlist_insert_end(llist, val):
    start = time.time()
    llist.append(val)
    end = time.time()
    return end - start

def time_linkedlist_access_index(llist, index):
    start = time.time()
    val = llist.get(index)
    end = time.time()
    return end - start, val

def time_linkedlist_access_last(llist):
    start = time.time()
    val = llist.get_last()
    end = time.time()
    return end - start, val

middle_index = N // 2
test_value = -1

times = {}

times['array_insert_start'] = time_array_insert_start(array, test_value)
times['array_insert_end'] = time_array_insert_end(array, test_value)
times['array_access_middle'], _ = time_array_access_index(array, middle_index)
times['array_access_last'], _ = time_array_access_last(array)

times['linkedlist_insert_start'] = time_linkedlist_insert_start(linked_list, test_value)
times['linkedlist_insert_end'] = time_linkedlist_insert_end(linked_list, test_value)
times['linkedlist_access_middle'], _ = time_linkedlist_access_index(linked_list, middle_index)
times['linkedlist_access_last'], _ = time_linkedlist_access_last(linked_list)

# Вывод результатов
print("Времена выполнения операций (в секундах):")
for op, t in times.items():
    print(f"{op}: {t:.6f}")
