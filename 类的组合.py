#类的组合，就是把类的实例化放到一个新类里面
class Turtle:
    def __init__(self, x):
        self.num =x

class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def num(self):
        print("水池里一共有乌龟 %d 只， 鱼 %d 条" % (self.turtle.num, self.fish.num))

pool = Pool(1, 10)
pool.num()
