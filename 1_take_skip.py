class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.initial_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        num = self.initial_num
        self.initial_num += self.step
        if self.count == 0:
            raise StopIteration
        self.count -=1
        return num

numbers = take_skip(10, 5)
for number in numbers:
    print(number)




