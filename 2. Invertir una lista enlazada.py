class LinkedList:
    # Se asume que se han definido las clases Node y LinkedList, como en el ejercicio anterior

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, param):
        pass


# Uso
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.reverse()
# Ahora la lista está invertida
