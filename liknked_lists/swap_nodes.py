
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def swap(head, x, y):
    import pdb; pdb.set_trace()
    if x == y:
        return

    px = py = None
    cx = cy = head

    foundx = foundy = False
    head1 = head
    while (head):
        if not foundx:
            if head.data == x:
                cx = head
                foundx = True
            elif head.next and head.next.data == x:
                px = head
                cx = head.next
                foundx = True

        if not foundy:
            if head.data == y:
                cy = head
                foundy = True
            elif head.next and head.next.data == y:
                py = head
                cy = head.next
                foundy = True

        head = head.next

    if not foundy or not foundx:
        return

    if not px:
        head1 = cy
    else:
        px.next = cy

    if not py:
        head1 = cx
    else:
        py.next = cx

    temp = cx.next
    cx.next = cy.next
    cy.next = temp

    return head1

def print_ll(head):
    while head:
        print (head.data, end = ' ')
        head = head.next

    print()

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = swap(head, 1, 5)
    print_ll(head)


if __name__ == "__main__":
    main()