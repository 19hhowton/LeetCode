class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        # because head equals the first node (data and next=None),
        # when you write new_node=.next = self.head, new_node (data and next=None) becomes new_node
        # (data and next=first_node) and next literally
        # points to that first node because it's assigned to that first node.
        new_node.next = self.head
        # head is now assigned/pointed to new_node and not the first node instance
        self.head = new_node

    def two_node_llist_switcher(self):
        # how do you get the first and second Nodes? prev and curr.
        prev = self.head.next
        curr = self.head
        # you would loop here but looking at only two node switch

        # curr.next point to None
        prev.next = curr
        curr.next = None
        self.head = prev

    def iterator(self):
        curr = self.head
        while curr != None:
            print(curr)
            curr = curr.next

    def insert_linked_list(self, prev_val, insert_node_val):
        prev = self.head
        counter = 0

        while prev != None:
            if prev.val == prev_val:
                if counter = 0:  # its a head
                    push(insert_node_val)
                # two can point to the same node.
                #
                #
                #
                #
                else:
            new_node.next = prev.next
            prev.next = new_node
            return 'Done'
        else:
            prev = prev.next


llist = LinkedList()
llist.push(2)
llist.push(1)
llist.push(7)

llist.insert_linked_list(1, 5)