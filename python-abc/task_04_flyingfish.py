class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Testing the FlyingFish class
if __name__ == "__main__":
    ff = FlyingFish()

    ff.fly()        # Output: The flying fish is soaring!
    ff.swim()       # Output: The flying fish is swimming!
    ff.habitat()    # Output: The flying fish lives both in water and the sky!

    # Print the method resolution order
    print(FlyingFish.mro())
