import sys
import os

# Добавляем папку src в путь, чтобы импортировать модуль
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tip_calculator import calculate_tip

def test_calculate_tip_single():
    """Тест расчета для одного человека"""
    result = calculate_tip(1000, 15)
    assert result["total_bill"] == 1150.0
    assert result["tip_amount"] == 150.0
    assert result["amount_per_person"] == 1150.0

def test_calculate_tip_split():
    """Тест расчета для компании"""
    result = calculate_tip(1000, 20, 4)
    assert result["total_bill"] == 1200.0
    assert result["tip_amount"] == 200.0
    assert result["amount_per_person"] == 300.0

def test_calculate_tip_invalid_input():
    """Тест на некорректный ввод"""
    result = calculate_tip("не число", 15)
    assert "error" in result

if __name__ == "__main__":
    test_calculate_tip_single()
    test_calculate_tip_split()
    test_calculate_tip_invalid_input()
    print("Все тесты прошли успешно!")
