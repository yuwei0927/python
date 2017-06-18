class Fruit(object):#类
    price = 0 #类的变量
    def __init__(self, name, color, *args, **kwargs):
        self.name = name
        self.color = color
        super(Fruit,self).__init__(*args, **kwargs)

    def grow(self): #类的方法
        print(self.color+" "+self.name +" fruit growing...")

    @staticmethod
    def getPrice():
        Fruit.price += 8
        print(Fruit.price)

class Apple(Fruit):#类的继承
    def __init__(self, kind):
        self.kind = kind
        super(Apple,self).__init__(name='apple', color='red')

    def grow(self):
        print('Apple growing')
    

if __name__ == "__main__":
    apple = Fruit(name='apple', color='red')#实例化
    apple.grow()
    apple.price = 9
    print(apple.price)
    print(apple.name)
    print(apple.color)

    banana = Fruit(name='banana', color='yellow')
    banana.grow()
    banana.price=10
    print(banana.price)
    banana.getPrice()

    print(Fruit.price)
    #print(Fruit.name) #这句话有误，不可以
    print(Fruit.getPrice())

    print(dir(Fruit))
    redApple = Apple('hong fu shi')
    redApple.grow()
    print(redApple.price)
    print(redApple.name)
    print(redApple.color)
    print(redApple.kind)




