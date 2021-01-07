"""Singly Linked List using python"""


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)  # If LL is empty create & add Node at beginning
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(data, None)  # If LL is not empty create & add Node at end

    def create(self, dataset):

        self.head = None
        for data in dataset:
            self.insert_at_end(data)

    def print(self):
        if self.head is None:
            print("Link List is empty!!!")
            return
        llstr = ''
        temp = self.head
        while temp:
            llstr += str(temp.data) + "-->"
            temp = temp.next
        llstr += "NULL"  # creating string of LL data eg."Node1-->Node2-->Node3"
        print(llstr)

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
            count += 1
            temp = temp.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_start(data)
            return

        temp = self.head
        count = 0
        while temp:
            if count == index - 1:
                node = Node(data, temp.next)
                temp.next = node
                break
            count += 1
            temp = temp.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print("Present")
                return True
            temp = temp.next
        print("Absent")
        return False

    def remove_using_key(self, key):
        if self.search(key):
            if self.head.data == key:
                self.head = self.head.next
                return

            temp = self.head
            prev = temp
            while temp:
                if temp.data == key:
                    print(prev.data)
                    prev.next = temp.next
                    return
                prev = temp
                temp = temp.next


if __name__ == '__main__':
    ll = LinkList()
    ll.insert_at_start(10)
    ll.insert_at_start(5)
    ll.insert_at_start(0)
    ll.print()
    print(ll.length())
    ll.insert_at_end(15)
    ll.print()
    print(ll.length())
    ll.remove_at(0)
    ll.print()
    print(ll.length())
    lis = [100, 90, 80, 70, 60, 50]
    ll.create(lis)
    ll.print()
    print(ll.length())
    ll.insert_at(1, 95)
    ll.print()
    print(ll.length())
    ll.search(91)
    ll.remove_using_key(80)
    ll.print()
    print(ll.length())
