"""
Commission calculator
"""

percentage = 0.13  # (13 / 100)

name = input("What is your name? ")
sales = float(input("What are your total sales? "))

total = sales * percentage

print(f"{name} your final commission is ${round(total, 2)}")
