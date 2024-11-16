class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.start = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start > 0:
            self.start -= 1
            return self.start
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
