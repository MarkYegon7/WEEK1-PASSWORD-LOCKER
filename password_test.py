import unittest

def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.user_account.first_name,"go.com")
        self.assertEqual(self.user_account.last_name,"12345")
        

if __name__ == '__main__':
    unittest.main()