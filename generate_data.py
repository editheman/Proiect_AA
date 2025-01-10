import random

def generate_knapsack_test(n: int, max_weight: int, max_value: int, capacity: int) -> str:
    items = [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(n)]
    
    input_data = f"{n} {capacity}\n"
    for weight, value in items:
        input_data += f"{weight} {value}\n"

    return input_data

def generate_knapsack_tests(output_dir: str):
    normal_cases = [
        (10, 20, 100, 50),  # numar mic de obiecte, capacitate medie
        (50, 100, 1000, 500),  # numar moderat de obiecte, capacitate mare
        (100, 50, 500, 1000),  # numar mare de obiecte, capacitate foarte mare
    ]

    edge_cases = [
        (1, 1, 1, 1),  # un singur obiect cu greutatea si valoarea minima
        (1, 1000000, 1000000, 1000000),  # un singur obiect mare
        (10000, 1, 1, 1000000),  # multe obiecte foarte usoare
        (10000, 1000000, 1000000, 1),  # capacitate foarte mica
        (10, 1000000, 1000000, 1000000),  # numar maxim de obiecte si valori
    ]

    cases = normal_cases + edge_cases

    for i, (n, max_weight, max_value, capacity) in enumerate(cases):
        test_data = generate_knapsack_test(n, max_weight, max_value, capacity)
        with open(f"{output_dir}/test_{i+1}.txt", "w") as file:
            file.write(test_data)

    for i in range(len(cases), 20):
        n = random.randint(1, 1000)  # numar aleatoriu de obiecte
        max_weight = random.randint(1, 1000000)
        max_value = random.randint(1, 1000000)
        capacity = random.randint(1, 1000000)

        test_data = generate_knapsack_test(n, max_weight, max_value, capacity)
        with open(f"{output_dir}/test_{i+1}.txt", "w") as file:
            file.write(test_data)

if __name__ == "__main__":
    output_directory = "knapsack_tests"

    import os
    os.makedirs(output_directory, exist_ok=True)

    generate_knapsack_tests(output_directory)
    print(f"20 de teste au fost generate in directorul '{output_directory}'.")
