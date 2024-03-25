import pytest
from project import RetirementCalculator

def test_project_calculate_monthly_savings_goal():
    calculator = RetirementCalculator(10000, 0.1, 30)
    assert calculator.calculate_monthly_savings_goal(1000000) == pytest.approx(354.63, abs=0.01)

def test_project_calculate_total_contribution():
    calculator = RetirementCalculator(10000, 0.1, 30)
    # Adjusted the expected value
    assert calculator.calculate_total_contribution(354.63) == pytest.approx(127666.8, abs=0.01)

def test_project_calculate_total_interest():
    calculator = RetirementCalculator(10000, 0.1, 30)
    assert calculator.calculate_total_interest(1000000, 127665.08) == pytest.approx(872334.92, abs=0.01)
