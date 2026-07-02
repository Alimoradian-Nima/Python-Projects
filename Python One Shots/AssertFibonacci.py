import unittest

# n = int(input("Enter a number: "))

def fibonacci_sum(n):
    if type(n) != int:
        return False
    if n <= 0:
        return 0
    #return the nth Fibonacci number with loop
    a, b = 0, 1 
    for _ in range(n+1):
        a, b = b, a + b
    return a-1


# print(fibonacci_sum(n))

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_sum(self):
        self.assertEqual(fibonacci_sum(0), 0)
        self.assertEqual(fibonacci_sum(1), 0)
        self.assertEqual(fibonacci_sum(2), 1)
        self.assertEqual(fibonacci_sum(3), 2)
        self.assertEqual(fibonacci_sum(4), 4)
        self.assertEqual(fibonacci_sum(5), 7)
        self.assertEqual(fibonacci_sum(-2), 0)
        self.assertFalse(fibonacci_sum("abc"))
        self.assertFalse(fibonacci_sum("string"))

if __name__ == "__main__":    
    unittest.main() 