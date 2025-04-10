class CashlessCard:
    def __init__(self, card_name, deposit=500):
        self.card_name = card_name
        self._deposit = deposit

# チャージする
    def charge(self, charge_amount):
          if int(charge_amount) < 100:
              raise ValueError("100円未満はチャージできません")
          self._deposit += charge_amount
          return self._deposit
        
# 支払い
    def pay(self, price):
        if self._deposit < price:
            raise ValueError("残高不足です")
        self._deposit -= price
        return self._deposit

# 残高を取得
    @property
    def deposit(self):
        return self._deposit