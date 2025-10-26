from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.data = balance
        self.size = len(self.data)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not 0 < account1 <= self.size or not 0 < account2 <= self.size:
            return False
        if self.data[account1 - 1] < money:
            return False
        self.data[account1 - 1] -= money
        self.data[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not 0 < account <= self.size:
            return False
        self.data[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not 0 < account <= self.size:
            return False
        if self.data[account - 1] < money:
            return False
        self.data[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
