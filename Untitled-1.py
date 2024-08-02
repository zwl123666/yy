import random

class MerchantGame:
    def __init__(self):
        self.starting_capital = 1000
        self.current_capital = self.starting_capital
        self.item_prices = {
            "apple": 0,
            "banana": 3,
            "orange": 7
        }
        self.inventory = {}

    def buy_item(self, item):
        if item not in self.item_prices:
            print("无效的商品")
            return
        price = self.item_prices[item]
        if self.current_capital < price:
            print("资金不足，无法购买")
            return
        self.current_capital -= price
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1
        print(f"成功购买 {item}，花费 {price} 元，剩余资金 {self.current_capital} 元")

    def sell_item(self, item):
        if item not in self.inventory or self.inventory[item] == 0:
            print("没有该商品可出售")
            return
        price = self.item_prices[item]
        self.current_capital += price
        self.inventory[item] -= 1
        print(f"成功出售 {item}，获得 {price} 元，当前资金 {self.current_capital} 元")

    def check_inventory(self):
        print("当前库存：")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

    def random_price_change(self):
        for item, price in self.item_prices.items():
            change = random.randint(-5, 5)
            new_price = max(1, price + change)
            self.item_prices[item] = new_price
            print(f"{item} 的价格变为 {new_price} 元")

    def play(self):
        while True:
            print("1. 购买商品")
            print("2. 出售商品")
            print("3. 查看库存")
            print("4. 查看商品价格")
            print("5. 随机价格变动")
            print("6. 退出游戏")
            choice = int(input("请选择操作："))
            if choice == 1:
                item = input("请输入要购买的商品：")
                self.buy_item(item)
            elif choice == 2:
                item = input("请输入要出售的商品：")
                self.sell_item(item)
            elif choice == 3:
                self.check_inventory()
            elif choice == 4:
                print("当前商品价格：")
                for item, price in self.item_prices.items():
                    print(f"{item}: {price} 元")
            elif choice == 5:
                self.random_price_change()
            elif choice == 6:
                print("游戏结束，最终资金：", self.current_capital)
                break
            else:
                print("无效的选择，请重新输入")

if __name__ == "__main__":
    game = MerchantGame()
    game.play()
    