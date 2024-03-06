import math

def multiply_numbers(numbers):
    result = math.prod(numbers)
    return result

if __name__ == "__main__":
    numbers = [int(i) for i in input().split()]
    result = multiply_numbers(numbers)
    print("Result:", result)
