# 1, 5, 6, 5, 1

class Node():
    def __init__(self, v):
        self.value = v
        self.next = None


def output(n):
    curr = n
    s = ""
    while curr is not None:
        s += f"{curr.value}->"
        curr = curr.next
    print(s)


def remove_dupes(head):
    check = head
    a = head
    b = head.next

    while check is not None:
        while a is not None and b is not None:
            if b.value == check.value:
                a.next = b.next
                b = a.next if a is not None else None
            else:
                a = b
                b = a.next if a is not None else None
        a = check.next
        b = a.next if a is not None else None
        check = a


def main():
    head = None
    curr = None

    for i in [1, 5, 6, 5, 1]:
        if head is None:
            head = Node(i)
            curr = head
        else:
            n = Node(i)
            curr.next = n
            curr = n

    output(head)
    remove_dupes(head)
    output(head)
