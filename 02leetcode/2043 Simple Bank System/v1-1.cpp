#include <vector>

using namespace std;

class Bank
{
  private:
    vector<long long> data;
    bool is_valid_user(int account)
    {
        return 0 < account && account <= data.size();
    }

  public:
    Bank(vector<long long> &balance) : data(balance)
    {
    }

    bool transfer(int account1, int account2, long long money)
    {
        if (!is_valid_user(account1) || !is_valid_user(account2))
        {
            return false;
        }
        if (data[account1 - 1] < money)
        {
            return false;
        }
        data[account1 - 1] -= money;
        data[account2 - 1] += money;
        return true;
    }

    bool deposit(int account, long long money)
    {
        if (!is_valid_user(account))
        {
            return false;
        }
        data[account - 1] += money;
        return true;
    }

    bool withdraw(int account, long long money)
    {
        if (!is_valid_user(account))
        {
            return false;
        }
        if (data[account - 1] < money)
        {
            return false;
        }
        data[account - 1] -= money;
        return true;
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */