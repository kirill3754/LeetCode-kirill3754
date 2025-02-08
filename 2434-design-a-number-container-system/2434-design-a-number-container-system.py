class NumberContainers:

    def __init__(self):
        self.index_number = {}
        self.where_numbers = {}
        

    def change(self, index: int, number: int) -> None:
        if index not in self.index_number:
            self.index_number[index] = number
            if number not in self.where_numbers:
                self.where_numbers[number] = SortedSet()
            self.where_numbers[number].add(index)
        else:
            old_number = self.index_number[index]
            self.where_numbers[old_number].remove(index)
            if not self.where_numbers[old_number]:
                del self.where_numbers[old_number]
            self.index_number[index] = number
            if number not in self.where_numbers:
                self.where_numbers[number] = SortedSet()
            self.where_numbers[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.where_numbers:
            return -1
        return self.where_numbers[number][0]


        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)