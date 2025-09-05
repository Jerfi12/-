# Two Sum (в лоб и улучшенный варианты)

def two_sum_bruteforce(nums, target):
    # В лоб: проверка всех пар
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def two_sum_optimized(nums, target):
    # Используем словарь для хранения элементов и их индексов
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


# Remove Duplicates from Sorted Array

def remove_duplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index


# Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # сохранение следующего узла
        current.next = prev       # переворот текущей ссылки
        prev = current            # сдвиг prev вперед 
        current = next_node       # переход к следующему узлу
    return prev
