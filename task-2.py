import re
from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):

    numbers_from_string = re.findall(r'\b-?\d+\.?\d*\b', text)
    for num in numbers_from_string:
        yield float(num)
        

def sum_profit(text: str, func: Callable):
    total_sum = sum(func(text))
    return total_sum

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")