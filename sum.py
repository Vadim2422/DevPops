import unittest

import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.sum(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
