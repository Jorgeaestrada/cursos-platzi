import time

""" 
Versión con Iterator de la 
sucesion de fibonacci
"""


class FibonacciIterator():

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.counter = 0

        return self

    def __next__(self):
        if self.max == None or self.counter <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.a

            self.c = self.a + self.b
            self.a, self.b = self.b, self.c
            self.counter += 1
            return self.a
        else:
            raise StopIteration


if __name__ == '__main__':

    fibonacci = FibonacciIterator(10)

    for element in fibonacci:
        print("fibonacci:   {}".format(element))
        time.sleep(0.5)