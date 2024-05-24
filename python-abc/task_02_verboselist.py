class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]  # Get the item to be popped for the message
        print(f"Popped {item} from the list.")
        return super().pop(index)

# Testing the VerboseList class
if __name__ == "__main__":
    vlist = VerboseList()

    # Test append
    vlist.append(1)  # Output: Added 1 to the list.
    vlist.append(2)  # Output: Added 2 to the list.

    # Test extend
    vlist.extend([3, 4, 5])  # Output: Extended the list with 3 items.

    # Test remove
    vlist.remove(3)  # Output: Removed 3 from the list.

    # Test pop
    vlist.pop()  # Output: Popped 5 from the list.
    vlist.pop(0)  # Output: Popped 1 from the list.

    # Display the final state of the list
    print(vlist)  # Output: [2, 4]
