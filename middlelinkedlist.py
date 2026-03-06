class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next
        
def middle_of_linked_list(head: Node) ->int:
    slow=fast=head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val

def create_linked_list(arr):
    """Helper function to convert a list into a Linked List."""
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def main():
    # Example 1: Odd number of elements
    elements_odd = [1, 2, 3, 4, 5]
    list_odd = create_linked_list(elements_odd)
    print(f"List: {elements_odd} -> Middle: {middle_of_linked_list(list_odd)}")

    # Example 2: Even number of elements
    elements_even = [10, 20, 30, 40, 50, 60]
    list_even = create_linked_list(elements_even)
    print(f"List: {elements_even} -> Middle: {middle_of_linked_list(list_even)}")

if __name__ == "__main__":
    main()