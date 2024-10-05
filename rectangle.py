class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.idx = 0  # To track iteration

    def __iter__(self):
        self.idx = 0  # Setting iteration index when a new iteration starts
        return self

    def __next__(self):
        if self.idx == 0:
            self.idx += 1
            return {'length': self.length}
        elif self.idx == 1:
            self.idx += 1
            return {'width': self.width}
        else:
            raise StopIteration  # No more items to iterate

# Example Test Case:
rect = Rectangle(10, 5)

for dimension in rect:
    print(dimension)
