
class GymEquipment:
    name = ""
    price = 0
    stock = 1

    def __init__(self, name, price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    

barbell = GymEquipment("barbell", 20,2)

squatrack = GymEquipment("squat_rack", 4,4)

bench = GymEquipment("bench", 16,6)


def get_shop_stock():

    shop_stock = {
        barbell.name : barbell,
     squatrack.name: squatrack,
     bench.name: bench
    }
    return shop_stock
