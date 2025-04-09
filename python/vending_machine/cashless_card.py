# class CashlessCard
class CashlessCard:
    def __init__(self, card_name, deposit=500):
        self.card_name = card_name
        self._deposit = deposit
# 必要な関数：チャージする(100円未満は例外処理), 残高確認, 支払う
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

# 残高を取得 getterとsetterを後程定義
    # def get_deposit(self):
    #     return self._deposit
    @property
    def deposit(self):
        return self._deposit
    
    @deposit.setter
    def deposit(self, deposit):
        if deposit < 0:
            False
        else:
            self._deposit = deposit