import unittest
from introduce import Introduce

class TestIntroduce(unittest.TestCase):

    def test_say_hi(self):
        introduction = Introduce()
        expected = "Hi Anita"
        greeting = introduction.sayHi("Anita")
        self.assertEqual(greeting, expected)