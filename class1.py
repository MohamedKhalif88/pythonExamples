class Awesome:
    chicken = 'they slaughtered two fat chicken for him'
    
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def the_first(self):
        print(self.name, f" this is the {self.num}st method of your code")

    def the_second(self):
        print(self.name, f" this is the {self.num}nd method of your code")


def main():
    cool = Awesome('Mak', 1)
    cool2 = Awesome('khalif', 2)
    cool.the_first()
    cool2.the_second()
    print(cool.chicken)
    print(cool2.chicken)


if __name__ == '__main__':
    main()