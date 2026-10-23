class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency
    
     # Delete this line and implement the Patient class



class MinHeap:
    def __init__(self, data=None):
        self.data = data if data is not None else []

    def _get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def _get_left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def _get_right_child_index(self, index: int) -> int:
        return 2 * index + 2


    def heapify_up(self, index: int) -> None:
        parent_index = self._get_parent_index(index)
        if index > 0 and self.data[index].urgency < self.data[parent_index].urgency:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index: int) -> None:
        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)
        smallest = index

        if left_child_index < len(self.data) and self.data[left_child_index].urgency < self.data[smallest].urgency:
            smallest = left_child_index

        if right_child_index < len(self.data) and self.data[right_child_index].urgency < self.data[smallest].urgency:
            smallest = right_child_index

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)


    def insert(self, patient: Patient) -> None:
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)


    
    def peek(self) -> Patient | None:
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self) -> Patient | None:
        if not self.data:
            return None
        

        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()

        self.heapify_down(0)

        return min_patient


    def print_heap(self) -> None:
            print("Current Queue:")
            for patient in self.data:
                print(f"Patient Name: {patient.name}, Urgency: {patient.urgency}")
    

    
     # Delete this line and implement the MinHeap class




# Test your MinHeap class here including edge cases
'''p1 = Patient("Alice", 5)

print(p1.name)  
print(p1.urgency)  
'''
heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.print_heap()

next_up = heap.peek()
print(next_up.name, next_up.urgency) 

served = heap.remove_min()
print(served.name) # Taylor
heap.print_heap()

'''
For this type of problem, using a tree data structure is the most efficient way to represent the parent-child relationships among doctors. This way, it shows a clear hierarchy and isolates different branches for the required purposes.
The choice of method depends on the operation the user is trying to perform. For example, the pre-order transverse method is used to show a hierarchical view of parent-child relationships. The inorder traversal is used for a Binary Search Tree (BST) to extract data when needed. Furthermore, the inorder traversal is in non-decreasing order, meaning its structure goes as follows “left-root-right”. Lastly, the post-order traversal is used to remove nodes or to calculate aggregated subtree values. This method is used because the user needs to validate all child nodes before finalizing the parent node.
The heap helps simulate real-time systems like emergency intake because it serves as the foundation for Priority Queues. The MinHeap class sorts patients by urgency level, with 1 being critical and 5 non-urgent; this way, it ensures that doctors always attend to the one in most need of assistance. The MinHeap has a structure for inserting new patients as they arrive and for deleting them as soon as they are admitted. Even though patients arrive dynamically at arbitrary times, the heap rearranges the queue dynamically based on priority, not like the system of FIFO.


'''