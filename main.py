class Goods(object):
    def __init__(self, name, price, stock):
        self.id = 0
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return 'id:%s\n' \
               'Имя:% s \ n' \
               'Цена:% s \ n' \
               'Инвентарь:% s \ n' % (self.id, self.name, self.price, self.stock)


if __name__ == '__main__':
    goods = Goods('One', 2999, 100)
    print(goods)
    goods2 = Goods('Two', 3666, 100)
    print(goods2)

