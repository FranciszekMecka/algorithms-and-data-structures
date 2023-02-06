#  randomly generated array for the driver code
arr = [ 23, 27, 79, 80, 58, 87, 9, 53, 12, 82, 45, 69, 66, 82, 8, 67, 21, 25, 3, 18, 42, 42, 11, 61, 61, 70, 40, 49, 37, 82, 83, 22, 87, 18, 65, 48, 33, 54, 25, 71, 14, 3, 80, 57, 50, 48, 1, 21, 38, 86, 63, 37, 43, 78, 62, 67, 40, 88, 35, 1, 96, 24, 73, 64, 86, 21, 83, 83, 57, 41, 16, 81, 38, 88, 65, 44, 60, 63, 7, 47, 53, 58, 98, 56, 78]

#  implementation of max heap
#  to change it to a min heap, it just takes takes to change '>' opetrators
class Heap:
    arr = [23, 27, 79, 80, 58, 87, 9, 53, 12, 82, 45, 69, 8, 67, 21, 25, 3, 18, 42, 42]

    def heapify(self, index: int):
        left = self.left_child(index)
        right = self.right_child(index)

        if (left <= len(self.arr)
            and self.arr[left - 1] > self.arr[index - 1]):
            max_index = left
            
        else:
            max_index = index

        if (right <= len(self.arr)
            and self.arr[right - 1] > self.arr[max_index - 1]):
            max_index = right

        if max_index != index:
            self.arr[max_index - 1], self.arr[index - 1] = self.arr[index - 1], self.arr[max_index - 1]
            self.heapify(max_index)

    def build_heap(self):
        for x in range(len(self.arr)//2, 0, -1):
            self.heapify(x)

    def insert_fix(self, index: int):
        parent = self.parent(index)

        if (self.arr[parent - 1] < self.arr[index - 1]):
            self.arr[parent - 1], self.arr[index - 1] = self.arr[index - 1], self.arr[parent - 1]
            self.insert_fix(parent)
        
    def insert(self, value: int):
        self.arr.append(value)
        self.insert_fix(len(self.arr))
        #  fixing the heap property

    def delete(self, index: int):
        if self.arr != []:
            self.arr[index - 1], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[index - 1]
            self.arr = self.arr[:-1]
            self.heapify(index)

    def parent(self, value: int):
        # indexes start from 1
        if value // 2 == 0: return 1
        return value // 2

    def left_child(self, value:int):
        return value * 2

    def right_child(self, value:int):
        return value * 2 + 1

    def check_heap(self):
        for x in range(1, len(self.arr)):
            parent = self.arr[self.parent(x) - 1]
            node = self.arr[x - 1]
            if parent < node:
                return False
        return True

#  driver code
heap = Heap()
print(heap.arr)
print(heap.check_heap())
heap.build_heap()
print(heap.arr)
print(heap.check_heap())
for x in range(5):
    heap.delete(1)
print(heap.arr)
print(heap.check_heap())
for x in arr:
    heap.insert(x)
print(heap.arr)
print(heap.check_heap())
for x in range(75):
    heap.delete(1)
print(heap.arr)
print(heap.check_heap())
