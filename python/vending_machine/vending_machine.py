
# 必要なクラスを考えていく
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

# class Juice
class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# class VendingMachine
class VendingMachine:
    def __init__(self, machine_name):
        self.machine_name = machine_name
        self.stock = {'ペプシ': 5, 'モンスター': 5, 'いろはす': 5}
        self._sales = 0
# 必要な関数：在庫数の表示, 総売上金額の表示
    def add_stock(self, juice, quantity):
        if juice.name not in self.stock:
            self.stock[juice.name] = 0
        self.stock[juice.name] += quantity

    def get_stock_count(self, juice_name):
        return self.stock.get(juice_name)

    @property
    def sales(self):
        return self._sales
    
    @sales.setter
    def sales(self, sales):
        if sales < 0:
            False
        else:
            self._sales = sales
    
    def can_purchase(self, juice, card):
        return self.stock.get(juice.name, 0) > 0 and card.deposit >= juice.price
    
    def purchase(self, juice, card):
        if not self.can_purchase(juice, card):
              raise Exception("購入できません")
        card.pay(juice.price)
        self.stock[juice.name] -= 1
        self._sales += juice.price


# プログラム実行の流れ
if __name__ == '__main__':
    suica = CashlessCard("Suica")
    pepsi = Juice("ペプシ", 150)
    monster = Juice("モンスター", 230)
    irohas = Juice("いろはす", 120)
    vm = VendingMachine("VM")

    juice_menu = {
        1: pepsi,
        2: monster,
        3: irohas
    }

    while True:
        menu_number = int(input(
        """
        メニュー番号を選んでください。
        1. キャッシュレスカードにチャージ
        2. ジュース購入
        3. 自販機のジュース在庫・売上金額確認
        4. ジュースの補充
        5. 終了
        :
        """))
        if menu_number == 1:
            try:
                print("【キャッシュレスカードにチャージ】")
                charge_amount = int(input("チャージ金額を入力してください(100円以上) : "))
                suica.charge(charge_amount)
                print(f"{charge_amount}円チャージしました。現在の残高: {suica.deposit}円")
            except ValueError as e:
                print(e)

        elif menu_number == 2:
            print("【購入できるジュース一覧】")
            for key, juice in juice_menu.items():
                print(f"{key}.{juice.name} ({juice.price}円)")
            juice_choice = int(input("購入したいジュースの番号を選んでください : "))
            selected_juice = juice_menu.get(juice_choice)

            try:
                if not selected_juice:
                    raise Exception("無効な選択です")
                if not vm.can_purchase(selected_juice, suica):
                    raise Exception("購入条件を満たしていません")
                vm.purchase(selected_juice, suica)
                print(f"{selected_juice.name}を購入しました。現在の残高: {suica.deposit}円")
            except Exception as e:
                print(e)

        elif menu_number == 3:
            print("【自販機のジュース在庫一覧・売上金額表示】")
            for juice in [pepsi, monster, irohas]:
                print(f"在庫: {juice.name}{vm.get_stock_count(juice.name)}本")
            print(f"自販機総売上 : {vm.sales}円")

        elif menu_number == 4:
            print("【ジュース在庫状況一覧】")
            for key, juice in juice_menu.items():
                print(f"{key}.{juice.name} : {vm.get_stock_count(juice.name)}本")
            juice_choice = int(input("補充したいジュースの番号を選択してください : "))
            selected_juice = juice_menu.get(juice_choice)
            quantity = int(input("補充したい本数を入力してください : "))

            try:
                if not selected_juice and quantity:
                    raise Exception("無効な選択値です")
                vm.add_stock(selected_juice, quantity)
                print(f"{selected_juice.name}を{quantity}本補充しました。合計:{vm.get_stock_count(selected_juice.name)}本")
            except Exception as e:
                print(e)

        elif menu_number == 5:
            print("終了します")
            break
        
        else:
            print("無効なメニュー番号です")
