import pytest
from app.calculator import Calculator

class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_adding_success(self):
       assert self.calc.adding(self, 18, 2) == 20 #тестирование операции сложение

   def test_subtraction_success(self):
       assert self.calc.subtraction(self, 18, 2) == 16 #тестирование операции вычитание

   def test_division_success(self):
        assert self.calc.division(self, 18, 2) == 9.0 #тестирование операции деление

   def test_multiply_success(self):
        assert self.calc.multiply(self, 18, 2) == 36 #тестирование операции умножение

   def teardown(self):
       print ('Тестирование выполнено.')