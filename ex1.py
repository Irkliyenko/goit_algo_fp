class Node:
    # Node class to represent each element of the linked list
    def __init__(self, data=None):
        self.data = data  # Data contained in the node
        self.next = None  # Pointer to the next node


class LinkedList:
    # LinkedList class to handle operations on a linked list
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def insert_at_beginning(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        # Insert a new node after a given node
        if prev_node is None:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        # Delete a node by its data (key)
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
            if cur is None:
                return
            prev.next = cur.next
            cur = None

    def reverse(self):
        # Reverse the linked list in place
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self, h):
        # Sort the linked list using merge sort algorithm
        if h is None or h.next is None:
            return h

        # Find the middle of the list
        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None

        # Recursively sort both halves and merge them
        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        # Helper function to find the middle of the list
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a, b):
        # Helper function to merge two sorted lists
        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def search_element(self, data: int) -> Node | None:
        # Search for an element in the list by its data
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    @staticmethod
    def merge_sorted_lists(list1, list2):
        # Static method to merge two sorted linked lists
        dummy = Node()
        tail = dummy
        while list1 and list2:
            if list1.data < list2.data:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next

    def print_list(self):
        # Print all elements in the list
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Main execution
llist = LinkedList()
l2 = LinkedList()

# Insert nodes into the lists
llist.insert_at_end(30)
llist.insert_at_end(3)
llist.insert_at_end(4)
llist.insert_at_end(20)
llist.insert_at_end(5)
l2.insert_at_end(30)
l2.insert_at_end(44)
l2.insert_at_end(7)

print("Original List:")
llist.print_list()

# Sort the list
llist.head = llist.merge_sort(llist.head)
l2.head = l2.merge_sort(l2.head)

merged_list_head = LinkedList.merge_sorted_lists(llist.head, l2.head)
merged_list = LinkedList()
merged_list.head = merged_list_head
print('\nTwo merged lists')
merged_list.print_list()


print("\nSorted List:")
llist.print_list()
