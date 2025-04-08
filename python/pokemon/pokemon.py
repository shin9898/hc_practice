from abc import ABC, abstractmethod


class NameService(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
    
    @name.setter
    @abstractmethod
    def name(self, new_name):
        pass


class User(NameService):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if "うんこ" in new_name:
            print("不適切な名前です")
            return
        else:
            self._name = new_name
            return self._name


class Pokemon(NameService):
    def __init__(self, name, type1, type2, hp):
        self._name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp


    def attack(self):
        print(f"{self._name}のこうげき!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if "うんこ" in new_name:
            print("不適切な名前です")
            return
        else:
            self._name = new_name
            return self._name

class Pikachu(Pokemon):
    def attack(self):
        super().attack()
        print(f"{super().name}の10万ボルト!")


class Squirtle(Pokemon):
    def attack(self):
        super().attack()
        print(f"{super().name}のみずてっぽう!")

if __name__ == '__main__':
    # poke = Pokemon(name='リザードン', type1='ほのお', type2='ひこう', hp=100) class Pokemonは抽象クラスにしたため削除
    # print(poke.name)
    # print(poke.type1)
    # print(poke.type2)
    # print(poke.hp)
    # poke.attack()

    poke = Pikachu(name='ピカチュウ', type1='でんき', type2='', hp=60)
    print(poke.name)
    poke.attack()
    poke.name = "テキセツ"
    print(poke.name)

    poke = Squirtle(name='ゼニガメ', type1='みず', type2='', hp=70)
    print(poke.name)
    poke.attack()
    poke.name = "うんこ"
    print(poke.name)