class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #클래스내부에 저장되는 변수 , 포인터는 아무것도 가리키지 않음

class LinkedList:
    def __init__(self,data):
        self.head=Node(data) #node를 하나 생성하여 head로 저장

    def append(self,data):
        #연결리스트에 아무 노드도 없을 때
        if self.head is None:
            self.head=Node(data)
            return
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(data)
    def print_all(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next

    def get_node(self,index):
        node=self.head
        count=0
        while count<index:
            node=node.next
            count+=1
        return node

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

        def print_all(self):
            cur = self.head
            while cur is not None:
                print(cur.data)
                cur = cur.next

        def get_node(self, index):
            node = self.head
            count = 0
            while count < index:
                node = node.next
                count += 1
            return node

        def add_node(self, index, value):
            #중간에 원소삽입
            new_node = Node(value)
            if index==0:
            #head 에 넣어야할 상황
                new_node.next=self.head
                self.head=new_node


            node=self.get_node(index-1) #index 번째에 넣기 위해서는 전의 노드인 index-1 노드를 가져와야함
            next_node=node.next # 이전 노드의 다음 노드를 변수에 저장
            node.next=new_node #이전꺼의 링크를 새노드의 앞링크와 연결
            new_node.next= next_node # 새노드를 이전노드의 다음노드와 연결

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

            def print_all(self):
                cur = self.head
                while cur is not None:
                    print(cur.data)
                    cur = cur.next

            def get_node(self, index):
                node = self.head
                count = 0
                while count < index:
                    node = node.next
                    count += 1
                return node

            def add_node(self, index, value):
                new_node = Node(value)
                if index == 0:
                    new_node.next = self.head
                    self.head = new_node
                    return

                node = self.get_node(index - 1)
                next_node = node.next
                node.next = new_node
                new_node.next = next_node

            def delete_node(self, index):
                #처음 노드 삭제
                if index==0:
                    self.head=self.head.next
                    return # 처리 완료햇으므로 return
                node = self.get_node(index-1) # 삭제할 노드으 이전노드 가져옴
                node.next=node.next.next

