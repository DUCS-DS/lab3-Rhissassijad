from llist import LList, Node, append


def llprint(lst, num):
    """Print the first num terms of a linked list."""
    node = lst.head
    count = 0
    while node and count < num:
        print(node.val, end=" ")
        node = node.next
        count += 1
    print()


def find_cycle(lst):
    """Return the start index and length of the cycle."""
    slow = fast = lst.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            
            slow = lst.head
            while slow != fast:
                slow = slow.next
                fast = fast.next
        
            cycle_start = slow

            
            length = 1
            fast = fast.next
            while fast != cycle_start:
                fast = fast.next
                length += 1

            return cycle_start.val, length
    return None, 0


if __name__ == "__main__":
    
    lst = LList()
    values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    cycle_start_index = 10
    cycle_length = 5

    for i, val in enumerate(values):
        node = Node(val)
        append(lst, node)
        if i == cycle_start_index:
            cycle_start_node = node

    node = lst.head
    while node.next:
        node = node.next
    node.next = cycle_start_node

    # Challenge 2: 
    print("Cyclic linked list:")
    llprint(lst, num=20)

    # Challenge 1: 
    start_index, cycle_length = find_cycle(lst)
    if start_index is not None:
        print("Cycle starts at index", start_index, "and has length", cycle_length)
    else:
        print("No cycle found.")
