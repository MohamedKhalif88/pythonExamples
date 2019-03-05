class Fruits:
    other_fruits = "these are some other important fruits: pawpaw, berries, bananas"

    def __init__(self, fruit1, fruit2):
        self.fruit1 = fruit1
        self.fruit2 = fruit2

    def mango(self):
        print(self.fruit1, " is one of the delicious fruits in the world")

    def orange(self):
        print(self.fruit2, " is the packed with vitamin C")


class Health(Fruits):
    def exercise(self):
        print(f"to have a good health one has to exercise regularly and eat a {self.fruit1} and an {self.fruit2} every morning")

    def sleep(self):
        print("a person should also sleep well for good health")


class Gym(Fruits):
    def __init__(self,fruit1, fruit2,  fruit3, fruit4):
        self.fruit1 = fruit1
        self.fruit2 = fruit2
        self.fruit3 = fruit3
        self.fruit4 = fruit4

    def wyder(self):
        print(f"to increase your bone density take 3 {self.fruit3} and 3 {self.fruit4} "
              f"every morning after exercising")


def main():
    awesomeness = Health("Mango", "Orange")
    awesomeness.orange()
    awesomeness.mango()
    awesomeness.exercise()
    print(awesomeness.other_fruits)
    awesomeness.sleep()
    wyd = Gym("Blue berry", "orange", "Bananas", "Passions")
    wyd.wyder()
    wyd.mango()


if __name__ == "__main__":
    main()
