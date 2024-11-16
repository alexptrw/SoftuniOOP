class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.steps_made = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.steps_made < self.count:
            value = self.steps_made * self.step
            self.steps_made += 1
            return value
        raise StopIteration

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
