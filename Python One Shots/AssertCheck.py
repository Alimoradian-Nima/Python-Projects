import unittest

class Tester(unittest.TestCase):
    def test_is_prime(self):
        # Test cases for the is_prime function
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(768))


# function that rreturns true if the number is prime and false if not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#A function that when passed a number, returns the number rounded to the nearest integer.
def round_number(num):
    return round(num)

if __name__ == "__main__":    
    unittest.main() 