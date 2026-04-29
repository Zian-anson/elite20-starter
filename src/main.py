"""
Elite20 Starter Project - Main Module
Author: Your Name
Date: 2024
"""

def greet(name: str) -> str:
    """生成问候语"""
    return f"Hello, {name}! Welcome to Elite20 Challenge System."

def calculate_sum(a: int, b: int) -> int:
    """计算两个数的和"""
    return a + b

def process_data(data: list) -> list:
    """处理数据列表，返回平方值"""
    return [x ** 2 for x in data]

if __name__ == "__main__":
    print(greet("Elite20 Learner"))
    print(f"Sum: {calculate_sum(10, 20)}")
    print(f"Processed: {process_data([1, 2, 3, 4, 5])}")