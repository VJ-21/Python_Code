# #  trying to create your own version of Python's built-in range() function using the iterator protocol.
class my_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def my_method(self):
        while True:
            if self.start < self.end:
                value = self.start
                yield value
                self.start = self.start + 1


r = my_range(1, 5)

for i in r.my_method():
    print(i)
