class budget:

    def __init__(self,m2):
        self.money = m2
        self.deposited_money = m2




    def deposit(self, m1):
        self.money = self.money + m1
        self.deposited_money = self.deposited_money + m1

    def show_balance(self):
        print('balance:', self.money)

    def withdraw(self,m1):
        self.money = self.money - m1

    def balance(self):
        return self.money
    def total_deposited_money(self):
        return self.deposited_money



food = budget(1000)

sports = budget(1500)

food.deposit(1000)

sports.deposit(1500)

food.withdraw(500)

sports.show_balance()
food.show_balance()
m = food.deposited_money + sports.deposited_money
print('total balance remaining is:', food.balance() + sports.balance())
print('total budget deposited for this year is: ', m )
print('percentage of budget for food is: ', food.deposited_money/m *100, '%')
print(food.deposited_money)
