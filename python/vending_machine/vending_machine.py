
# 必要なクラスを考えていく

# class CashlessCard
class CashlessCard:
# 必要な変数：カード名, デポジット(default==500)
    def __init__(self, card_name,deposit):
        self.card_name = card_name
        self.deposit = deposit
# 必要な関数：チャージする(100円未満は例外処理), 残高確認, 支払う

# Suicaインスタンスの生成
suica = CashlessCard('Suica', 500)
print(suica.card_name)
print(suica.deposit)

# class Juice
class Juice:
# 必要な変数：ジュース名, 値段
    def __init__(self,juice_name, price):
        self.juice_name = juice_name
        self.price = price
# 必要な関数：思いつかず
# ペプシインスタンスの生成
pepsi = Juice('ペプシ', 150)
print(pepsi.juice_name)
print(pepsi.price)

# class VendingMachine
class VendingMachine:
# 必要な変数：自販機名,格納されているジュースの種類, 在庫数, 売上金額
    def __init__(self, vending_machine_name, juice_type_stored, stock_quantity, sales_amount):
          self.vending_machine_name = vending_machine_name
          self.juice_type_stored = juice_type_stored
          self.stock_quantity = stock_quantity
          self.sales_amount = sales_amount
# 必要な関数：ジュースの補充, ジュースの購入, 在庫数の表示, 総売上金額の表示
# １種類のジュースが格納できる自販機インスタンスの生成
vending_machine1 = VendingMachine('machine1', 1, 5, 0)
print(vending_machine1.vending_machine_name)
print(vending_machine1.juice_type_stored)
print(vending_machine1.stock_quantity)
print(vending_machine1.sales_amount)