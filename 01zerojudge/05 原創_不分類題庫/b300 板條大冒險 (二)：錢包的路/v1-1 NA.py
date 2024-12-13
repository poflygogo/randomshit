# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b300. 板條大冒險 (二)：錢包的路


class Solution:
    # date_start: tuple[int] 開始日期
    # total_money: int 資產總額
    # cities_data: dict 當前城市資料， 城市:收入
    # cities_order: tuple 紀錄城市的順序，用於最終輸出
    # x, y: int 城市的變化量
    # trend: dict 紀錄每個月有哪些城市發生變化，tuple[int]日期:list[tuple[str]]城市的變化
    # date_end: tuple[int] 結束日期
    def __init__(self):
        self.date_start, self.total_money = input().split()
        self.date_start = tuple(map(int, self.date_start.split('/')))
        self.total_money = int(self.total_money)
        self.cities_data, self.cities_order = self.get_cities_init_data()
        self.x, self.y = map(int, input().split())
        self.trend = self.get_trend_data()
        self.date_end = tuple(map(int, input().split('/')))

    def mainloop(self):
        # 第一個月已經結算完，但還是要記錄狀態變化
        self.city_change(self.date_start)
        for i in range(1, self.date_end[0] * 12 + self.date_end[1] - self.date_start[0] * 12 - self.date_start[1] + 1):
            # 1. 進行財產結算
            self.total_money += sum(self.cities_data.values())

            # 2. 紀錄城市狀態變化
            date_curr = self.date_pass_n_mon(self.date_start, i)
            self.city_change(date_curr)
        
        # 3. 帳冊總結
        print(
            f'{self.date_end[0]}/{str(self.date_end[1]).rjust(2, "0")} {self.total_money}',
            '\n'.join(f'{i} {self.cities_data[i]}' for i in sorted(self.cities_data, key=lambda x: (self.cities_data[x], self.cities_order))),
            sep='\n'
        )

    @staticmethod
    def get_cities_init_data():
        """接收城市的基本資料"""
        result_dict = {}
        result_order = []
        while True:
            temp = input()
            if temp == '----':
                break
            temp = temp.split()
            result_order.append(temp[0])
            result_dict[temp[0]] = int(temp[1])
        return result_dict, tuple(result_order)

    @staticmethod
    def get_trend_data():
        """接收城市變化紀錄的資料"""
        result_dict = {}
        while True:
            temp = input()
            if temp == '----':
                break
            date, city, change = temp.split()
            date = tuple(map(int, date.split('/')))
            result_dict[date] = result_dict.get(date, []) + [(city, change)]
        return result_dict
    
    @staticmethod
    def date_pass_n_mon(date: tuple, n: int) -> tuple:
        """將時間推進 n 個月"""
        year, mon = date
        mon += n
        if mon > 12:
            year += mon // 12
            mon %= 12
        return (year, mon)
    
    def city_change(self, date):
        """紀錄 date 時，城市變化後的結果"""
        for city, change in self.trend.get(date, []):
            if change == 'BUILT':
                self.cities_data[city] += self.x
            elif change == 'BOOST':
                self.cities_data[city] += self.x ** 2
            elif change == 'DAMAGE':
                self.cities_data[city] -= self.y
                if self.cities_data[city] < 0:
                    self.cities_data[city] = 0
            else:   # if change == 'RUIN'
                self.cities_data[city] = 0
    
    def print_all(self):
        """測試用，用來肉眼檢查變量初始化的內容是否正確"""
        print(
            f'date_start: {self.date_start}',
            f'date_end: {self.date_end}',
            f'total_money: {self.total_money}',
            f'cities_data: {self.cities_data}',
            f'cities_order: {self.cities_order}',
            f'x, y: {self.x}, {self.y}',
            f'trend: {self.trend}',
            sep='\n'
        )


if __name__ == '__main__':
    s = Solution()
    s.mainloop()
