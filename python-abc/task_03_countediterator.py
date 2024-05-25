class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count

# Testing the CountedIterator class
if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    counted_iter = CountedIterator(sample_list)

    print("Iterating through the list:")
    for item in counted_iter:
        print(item)

    print(f"Number of items iterated over: {counted_iter.get_count()}")

    # Manual iteration
    counted_iter = CountedIterator(sample_list)
    print("\nManual iteration:")
    while True:
        try:
            item = next(counted_iter)
            print(item)
        except StopIteration:
            break

    print(f"Number of items iterated over: {counted_iter.get_count()}")
