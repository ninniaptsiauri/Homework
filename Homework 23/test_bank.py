import unittest
import bank

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = bank.BankAccount("John Doe", 1000)

    
    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)


    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)


    def test_negative_deposit(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100)
        self.assertEqual(str(context.exception), "Deposit amount must be positive")


    def test_zero_deposit(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(0)
        self.assertEqual(str(context.exception), "Deposit amount must be positive")

          
    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.get_balance(), 500)


    def test_zero_withdraw(self):
        self.account.withdraw(0)
        self.assertEqual(self.account.get_balance(), 1000)

    
    def test_withdraw_full_balance(self):  
        self.account.withdraw(1000)
        self.assertEqual(self.account.get_balance(), 0)


    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(1500)
        self.assertEqual(str(context.exception), "Insufficient funds")

    
    def test_multiple_methods(self):
        self.account.deposit(500)
        self.account.withdraw(300)
        self.account.deposit(350)
        self.account.withdraw(250)
        self.assertEqual(self.account.get_balance(), 1300)

        


if __name__ == '__main__':
    unittest.main()