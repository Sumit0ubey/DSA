class Node:
    def __init__(self, data:str):
        self.data = data
        self.next = None

def PrintlinkedList(List:Node):
    while List:
        print(List.data, sep="->", end=" ")
        List = List.next
    print()

def MergeSortedLinkedLists(List1:Node, List2:Node):
    if List1 == None: return List2
    if List2 == None: return List1

    if List1.data <= List2.data:
        List1.next = MergeSortedLinkedLists(List1.next, List2)
        return List1
    else:
        List2.next = MergeSortedLinkedLists(List1, List2.next)
        return List2

linkedlistgrop1_1 = Node(5)
linkedlistgrop1_2 = Node(8)
linkedlistgrop1_3 = Node(9)
linkedlistgrop1_4 = Node(10)
linkedlistgrop1_1.next = linkedlistgrop1_2
linkedlistgrop1_2.next = linkedlistgrop1_3
linkedlistgrop1_3.next = linkedlistgrop1_4

linkedlistgrop2_1 = Node(24)
linkedlistgrop2_2 = Node(69)
linkedlistgrop2_3 = Node(85)
linkedlistgrop2_4 = Node(98)
linkedlistgrop2_1.next = linkedlistgrop2_2
linkedlistgrop2_2.next = linkedlistgrop2_3
linkedlistgrop2_3.next = linkedlistgrop2_4

print("Group 1st Linked-list: ", end=" ")
PrintlinkedList(linkedlistgrop1_1)
print("Group 2nd Linked-list: ", end=" ")
PrintlinkedList(linkedlistgrop2_1)

print("Merged Linked-List: ", end=" ")
PrintlinkedList(MergeSortedLinkedLists(linkedlistgrop1_1, linkedlistgrop2_1))
