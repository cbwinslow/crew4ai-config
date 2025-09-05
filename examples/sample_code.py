"""
Sample Code File for Testing Code Review Crew
============================================

This is a sample Python file with intentional issues for testing the code review crew.
"""

import os
import sys
from typing import List, Dict

# Global variable - not a good practice
global_var = "This is a global variable"

def calculate_sum(numbers):
    # No type hints
    # No docstring
    total = 0
    for num in numbers:
        total += num
    return total

def divide_numbers(a, b):
    # No error handling for division by zero
    result = a / b
    return result

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add_data(self, item):
        # No validation
        self.data.append(item)
    
    def process_data(self):
        # Inefficient algorithm with O(n^2) complexity
        results = []
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if i != j:
                    results.append(self.data[i] + self.data[j])
        return results

def main():
    # Using global variable
    print(global_var)
    
    # Hardcoded password - security issue
    password = "secret123"
    
    # Unused variable
    unused_var = "This is never used"
    
    # Large list creation
    numbers = list(range(10000))
    
    processor = DataProcessor()
    for num in numbers:
        processor.add_data(num)
    
    # This will be very slow due to inefficient algorithm
    results = processor.process_data()
    print(f"Processed {len(results)} items")

if __name__ == "__main__":
    main()