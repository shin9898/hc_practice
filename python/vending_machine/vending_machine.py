from juice import Juice
class VendingMachine:
    def __init__(self, machine_name):
        self.machine_name = machine_name
        self.stock = []

        # 初期在庫5本を追加
        for _ in range(5):
            self.stock.append(Juice('ペプシ', 150))
            self.stock.append(Juice('モンスター', 230))
            self.stock.append(Juice('いろはす', 120))

        self._sales = 0

# 在庫補充
    def add_stock(self, juice, quantity):
        for _ in range(quantity):
            self.stock.append(Juice(juice.name, juice.price))

# 在庫確認
    def get_stock_count(self, juice_name):
        return len([j for j in self.stock if j.name == juice_name])

    @property
    def sales(self):
        return self._sales

# 購入条件確認
    def can_purchase(self, juice, card):
        return self.get_stock_count(juice.name) > 0 and card.deposit >= juice.price

# ジュース購入
    def purchase(self, juice, card):
        if not self.can_purchase(juice, card):
              raise Exception("購入できません")
        for i, j in enumerate(self.stock):
            if j.name == juice.name:
                del self.stock[i]
                break
        card.pay(juice.price)
        self._sales += juice.price