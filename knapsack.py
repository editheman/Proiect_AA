import random
import os
from typing import List, Tuple

def knapsack_backtracking(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    n = len(weights)
    max_value = 0
    best_combination = []

    def backtrack(index, current_weight, current_value, current_combination):
        nonlocal max_value, best_combination

        if current_weight > capacity:
            return

        if current_value > max_value:
            max_value = current_value
            best_combination = current_combination[:]

        if index == n:
            return

        current_combination.append(index)
        backtrack(index + 1, current_weight + weights[index], current_value + values[index], current_combination)
        current_combination.pop()

        backtrack(index + 1, current_weight, current_value, current_combination)

    backtrack(0, 0, 0, [])
    return max_value, best_combination


def knapsack_dynamic_programming(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(2)]
    keep = [[0] * (capacity + 1) for _ in range(n)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                if dp[(i - 1) % 2][w] < dp[(i - 1) % 2][w - weights[i - 1]] + values[i - 1]:
                    dp[i % 2][w] = dp[(i - 1) % 2][w - weights[i - 1]] + values[i - 1]
                    keep[i - 1][w] = 1
                else:
                    dp[i % 2][w] = dp[(i - 1) % 2][w]
            else:
                dp[i % 2][w] = dp[(i - 1) % 2][w]

    max_value = dp[n % 2][capacity]

    selected_items = []
    w = capacity
    for i in range(n - 1, -1, -1):
        if keep[i][w] == 1:
            selected_items.append(i)
            w -= weights[i]

    return max_value, selected_items[::-1]


def knapsack_greedy(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    n = len(weights)
    items = list(range(n))
    items.sort(key=lambda i: values[i] / weights[i], reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    for i in items:
        if total_weight + weights[i] <= capacity:
            selected_items.append(i)
            total_weight += weights[i]
            total_value += values[i]

    return total_value, selected_items

def read_input_from_file(file_path: str) -> Tuple[int, List[int], List[int]]:
    with open(file_path, "r") as file:
        lines = file.readlines()
        n, capacity = map(int, lines[0].split())
        weights = []
        values = []
        for line in lines[1:]:
            weight, value = map(int, line.split())
            weights.append(weight)
            values.append(value)
    return capacity, weights, values

def run_tests_in_directory(directory: str):
    test_files = sorted([f for f in os.listdir(directory) if f.endswith(".txt")], key=lambda x: int(x.split('_')[1].split('.')[0]))

    for test_file in test_files:
        file_path = os.path.join(directory, test_file)
        print(f"\nTest {test_file}:")

        capacity, weights, values = read_input_from_file(file_path)

        bt_value, bt_items = knapsack_backtracking(weights, values, capacity)
        print("backtracking:")
        print(f"valoare maxima: {bt_value}")
        print(f"obiecte selectate: {bt_items}")

        dp_value, dp_items = knapsack_dynamic_programming(weights, values, capacity)
        print("\nprogramare Dinamică:")
        print(f"valoare maxima: {dp_value}")
        print(f"obiecte selectate: {dp_items}")

        gr_value, gr_items = knapsack_greedy(weights, values, capacity)
        print("\ngreedy:")
        print(f"valoare aproximativa: {gr_value}")
        print(f"obiecte selectate: {gr_items}")

if __name__ == "__main__":
    test_directory = "knapsack_tests"

    run_tests_in_directory(test_directory)
