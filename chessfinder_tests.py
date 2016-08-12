# Chess Tests
import unittest

TEST_BOARD = [
    ['r-b','k-b','b-b','q-b','k-b','b-b','k-b','r-b'],
    ['p-b','p-b','p-b','p-b','p-b','p-b','p-b','p-b'],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['r-w','k-w','b-w','q-w','k-w','b-w','k-w','r-w'],
    ['p-w','p-w','p-w','p-w','p-w','p-w','p-w','p-w'],
]

class TestChessFinder(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
