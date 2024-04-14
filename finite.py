from llist import LList, Node, append


def length(lst):
    """Return the length of a finite linked list."""
    count = 0
    node = lst.head
    while node:
        count += 1
        node = node.next
    return count


def llprint(lst):
    """Print a finite linked list."""
    node = lst.head
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    
    lst = LList()
    values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    for val in values:
        append(lst, Node(val))

    # Exercise 2: 
    print("Length of the linked list:", length(lst))

    # Exercise 3: 
    print("Linked list:")
    llprint(lst)

    # Exercise 4:
    print("\nTesting length and llprint functions:")
    print("Length of the linked list:", length(lst))
    print("Linked list:")
    llprint(lst)
