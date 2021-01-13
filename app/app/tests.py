from django.test import TestCase
from app.calc import add,sub

class CalcTest(TestCase):
	def test_add_numbers(self):
		self.assertEqual(add(3,8),11)

	def test_subtract_numbers(self):
		self.assertEqual(sub(7,5),2)
