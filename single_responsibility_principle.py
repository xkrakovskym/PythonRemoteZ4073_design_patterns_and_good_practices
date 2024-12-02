def math_operations(numbers: list[int]) -> None:
    print(f"Mean is {sum(numbers) / len(numbers)}")
    print(f"Max value is {max(numbers)}")

def mean(numbers: list[int]) -> float:
    return sum(numbers)/len(numbers)

def max_value(numbers: list[int]) -> int:
    return max(numbers)

numbers = [1.2, 2.3, 4.5]

print(max_value(numbers))
