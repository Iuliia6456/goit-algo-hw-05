from typing import List, Optional, Tuple

def binary_search(arr: List[float], x: float) -> Tuple[int, Optional[float]]:
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = arr[mid]

        iterations += 1

        if mid_value == x:
            return iterations, mid_value
        elif mid_value < x:
            left = mid + 1
        else:
            right = mid - 1

    if left < len(arr) and arr[left] > x:
        upper_limit = arr[left]
    else:
        upper_limit = None
    
    return iterations, upper_limit

array = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
x = 0.5

result = binary_search(array, x)
print(result)

print(f"\nNumber of iterations: {result[0]}")
print(f"Upper limit: {result[1]}\n")

