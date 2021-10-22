class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    sum1=get_sum(linked_list_1)
    sum2 = get_sum(linked_list_2)
    return sum1+sum2

def get_sum(linked_list):
    total= 0
    head= linked_list.head
    while head is not None:
        total = total * 10 + head.data
        head = head.next

    return total

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))