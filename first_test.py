import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 10, 2) == 20

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 8, 2) == 5

    def test_adding_calc_correct(self):
        assert self.calc.adding(self, 20, 5) == 25

    def test_subtraction_calc_correct(self):
        assert self.calc.subtraction(self, 20, 7) == 13

    def test_division_calc_correct(self):
        assert self.calc.division(self, 6, 2) == 3