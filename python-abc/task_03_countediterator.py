#!/usr/bin/python3
'''task_03_countediterator.py
Module that add a class countedIterator that iterate iterable with multiple
methods'''


class CountedIterator():
    # Adding a class based on iterable
    def __init__(self, iterator):
        # Initializing the class
        self.iterator = iter(iterator)
        self.iterable = iterator
        self.count = 0

    def __iter__(self):
        # returning the actual iteration
        return self

    def __next__(self):
        # Return the next iteration and update the counter
        if self.count < len(self.iterable):
            new_iter = next(self.iterator)
            self.count += 1
            return new_iter
        else:
            raise StopIteration

    def get_count(self):
        # return the actual counter
        return self.count
