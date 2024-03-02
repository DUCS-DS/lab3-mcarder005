from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count = 1
    if lst.head:
        node = lst.head
        while node.next:
            count +=1
            node = node.next
    else:
        return 0
    return count

def llprint(lst):
    """print a finite linked list"""
    
    if lst.head:
        node = lst.head
        while node.next:
            print(node.val,end = " ")
        print(node.val)
    else:
        print(0)

if __name__ == "__main__":

    from genfinite import lst
    print(length(lst))
    #
