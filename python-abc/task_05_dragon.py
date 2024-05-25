class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Testing the Dragon class
if __name__ == "__main__":
    draco = Dragon()

    draco.swim()  # Output: The creature swims!
    draco.fly()   # Output: The creature flies!
    draco.roar()  # Output: The dragon roars!
