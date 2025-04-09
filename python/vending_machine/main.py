from cashless_card import CashlessCard
from juice import Juice
from vending_machine import VendingMachine


if __name__ == '__main__':
    suica = CashlessCard("Suica")
    vm = VendingMachine("VM")

    juice_definitions = {
        1: ("ペプシ", 150),
        2: ("モンスター", 230),
        3: ("いろはす", 120)
    }

    juice_menu = {key: Juice(name, price) for key, (name, price) in juice_definitions.items()}

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
            for juice in juice_menu.values():
                print(f"在庫: {juice.name},{vm.get_stock_count(juice.name)}本")
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