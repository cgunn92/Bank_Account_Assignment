import unittest
import BankAccount as ba

class BankAccountTest(unittest.TestCase):
    
    def test_customer(self):
        a = ba.Customer('Caleb', '1234567890', '123', 'apt 1', 'Carlton', 'BC', 'v2r 5c7', '1', '6046875309', None)
        
        self.assertEquals(type(a._acct), str)
        self.assertEqual(len(a._cellPhone), 10)
        self.assertEqual(len(a._postCode), 7)
        self.assertEqual(len(a._workPhone), 10)
        self.assertEquals(type(a._acct), str)
        
    def test_account(self):
        a = ba.Account(2359, '1', '1')
        
        self.assertLessEqual(a._balance, 2147483647)
        self.assertGreaterEqual(a._balance, -2147483648)
        